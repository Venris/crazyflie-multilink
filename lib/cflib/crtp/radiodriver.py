#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#     ||          ____  _ __
#  +------+      / __ )(_) /_______________ _____  ___
#  | 0xBC |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
#  +------+    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#   ||  ||    /_____/_/\__/\___/_/   \__,_/ /___/\___/
#
#  Copyright (C) 2011-2013 Bitcraze AB
#
#  Crazyflie Nano Quadcopter Client
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA  02110-1301, USA.

"""
Crazyradio CRTP link driver.

This driver is used to communicate with the Crazyflie using the Crazyradio
USB dongle.
"""

__author__ = 'Bitcraze AB'
__all__ = ['RadioDriver']

import logging
logger = logging.getLogger(__name__)

from cflib.crtp.crtpdriver import CRTPDriver
from .crtpstack import CRTPPacket
from .exceptions import WrongUriType
import threading
import Queue
import re
import array
import binascii
import struct

from cflib.drivers.crazyradio import Crazyradio
from usb import USBError


class RadioDriver(CRTPDriver):
    """ Crazyradio link driver """

    # Class variable containing currently in-use transfer threads
    #: :type: dict of (int, _RadioTransferThread)
    transfer_threads = {}

    def __init__(self):
        """ Create the link driver """
        CRTPDriver.__init__(self)
        self.uri = ""
        self.link_error_callback = None
        self.link_quality_callback = None
        self.in_queue = None
        self.out_queue = None
        self._thread = None
        self._profile = None
        self._radio_id = None

    def connect(self, uri, link_quality_callback, link_error_callback):
        """
        Connect the link driver to a specified URI of the format:
        radio://<dongle nbr>/<radio channel>/[250K,1M,2M]

        The callback for linkQuality can be called at any moment from the
        driver to report back the link quality in percentage. The
        callback from linkError will be called when a error occues with
        an error message.
        """

        # check if the URI is a radio URI
        if not re.search("^radio://", uri):
            raise WrongUriType("Not a radio URI")

        # Open the USB dongle
        if not re.search("^radio://([0-9]+)((/([0-9]+))((/(250K|1M|2M))?(/([A-F0-9]+))?)?)?$",
                         uri):
            raise WrongUriType('Wrong radio URI format!')

        uri_data = re.search("^radio://([0-9]+)((/([0-9]+))"
                             "((/(250K|1M|2M))?(/([A-F0-9]+))?)?)?$",
                             uri)

        self.uri = uri

        channel = 2
        if uri_data.group(4):
            channel = int(uri_data.group(4))

        datarate = Crazyradio.DR_2MPS
        if uri_data.group(7) == "250K":
            datarate = Crazyradio.DR_250KPS
        if uri_data.group(7) == "1M":
            datarate = Crazyradio.DR_1MPS
        if uri_data.group(7) == "2M":
            datarate = Crazyradio.DR_2MPS

        self._radio_id = int(uri_data.group(1))

        new_addr = Crazyradio.DEFAULT_ADDRESS
        if uri_data.group(9):
            addr = str(uri_data.group(9))
            new_addr = struct.unpack("<BBBBB", binascii.unhexlify(addr))

        self._profile = _RadioProfile(channel, datarate, new_addr)

        if not self.transfer_threads.has_key(self._radio_id):
            self.transfer_threads[self._radio_id] = _RadioTransferThread(self._radio_id)
            self.transfer_threads[self._radio_id].setDaemon(True)

            self.transfer_threads[self._radio_id].start()

        #Connect this profile to the transfers thread
        handle = self.transfer_threads[self._radio_id].add_profile()
        self._profile.handle = handle

        # Prepare the inter-thread communication queue
        self.in_queue = Queue.Queue()
        # Limited size out queue to avoid "ReadBack" effect
        self.out_queue = Queue.Queue(50)

        # Launch the comm thread
        self._thread = _RadioDriverThread(self.transfer_threads[self._radio_id], self._profile,
                                          self.in_queue, self.out_queue,
                                          link_quality_callback,
                                          link_error_callback)
        self._thread.start()

        self.link_error_callback = link_error_callback

    def receive_packet(self, time=0):
        """
        Receive a packet though the link. This call is blocking but will
        timeout and return None if a timeout is supplied.
        """
        if time == 0:
            try:
                return self.in_queue.get(False)
            except Queue.Empty:
                return None
        elif time < 0:
            try:
                return self.in_queue.get(True)
            except Queue.Empty:
                return None
        else:
            try:
                return self.in_queue.get(True, time)
            except Queue.Empty:
                return None

    def send_packet(self, pk):
        """ Send the packet pk though the link """
        # if self.out_queue.full():
        #    self.out_queue.get()
        if self._profile is None:
            return

        try:
            self.out_queue.put(pk, True, 2)
        except Queue.Full:
            if self.link_error_callback:
                self.link_error_callback("RadioDriver: Could not send packet"
                                         " to copter")

    def pause(self):
        self._thread.stop()
        self._thread = None

    def restart(self):
        if self._thread:
            return

        self._thread = _RadioDriverThread(self.transfer_threads[self._radio_id], self._profile,
                                          self.in_queue, self.out_queue,
                                          self.link_quality_callback,
                                          self.link_error_callback)
        self._thread.start()
    def close(self):
        """ Close the link. """
        # Stop the comm thread
        self._thread.stop()

        self.transfer_threads[self._radio_id].remove_profile(self._profile.handle)
        if self.transfer_threads[self._radio_id].num_profiles() == 0:
            self.transfer_threads[self._radio_id].stop()
            del self.transfer_threads[self._radio_id]

    def _scan_radio_channels(self, cradio, start=0, stop=125):
        """ Scan for Crazyflies between the supplied channels. """
        return list(cradio.scan_channels(start, stop, (0xff,)))

    def scan_selected(self, links):
        to_scan = ()
        for l in links:
            one_to_scan = {}
            uri_data = re.search("^radio://([0-9]+)((/([0-9]+))"
                                 "(/(250K|1M|2M))?)?$",
                                 l)

            one_to_scan["channel"] = int(uri_data.group(4))

            datarate = Crazyradio.DR_2MPS
            if uri_data.group(6) == "250K":
                datarate = Crazyradio.DR_250KPS
            if uri_data.group(6) == "1M":
                datarate = Crazyradio.DR_1MPS
            if uri_data.group(6) == "2M":
                datarate = Crazyradio.DR_2MPS

            one_to_scan["datarate"] = datarate

            to_scan += (one_to_scan, )

        found = self.transfer_threads[self._radio_id].cradio.scan_selected(to_scan, (0xFF, 0xFF, 0xFF))

        ret = ()
        for f in found:
            dr_string = ""
            if f["datarate"] == Crazyradio.DR_2MPS:
                dr_string = "2M"
            if f["datarate"] == Crazyradio.DR_250KPS:
                dr_string = "250K"
            if f["datarate"] == Crazyradio.DR_1MPS:
                dr_string = "1M"

            ret += ("radio://0/{}/{}".format(f["channel"], dr_string),)

        return ret

    def scan_interface(self, address):
        """ Scan interface for Crazyflies """
        # This will cause an exception if not successful
        cradio = Crazyradio()

        # FIXME: implements serial number in the Crazyradio driver!
        serial = "N/A"

        logger.info("v%s dongle with serial %s found", cradio.version,
                    serial)
        found = []

        if address != None:
            addr = "{:X}".format(address)
            new_addr = struct.unpack("<BBBBB", binascii.unhexlify(addr))
            cradio.set_address(new_addr)

        cradio.set_arc(1)

        cradio.set_data_rate(cradio.DR_250KPS)

        if address == None or address == 0xE7E7E7E7E7:
            found += map(lambda c: ["radio://0/{}/250K".format(c), ""],
                         self._scan_radio_channels(cradio))
            cradio.set_data_rate(cradio.DR_1MPS)
            found += map(lambda c: ["radio://0/{}/1M".format(c), ""],
                         self._scan_radio_channels(cradio))
            cradio.set_data_rate(cradio.DR_2MPS)
            found += map(lambda c: ["radio://0/{}/2M".format(c), ""],
                         self._scan_radio_channels(cradio))
        else:
            found += map(lambda c: ["radio://0/{}/250K/{:X}".format(c, address), ""],
                         self._scan_radio_channels(cradio))
            cradio.set_data_rate(cradio.DR_1MPS)
            found += map(lambda c: ["radio://0/{}/1M/{:X}".format(c, address), ""],
                         self._scan_radio_channels(cradio))
            cradio.set_data_rate(cradio.DR_2MPS)
            found += map(lambda c: ["radio://0/{}/2M/{:X}".format(c, address), ""],
                         self._scan_radio_channels(cradio))

        cradio.close()
        cradio = None

        return found

    def get_status(self):
        # This will cause an exception if not successful
        cradio = Crazyradio()

        ver = cradio.version
        cradio.close()
        cradio = None

        return "Crazyradio version {}".format(ver)

    def get_name(self):
        return "radio"


