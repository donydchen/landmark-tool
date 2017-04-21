# -*- coding:utf-8 -*-
from PyQt4 import QtCore, QtGui
from ui.main_win_ui import Ui_Landmark
from utils import get_imgnames
from os.path import expanduser, join
import json


__all__ = ["MainWin"]


class MainWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Landmark()
        self.ui.setupUi(self)

        self.init_toolbar()
        self.setup_connect()
        self.point_dict = {}
        self.point_rad = 3
        self.point_pen = QtGui.QPen(QtCore.Qt.red)
        self.point_pen.setWidth(2)

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
            self.point_dict[unicode(imgname)] = []
            item = QtGui.QStandardItem(unicode(imgname))
            model.appendRow(item)
        self.ui.nameList.setModel(model)

    def show_img(self, index):
        self.scene = QtGui.QGraphicsScene()
        self.ui.imgShow.setScene(self.scene)
        self.cur_img = unicode(str(index.data().toString()))
        pixmap = QtGui.QPixmap(join(str(self.pathname), self.cur_img))
        img_width = self.ui.imgShow.size().width() - 5
        self.dis_scale = float(pixmap.width()) / float(img_width)
        pixmap = pixmap.scaledToWidth(img_width)
        pixmap = QtGui.QGraphicsPixmapItem(pixmap, None, self.scene)
        # append existing point
        for item in self.point_dict[self.cur_img]:
            self.scene.addEllipse(item[0] - self.point_rad, item[1] - self.point_rad,
                                  self.point_rad * 2, self.point_rad * 2,
                                  self.point_pen)

        pixmap.mousePressEvent = self.point_select

    def point_select(self, event):
        point = event.pos()
        self.point_dict[self.cur_img].append([point.x(), point.y()])
        self.scene.addEllipse(point.x() - self.point_rad, point.y() - self.point_rad,
                              self.point_rad * 2, self.point_rad * 2,
                              self.point_pen)

    def save_points(self):
        with open("landmarks.json", "wb") as f:
            json.dump(self.point_dict, f)

    def closeEvent(self, event):
        self.save_points()
