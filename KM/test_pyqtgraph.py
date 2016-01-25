# -*- coding: utf-8 -*-
"""
Demonstrates use of PlotWidget class. This is little more than a
GraphicsView with a PlotItem placed in its center.
"""


# import initExample ## Add path to library (just for examples; you do not need this)


from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.setWindowTitle('pyqtgraph example: PlotWidget')
mw.resize(800,800)
cw = QtGui.QWidget()
mw.setCentralWidget(cw)
l = QtGui.QVBoxLayout()
cw.setLayout(l)

pw = pg.PlotWidget(name='Plot1')  ## giving the plots names allows us to link their axes together
l.addWidget(pw)




mw.show()

## Create an empty plot curve to be filled later, set its pen
p1 = pw.plot()

p1.setPen((200,200,100))

## Add in some extra graphics
rect = QtGui.QGraphicsRectItem(QtCore.QRectF(0, 0, 1, 5e-11))
rect.setPen(QtGui.QPen(QtGui.QColor(100, 200, 100)))
pw.addItem(rect)

pw.setLabel('left', 'Value', units='V')
pw.setLabel('bottom', 'Time', units='s')
pw.setXRange(0, 2)
pw.setYRange(0, 1e-10)

def rand(n):
    data = np.random.random(n)
    data[int(n*0.1):int(n*0.13)] += .5
    data[int(n*0.18)] += 2
    data[int(n*0.1):int(n*0.13)] *= 5
    data[int(n*0.18)] *= 20
    data *= 1e-12
    print np.arange(n, n+len(data)) / float(n)
    return data, np.arange(n, n+len(data)) / float(n)



def updateData():
    yd, xd = rand(10000)
    p1.setData(y=yd, x=xd)


## Start a timer to rapidly update the plot in pw
t = QtCore.QTimer()
t.timeout.connect(updateData)
t.start(50)




## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
