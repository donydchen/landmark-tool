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
        Landmark.resize(1000, 600)
        self.centralwidget = QtGui.QWidget(Landmark)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 980, 520))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.imgShow = QtGui.QGraphicsView(self.gridLayoutWidget)
        self.imgShow.setObjectName(_fromUtf8("imgShow"))
        self.gridLayout.addWidget(self.imgShow, 0, 4, 1, 1)
        self.nameList = QtGui.QListView(self.gridLayoutWidget)
        self.nameList.setObjectName(_fromUtf8("nameList"))
        self.gridLayout.addWidget(self.nameList, 0, 0, 1, 3)
        Landmark.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Landmark)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        Landmark.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Landmark)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Landmark.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Landmark)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Landmark.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen_Folder = QtGui.QAction(Landmark)
        self.actionOpen_Folder.setObjectName(_fromUtf8("actionOpen_Folder"))
        self.actionSave_File = QtGui.QAction(Landmark)
        self.actionSave_File.setObjectName(_fromUtf8("actionSave_File"))
        self.actionExit = QtGui.QAction(Landmark)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(Landmark)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addAction(self.actionSave_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Landmark)
        QtCore.QMetaObject.connectSlotsByName(Landmark)

    def retranslateUi(self, Landmark):
        Landmark.setWindowTitle(_translate("Landmark", "Landmark Tool", None))
        self.menuFile.setTitle(_translate("Landmark", "File", None))
        self.menuHelp.setTitle(_translate("Landmark", "Help", None))
        self.toolBar.setWindowTitle(_translate("Landmark", "toolBar", None))
        self.actionOpen_Folder.setText(_translate("Landmark", "Open Folder", None))
        self.actionOpen_Folder.setShortcut(_translate("Landmark", "Ctrl+O", None))
        self.actionSave_File.setText(_translate("Landmark", "Save File", None))
        self.actionSave_File.setShortcut(_translate("Landmark", "Ctrl+S", None))
        self.actionExit.setText(_translate("Landmark", "Quit", None))
        self.actionExit.setShortcut(_translate("Landmark", "Ctrl+Q", None))
        self.actionAbout.setText(_translate("Landmark", "About", None))

