# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saveWindow_demo.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import json
import os
import sys
import base64

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog
from urllib.parse import unquote

from save_thread import SavePageUrlThread


class Ui_MainWindow(object):
    def __init__(self, mainWindow, args):
        super().__init__()
        f_settings = open('D:\\chrome_back\\dist\\settings.json', 'r')
        self.settings = json.load(f_settings)
        f_settings.close()
        self.mainwindow = mainWindow
        self.args = args

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(81, 62, 321, 346))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(40)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("text-align=center")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 2, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 4, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "浏览器保存"))
        type_list = os.listdir(self.settings['FILE_LOCATION'])
        for index, type in enumerate(type_list):
            self.comboBox.addItem('')
            self.comboBox.setItemText(index, _translate("MainWindow", type))
        self.label_3.setText(_translate("MainWindow", "文件名:"))
        self.pushButton.setText(_translate("MainWindow", "新建分类"))
        self.label_2.setText(_translate("MainWindow", "网页URL:"))
        self.pushButton_2.setText(_translate("MainWindow", "保存网页"))
        try:
            self.save_url = self.args[1].split('//', 1)[1].split("netarticle", 1)[0]
        except:
            self.save_url = 'http://www.baidu.com'
        try:
            self.url_title = self.args[1].split('netarticletitle=', 1)[1].split('netarticlecookie', 1)[0]
            self.url_title = unquote(self.url_title)
        except:
            self.url_title = 'test-file'
        try:
            self.cookies = sys.argv[1].split('netarticlecookie=', 1)[1]
            self.decode_cookies = base64.b64decode(self.cookies.encode('utf-8'))
            # print(cookies)
        except:
            self.decode_cookies = []
        # print(self.save_url, self.cookies, self.url_title)
        self.textBrowser.setHtml(_translate("MainWindow", self.save_url))
        self.lineEdit.setText(self.url_title)
        self.label.setText(_translate("MainWindow", "网页分类"))
        self.pushButton.clicked.connect(self.new_type)
        self.pushButton_2.clicked.connect(self.save_page)

    def new_type(self):
        value, ok = QInputDialog.getText(None, '新建分类', '新建分类名') # value 为输入框的值，如果不输入或点击cancel则value为空
        if value:
            self.comboBox.addItem('')
            self.comboBox.setItemText(len(self.comboBox) - 1, value)
            self.comboBox.setCurrentIndex(len(self.comboBox) - 1)
            os.mkdir(os.path.join(self.settings['FILE_LOCATION'], value))

    def save_page(self):
        url_type = self.comboBox.currentText()
        filename = self.lineEdit.text()
        reply = QMessageBox.information(self.mainwindow, '确认保存', '分类：' + url_type + '\n文件名：' + filename,
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == 16384:
            print('用户选择保存网页')
            # print(self.decode_cookies)
            self.save_thread = SavePageUrlThread(self.save_url, url_type, filename, self.settings['FILE_LOCATION'],
                                                 self.decode_cookies)
            self.save_thread.start()
            self.save_thread.sinOut.connect(self.save_page_result)

    def save_page_result(self, msg):
        print(msg)
        self.save_thread.wait()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow(MainWindow, sys.argv)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
