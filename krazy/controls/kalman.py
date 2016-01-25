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

