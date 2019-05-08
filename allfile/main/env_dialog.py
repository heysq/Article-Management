import json
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog, QLabel


class EnvDialog(object):
    def __init__(self):
        f = open('../settings/settings.json','rb')
        self.settings = json.load(f)
        f.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(520, 190)
        self.dialog = Dialog
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(230, 140, 271, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 50, 491, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton.clicked.connect(self.choose_dir)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.buttonBox.accepted.connect(self.update_settings)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "软件存储位置选择提示"))
        self.pushButton.setStatusTip(_translate("Dialog", "选择文件夹"))
        self.lineEdit.setText(self.settings['FILE_LOCATION'])

    def choose_dir(self):
        self.file_dialog = QFileDialog.getExistingDirectory(caption='选择文件夹',
                                                            directory=self.settings['FILE_LOCATION'])
        print(self.file_dialog)
        try:
            self.lineEdit.setText(self.file_dialog)
        except:
            error_dialog = QDialog()
            err_msg = QLabel()
            err_msg.setText('目录无效，重新选择')
            error_dialog.show()
    def update_settings(self):
        f = open('../settings/settings.json','w')
        self.settings['FILE_LOCATION'] = self.file_dialog
        json.dump(self.settings,f)
        f.close()
        QtWidgets.QMessageBox.warning(self.dialog, "提示", "修改成功！请重新打开以查看新设置!", QtWidgets.QMessageBox.Ok)
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    envdialog = EnvDialog()
    envdialog.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())


