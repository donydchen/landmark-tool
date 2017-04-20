# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Landmark(object):
    def setupUi(self, Landmark):
        Landmark.setObjectName(_fromUtf8("Landmark"))
        Landmark.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Landmark)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 521))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.imgShow = QtGui.QGraphicsView(self.gridLayoutWidget)
        self.imgShow.setObjectName(_fromUtf8("imgShow"))
        self.gridLayout.addWidget(self.imgShow, 0, 3, 1, 1)
        self.nameList = QtGui.QListView(self.gridLayoutWidget)
        self.nameList.setObjectName(_fromUtf8("nameList"))
        self.gridLayout.addWidget(self.nameList, 0, 0, 1, 2)
        Landmark.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Landmark)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Landmark.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Landmark)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Landmark.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Landmark)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Landmark.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(Landmark)
        QtCore.QMetaObject.connectSlotsByName(Landmark)

    def retranslateUi(self, Landmark):
        Landmark.setWindowTitle(_translate("Landmark", "Landmark Tool", None))
        self.toolBar.setWindowTitle(_translate("Landmark", "toolBar", None))

