# -*- coding:utf-8 -*-
from PyQt4 import QtCore, QtGui
from ui.main_win_ui import Ui_Landmark
from utils import get_imgnames
from os.path import expanduser, join


__all__ = ["MainWin"]


class MainWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Landmark()
        self.ui.setupUi(self)

        self.init_toolbar()
        self.setup_connect()

    def setup_connect(self):
        self.btnOpen.triggered.connect(self.file_dialog)
        self.ui.nameList.clicked.connect(self.show_img)

    def init_toolbar(self):
        self.btnOpen = QtGui.QAction(QtGui.QIcon.fromTheme("folder-open"), "Open Folder", self)
        self.ui.toolBar.addAction(self.btnOpen)
        self.btnSave = QtGui.QAction(QtGui.QIcon.fromTheme("document-save-as"),
                                     "Save File", self)
        self.ui.toolBar.addAction(self.btnSave)

        self.ui.toolBar.addSeparator()

        self.btnClear = QtGui.QAction(QtGui.QIcon.fromTheme("edit-clear"),
                                      "Clear all landmarks", self)
        self.ui.toolBar.addAction(self.btnClear)
        self.btnUndo = QtGui.QAction(QtGui.QIcon.fromTheme("edit-undo"),
                                     "Undo", self)
        self.ui.toolBar.addAction(self.btnUndo)

    def file_dialog(self):
        fd = QtGui.QFileDialog(self)
        self.pathname = fd.getExistingDirectory(caption="Open Folder",
                                                directory=expanduser("~/Pictures/PhoenixOS"))
        # show all filenames in list
        self.imgnames = get_imgnames(self.pathname)
        model = QtGui.QStandardItemModel()
        for imgname in self.imgnames:
            item = QtGui.QStandardItem(unicode(imgname))
            model.appendRow(item)
        self.ui.nameList.setModel(model)

    def show_img(self, index):
        cur_img = unicode(join(str(self.pathname), str(index.data().toString())))
        scene = QtGui.QGraphicsScene()
        pixmap = QtGui.QPixmap(cur_img)
        img_width = self.ui.imgShow.size().width()
        pixmap = pixmap.scaledToWidth(int(img_width) - 5)
        scene.addPixmap(pixmap)
        self.ui.imgShow.setScene(scene)
