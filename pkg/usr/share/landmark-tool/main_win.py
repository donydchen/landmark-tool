# -*- coding:utf-8 -*-
from PyQt4 import QtCore, QtGui
from ui.main_win_ui import Ui_Landmark
from utils import get_imgnames
from os.path import expanduser, join, isfile
import json


__all__ = ["MainWin"]


class MainWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Landmark()
        self.ui.setupUi(self)

        self.init_toolbar()
        self.setup_connect()

        self.setFixedSize(self.size())

    def setup_connect(self):
        self.btnOpen.triggered.connect(self.file_dialog)
        self.ui.actionOpen_Folder.triggered.connect(self.file_dialog)
        self.btnClear.triggered.connect(self.rm_points)
        self.btnSave.triggered.connect(self.dump_dict)
        self.ui.actionSave_File.triggered.connect(self.dump_dict)
        self.btnUndo.triggered.connect(self.rm_last_point)
        self.ui.nameList.clicked.connect(self.show_img)
        self.ui.actionExit.triggered.connect(self.close)

    @QtCore.pyqtSlot()
    def on_actionAbout_triggered(self):
        QtGui.QMessageBox.about(None, "About Landmark Tool",
            "<p align='center' style='font-size:16pt'><b>Landmark Tool</b>"
            " is a simple application that helps you to landmark images</p>"
            "<p align='center' style='font-size:12pt'>Developed by <b>Donald</b>.</p>"
            "<p align='center' style='font-size:12pt'>April 2017</p>")

    def init_toolbar(self):
        self.ui.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnOpen = QtGui.QAction(QtGui.QIcon.fromTheme("folder-open"), "Open Folder", self)
        self.ui.toolBar.addAction(self.btnOpen)
        self.btnSave = QtGui.QAction(QtGui.QIcon.fromTheme("document-save-as"),
                                     "Save File", self)
        self.ui.toolBar.addAction(self.btnSave)

        self.ui.toolBar.addSeparator()

        self.btnClear = QtGui.QAction(QtGui.QIcon.fromTheme("edit-clear"),
                                      "Clear All", self)
        self.ui.toolBar.addAction(self.btnClear)
        self.btnUndo = QtGui.QAction(QtGui.QIcon.fromTheme("edit-undo"),
                                     "Undo", self)
        self.ui.toolBar.addAction(self.btnUndo)


    def file_dialog(self):
        # init all variables
        self.points_dict = {}
        self.cur_points = []
        self.cur_img = ""
        self.point_rad = 3
        self.point_pen = QtGui.QPen(QtCore.Qt.red)
        self.point_pen.setWidth(2)
        # get folder path
        fd = QtGui.QFileDialog(self)
        self.pathname = fd.getExistingDirectory(caption="Open Folder",
                                                directory=expanduser("~"))
        # load landmarks
        self.json_file = join(str(self.pathname), "landmarks.json")
        if isfile(self.json_file):
            with open(self.json_file) as json_data:
                self.points_dict = dict(json.load(json_data))
        # show all filenames in list
        self.imgnames = get_imgnames(self.pathname)
        model = QtGui.QStandardItemModel()
        for imgname in self.imgnames:
            if not unicode(imgname) in self.points_dict:
                self.points_dict[unicode(imgname)] = []
            item = QtGui.QStandardItem(unicode(imgname))
            model.appendRow(item)
        self.ui.nameList.setModel(model)

    def show_img(self, index):
        # save the previous image point, and reset
        if self.cur_img:
            self.save_cur_points()
            self.cur_points = []

        self.scene = QtGui.QGraphicsScene()
        self.ui.imgShow.setScene(self.scene)
        # read image, scale to proper size
        self.cur_img = unicode(str(index.data().toString()))
        pixmap = QtGui.QPixmap(join(str(self.pathname), self.cur_img))
        img_width = self.ui.imgShow.size().width() - 5
        self.dis_scale = 1.0
        if img_width < pixmap.width():
            self.dis_scale = float(pixmap.width()) / float(img_width)
            pixmap = pixmap.scaledToWidth(img_width)
        pixmap = QtGui.QGraphicsPixmapItem(pixmap, None, self.scene)
        # append existing point
        for item in self.points_dict[self.cur_img]:
            cur_point = self.scene.addEllipse(item[0] / self.dis_scale - self.point_rad,
                                              item[1] / self.dis_scale - self.point_rad,
                                              self.point_rad * 2, self.point_rad * 2,
                                              self.point_pen)
            self.cur_points.append(cur_point)
        # add mouse click event
        pixmap.mousePressEvent = self.draw_point

    def draw_point(self, event):
        cur_point = self.scene.addEllipse(event.pos().x() - self.point_rad,
                                          event.pos().y() - self.point_rad,
                                          self.point_rad * 2, self.point_rad * 2,
                                          self.point_pen)
        self.cur_points.append(cur_point)

    def save_cur_points(self):
        self.points_dict[self.cur_img] = []
        for item in self.cur_points:
            rect = item.rect().getRect()
            self.points_dict[self.cur_img].append(\
                [int((rect[0] + self.point_rad) * self.dis_scale),
                 int((rect[1] + self.point_rad) * self.dis_scale)])

    def dump_dict(self):
        self.save_cur_points()
        with open(self.json_file, "wb") as f:
            json.dump(self.points_dict, f)

    def rm_points(self):
        while self.cur_points:
            self.rm_last_point()

    def rm_last_point(self):
        if self.cur_points:
            last_point = self.cur_points.pop()
            if last_point and isinstance(last_point, QtGui.QGraphicsEllipseItem):
                self.scene.removeItem(last_point)

    def closeEvent(self, event):
        self.dump_dict()
