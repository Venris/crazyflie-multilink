import time
import numpy as np

class kalman:
    def __init__(self):
        self.stan=np.matrix([0,0,0,0,0,0]).transpose()
        self.A=np.matrix([[1.0,0,0,0.01,0,0],
                          [0,1.0,0,0,0.01,0],
                          [0,0,1.0,0,0,0.01],
                          [0,0,0,1.0,0,0],
                          [0,0,0,0,1.0,0],
                          [0,0,0,0,0,1.0]])
        self.H=np.matrix([[1.0,0,0,0,0,0],
                          [0,1.0,0,0,0,0],
                          [0,0,1.0,0,0,0]])

        self.P=np.matrix([[0.1042,0,0,0.0996,0,0],
                          [0,0.1042,0,0,0.0996,0],
                          [0,0,0.0703,0,0,0.0686],
                          [0.0996,0,0,1.1473,0,0],
                          [0,0.0996,0,0,1.1473,0],
                          [0,0,0.0686,0,0,1.1149]])

        self.Q=np.eye(6)*0.01

        self.R=np.eye(3)
        self.R[-1,-1]=0.5

        self.y=np.matrix([0,0,0]).transpose()

        self.K=np.zeros((6,3))


    def licz(self,pomiarX,pomiarY,pomiarZ):
        ## faza predykcji ##
        self.stan=self.A*self.stan

        self.P=self.A*self.P*self.A.transpose()+self.Q

        ## rownanie pomiaru ##
        pomiar=np.matrix([pomiarX,pomiarY,pomiarZ]).transpose()
        self.y=pomiar-(self.H*self.stan)

        ## wzmocnienie kalmana ##
        iloczyn=(self.H*self.P*self.H.transpose())+self.R
        self.K=self.P*self.H.transpose()*(iloczyn**(-1))

        ## faza korekcji ##
        self.stan=self.stan+self.K*self.y
        self.P=(np.eye(6)-self.K*self.H)*self.P

        return self.stan


class kalman8:
    def __init__(self):
        self.stan=np.matrix([0,0,0,0,0,0,0,0]).transpose()
        self.A=np.matrix([[1.0,0,0,0.01,0,0,0,0],
                          [0,1.0,0,0,0.01,0,0,0],
                          [0,0,1.0,0,0,0.01,0,0],
                          [0,0,0,1.0,0,0,0,0],
                          [0,0,0,0,1.0,0,0,0],
                          [0,0,0,0,0,1.0,0,0],
                          [0,0,0,0,0,0,1.0,0.01],
                          [0,0,0,0,0,0,0,1.0]])
        self.H=np.matrix([[1.0,0,0,0,0,0,0,0],
                          [0,1.0,0,0,0,0,0,0],
                          [0,0,1.0,0,0,0,0,0],
                          [0,0,0,0,0,0,1.0,0]])

        # self.P=np.matrix([[0.1042,0,0,0.0996,0,0,0,0],
        #                   [0,0.1042,0,0,0.0996,0,0,0],
        #                   [0,0,0.0703,0,0,0.0686,0,0],
        #                   [0.0996,0,0,1.1473,0,0,0,0],
        #                   [0,0.0996,0,0,1.1473,0,0,0],
        #                   [0,0,0.0686,0,0,1.1149,0,0],
        #                   [0,0,0,0,0,0,0.1042,0.0996],
        #                   [0,0,0,0,0,0,0.0996,1.1473]])

        self.P=np.eye(8)*10000

        # self.Q=np.diag([1,1,1,0.1,0.1,0.1,1,0.1])
        self.Q=np.diag([1,1,0.01,0.1,0.1,1,1,0.1])

        # self.R=np.eye(4)*1000
        self.R=np.diag([10,10,1,100])
        # self.R[2,2]=0.5

        self.y=np.matrix([0,0,0,0]).transpose()

        self.K=np.zeros((8,4))


    def licz(self,pomiarX,pomiarY,pomiarZ,pomiarAlfaRad):

        ## faza predykcji ##
        self.stan=self.A*self.stan

        self.P=self.A*self.P*self.A.transpose()+self.Q

        ## rownanie pomiaru ##
        pomiar=np.matrix([pomiarX,pomiarY,pomiarZ,pomiarAlfaRad]).transpose()
        self.y=pomiar-(self.H*self.stan)

        ## wzmocnienie kalmana ##
        iloczyn=(self.H*self.P*self.H.transpose())+self.R
        self.K=self.P*self.H.transpose()*(iloczyn**(-1))

        ## faza korekcji ##
        self.stan=self.stan+self.K*self.y
        self.P=(np.eye(8)-self.K*self.H)*self.P

        return self.stan



class kalman12:
    def __init__(self):
        self.stan=np.matrix([0,0,0,0,0,0,0,0,0,0,0,0]).transpose()
        self.A=np.eye(12)
        for i in range(6):
            self.A[i,i+6]=0.01

        self.A=np.asmatrix(self.A)
        # self.A[0,6]=0.01
        # self.A[1,7]=0.01
        # self.A[2,8]=0.01
        # self.A[3,9]=0.01
        # self.A[4,10]=0.01
        # self.A[5,11]=0.01

        self.H=np.zeros((6,12))
        for i in range(6):
            self.H[i,i]=1

        self.H=np.asmatrix(self.H)


        self.P=np.eye(12)*1000.0
        # for i in range(12):
        #     # print i
        #     self.P[i,i]=1000.0
        self.P=np.asmatrix(self.P)
        # self.Q=np.diag([1,1,1,0.1,0.1,0.1,1,0.1])
        self.Q=np.diag([0.01,0.01,0.01,1,1,0.001,1,1,1,1,1,1])
        self.Q=np.asmatrix(self.Q)

        self.R=np.eye(6)
        self.R[-1,-1]=10
        self.R=np.asmatrix(self.R)
        # self.R=np.diag([10,10,1,100])
        # self.R[2,2]=0.5

        self.y=np.matrix([0,0,0,0,0,0]).transpose()

        self.K=np.zeros((12,6))
        self.K=np.asmatrix(self.K)


    def licz(self,pomiarX,pomiarY,pomiarZ,pomiarRollRad,pomiarPitchRad,pomiarYawRad):

        ## faza predykcji ##
        self.stan=self.A*self.stan

        self.P=self.A*self.P*self.A.transpose()+self.Q

        ## rownanie pomiaru ##
        pomiar=np.matrix([pomiarX,pomiarY,pomiarZ,pomiarRollRad,pomiarPitchRad,pomiarYawRad]).transpose()
        self.y=pomiar-(self.H*self.stan)

        ## wzmocnienie kalmana ##
        # print self.R
        # print (self.H*self.P*self.H.transpose())
        iloczyn=(self.H*self.P*self.H.transpose())+self.R
        self.K=self.P*self.H.transpose()*(iloczyn**(-1))

        ## faza korekcji ##
        self.stan=self.stan+self.K*self.y
        self.P=(np.eye(12)-self.K*self.H)*self.P

        return self.stan

# a=kalman12()
# b=a.licz(1,1,1,1,1,1)
#
# print np.shape(b)
# print b