# Transmit/receive radio thread
class _RadioDriverThread (threading.Thread):
    """
    Radio link receiver thread used to read data from the
    Crazyradio USB driver. """

    RETRYCOUNT_BEFORE_DISCONNECT = 10

    def __init__(self, transfers_thread, profile, inQueue, outQueue,
                 link_quality_callback, link_error_callback):
        """ Create the object """
        threading.Thread.__init__(self)
        self.transfers_thread = transfers_thread
        self._profile = profile
        self.in_queue = inQueue
        self.out_queue = outQueue
        self.sp = False
        self.link_error_callback = link_error_callback
        self.link_quality_callback = link_quality_callback
        self.retryBeforeDisconnect = self.RETRYCOUNT_BEFORE_DISCONNECT

    def stop(self):
        """ Stop the thread """
        self.sp = True
        try:
            self.join()
        except Exception:
            pass

    def run(self):
        """ Run the receiver thread """
        dataOut = array.array('B', [0xFF])
        waitTime = 0
        emptyCtr = 0

        while(True):
            if (self.sp):
                break

            try:
                ackStatus = self.transfers_thread.send_packet(self._profile, dataOut)
            except Exception as e:
                import traceback
                self.link_error_callback("Error communicating with crazy radio"
                                         " ,it has probably been unplugged!\n"
                                         "Exception:%s\n\n%s" % (e,
                                         traceback.format_exc()))

            # Analise the in data packet ...
            if ackStatus is None:
                if (self.link_error_callback is not None):
                    self.link_error_callback("Dongle communication error"
                                             " (ackStatus==None)")
                continue

            if (self.link_quality_callback is not None):
                self.link_quality_callback((10 - ackStatus.retry) * 10)

            # If no copter, retry
            if ackStatus.ack is False:
                self.retryBeforeDisconnect = self.retryBeforeDisconnect - 1
                if (self.retryBeforeDisconnect == 0 and
                        self.link_error_callback is not None):
                    self.link_error_callback("Too many packets lost")
                continue
            self.retryBeforeDisconnect = self.RETRYCOUNT_BEFORE_DISCONNECT

            data = ackStatus.data

            # If there is a copter in range, the packet is analysed and the
            # next packet to send is prepared
            if (len(data) > 0):
                inPacket = CRTPPacket(data[0], list(data[1:]))
                # print "<- " + inPacket.__str__()
                self.in_queue.put(inPacket)
                waitTime = 0
                emptyCtr = 0
            else:
                emptyCtr += 1
                if (emptyCtr > 10):
                    emptyCtr = 10
                    # Relaxation time if the last 10 packet where empty
                    waitTime = 0.01
                else:
                    waitTime = 0

            # get the next packet to send of relaxation (wait 10ms)
            try:
                outPacket = self.out_queue.get(True, waitTime)
            except Queue.Empty:
                outPacket = None

            dataOut = array.array('B')

            if outPacket:
                # print "-> " + outPacket.__str__()
                dataOut.append(outPacket.header)
                for X in outPacket.data:
                    if type(X) == int:
                        dataOut.append(X)
                    else:
                        dataOut.append(ord(X))
            else:
                dataOut.append(0xFF)


