# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_status.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class FileStatusWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 480)
        MainWindow.setMinimumSize(QtCore.QSize(440, 480))
        MainWindow.setMaximumSize(QtCore.QSize(440, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(130, 400, 295, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 90, 401, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 130, 421, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setMinimumSize(QtCore.QSize(300, 0))
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 40, 171, 21))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 90, 100))
        self.label.setMinimumSize(QtCore.QSize(0, 100))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文件属性"))
        self.pushButton.setText(_translate("MainWindow", "应用"))
        self.pushButton_2.setText(_translate("MainWindow", "确定"))
        self.pushButton_3.setText(_translate("MainWindow", "取消"))
        self.label_8.setText(_translate("MainWindow", "创建时间:"))
        self.label_11.setText(_translate("MainWindow", "2019‎年‎4‎月‎30‎日, ‎星期二，‏‎14:39:12"))
        self.label_13.setText(_translate("MainWindow", "2019‎年‎4‎月‎30‎日, ‎星期二，‏‎14:39:46"))
        self.label_6.setText(_translate("MainWindow", "大小:"))
        self.label_2.setText(_translate("MainWindow", "文件类型:"))
        self.label_3.setText(_translate("MainWindow", "html网页文件"))
        self.label_4.setText(_translate("MainWindow", "位置:"))
        self.label_9.setText(_translate("MainWindow", "2019‎年‎4‎月‎30‎日, ‎星期二，‏‎14:39:41"))
        self.label_10.setText(_translate("MainWindow", "修改时间:"))
        self.label_7.setText(_translate("MainWindow", "56.5KB"))
        self.label_12.setText(_translate("MainWindow", "访问时间:"))
        self.label_5.setText(_translate("MainWindow", "D:\\graduation-project\\articl\\csdnCSDN-专业IT技术社区\\"))
        self.lineEdit.setText(_translate("MainWindow", "文件名"))
        self.label.setText(_translate("MainWindow", "文件类型图片"))

