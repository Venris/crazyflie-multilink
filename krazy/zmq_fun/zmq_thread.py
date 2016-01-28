from PyQt4.QtCore import QThread,pyqtSignal
from time import time



class zmq_thread(QThread):
    # watek odbierajacy dane z ZMQ
    zmq_log=pyqtSignal(list)
    def __init__(self,socket):
        QThread.__init__(self)
        self.socket=socket
        self.isAlive=True

    def __del__(self):

        self.isAlive = False
        self.wait()

    def run(self):
        previous_time=time()
        while self.isAlive:

            rcv=self.socket.recv_unicode()

            actual_time=time()
            dt=actual_time-previous_time
            previous_time=actual_time
            # print rcv
            if rcv!=None and len(rcv)>0 and dt!=0:
                rcv=rcv.replace(",",".")
                splited=rcv.split(";")
                for i,s in enumerate(splited):
                    splited[i]=float(s)
                splited.append(dt)
                self.zmq_log.emit(splited)