class _RadioProfile:
    def __init__(self, channel, rate, address):
        self.channel = channel
        self.rate = rate
        self.address = address


class _RadioTransferThread(threading.Thread):
    """ Thread that handles transfer for a single crazyradio hardware
    Can handles transfers form more than one radio profile (ie. link to a copter)
    """

    def __init__(self, radio_id):
        threading.Thread.__init__(self)
        self.cradio = Crazyradio(devid=radio_id)
        if self.cradio.version >= 0.4:
            self.cradio.set_arc(10)
        else:
            logger.warning("Radio version <0.4 will be obsoleted soon!")

        self._num_profiles = 0
        self.tx_queue = Queue.Queue()

        self.sp = False

    def add_profile(self):
        self._num_profiles += 1
        rx_queue = Queue.Queue()
        return rx_queue

    def remove_profile(self, handle):
        # we don't need to to anything, the python garbage collector will take care of it
        self._num_profiles -= 1

    def num_profiles(self):
        return self._num_profiles

    def send_packet(self, profile, data):
        self.tx_queue.put([profile, data])
        return profile.handle.get()

    def stop(self):
        self.sp = True
        self.tx_queue.put([None, None])
        self.join()

    def run(self):
        #Simply service transfers requests
        while not self.sp:
            tx = self.tx_queue.get()
            if self.sp:
                break
            ack = self._send_packet(tx[0], tx[1])
            tx[0].handle.put(ack)

        # Close the USB dongle
        try:
            if self.cradio:
                self.cradio.close()
                print("Closed radio")
        except:
            # If we pull out the dongle we will not make this call
            pass
        self.cradio = None

    def _send_packet(self, profile, data):
        """
        Send packet making sure the radio is configured for the
        right transfers profile
        """
        assert isinstance(profile, _RadioProfile)
        if self.cradio.channel != profile.channel:
            self.cradio.set_channel(profile.channel)
        if self.cradio.data_rate != profile.rate:
            self.cradio.set_data_rate(profile.rate)
        if self.cradio.address != profile.address:
            self.cradio.set_address(profile.address)
        return self.cradio.send_packet(data)
