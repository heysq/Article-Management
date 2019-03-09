import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import *


class MyDialog(QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setUI()

    def setUI(self):
        self.resize(300,200)
        self.layout = QVBoxLayout()
        self.label1 = QLabel('text',self)
        self.label2 = QLabel('text',self)
        self.btn = QPushButton('确定', self)
        self.btn.setGeometry(QRect(250,150,50,50))
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyDialog()
    win.show()
    sys.exit(app.exec_())



