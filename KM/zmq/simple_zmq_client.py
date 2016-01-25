from time import sleep,strftime
import zmq



port=2500
context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, u"")
socket.connect ("tcp://169.254.15.119:%s" % port)
zmienne=["x","y","z",'yaw']


while True:
# for x in range(10):
    # socket.send_unicode(u'all')


    rcv=socket.recv_unicode()
    # rcv=str(rcv)
    if rcv!=None and len(rcv)>0:
        print rcv
        splited=rcv.split(";")
        for i,element in enumerate(splited):
            nowy=element.replace(",",".")
            # print repr(element)
            # print type(element)
            print "{} - {}".format(zmienne[i],float(nowy))
            # print element.encode(encoding='utf-8')
            # m = re.search(r'\d+', element)
            # print(type(m))
            # print float(m)
    sleep(0.01)
    # print x


# if len(sys.argv) > 2:
#     socket.connect ("tcp://localhost:%s" % port1)