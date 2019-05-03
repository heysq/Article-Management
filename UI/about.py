# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class AboutDialog(QDialog):
    def __init__(self,parent = None):
        super(AboutDialog, self).__init__(parent)
        self.setWindowTitle('关于网络文章管理系统')
        self.setUi()

    def setUi(self):

        # 软降窗口固定大小
        self.setFixedSize(500,300)

        # 软件图片
        self.label1 = QLabel()

        self.label1.setText('软件商标')
        qPixmap = QPixmap('UI/images/software.jpg')
        self.label1.setPixmap(qPixmap)
        self.label1.resize(256,256)
        self.label1.setScaledContents(True)

        # 软件作者
        self.author_label = QLabel()
        self.author_label.setText('开发人员：孙琦')
        self.author_label.setGeometry(280, 70, 200, 200)
        self.author_label.resize(150, 100)

        # 联系方式
        self.tel_label = QLabel()
        self.tel_label.setText('邮箱：15735657423@163.com')
        self.tel_label.setGeometry(280, 90, 200, 200, )
        self.tel_label.resize(210, 100)

        total_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()


        left_layout.addWidget(self.label1)

        right_layout.addWidget(self.author_label)
        right_layout.addWidget(self.tel_label)


        total_layout.addLayout(left_layout)
        total_layout.addLayout(right_layout)

        self.setLayout(total_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AboutDialog()
    win.show()
    sys.exit(app.exec_())