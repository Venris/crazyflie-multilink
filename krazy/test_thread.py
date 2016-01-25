from threading import Thread
from time import *


class ttt(Thread):
    def __init__(self):
        super(ttt,self).__init__()
        self.dziala=True


    def run(self):
        while self.dziala:
            print (time())
            sleep(0.1)

    def stop(self):
        self.dziala=False


a=ttt()
a.start()

sleep(2)
print a.isAlive()
# print ("joining")
# a.join(timeout=0.1)
a.stop()
# print a.isAlive()
# print ("joining")
# a.join()



sleep(2)
# a=ttt()
# a.start()
# a.join()
print a.isAlive()
sleep(1)




