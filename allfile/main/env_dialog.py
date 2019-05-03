import sys
import os
import json

from PyQt5.QtWidgets import *


class EnvDialog(QDialog):
    def __init__(self, settings, parent=None):
        super(EnvDialog, self).__init__(parent)
        self.json_settings = settings
        self.setUi()

    def setUi(self):
        self.resize(400, 200)
        self.setWindowTitle('存储路径选择')

        layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        self.file_label = QLabel()
        self.file_label.setText('请填入文件存储目录:')
        self.file_local = QLineEdit()
        self.file_local.setText(self.json_settings['FILE_LOCATION'])

        self.btn_chooseDir = QPushButton(self)
        self.btn_chooseDir.setObjectName("btn_chooseDir")
        self.btn_chooseDir.setText("选择文件夹")

        self.confirm = QPushButton(self)
        self.confirm.setText('确定')

        layout.addWidget(self.file_label)
        h_layout.addWidget(self.file_local)
        h_layout.addWidget(self.btn_chooseDir)
        layout.addLayout(h_layout)
        layout.addWidget(self.confirm)

        self.btn_chooseDir.clicked.connect(self.choose_dir)
        self.setLayout(layout)

    def choose_dir(self):
        self.file_dialog = QFileDialog.getExistingDirectory(caption='选择文件夹', directory=self.json_settings['FILE_LOCATION'])
        try:
            # os.chdir(self.file_dialog)
            self.file_local.setText(self.file_dialog)
        except:
            error_dialog = QDialog()
            err_msg = QLabel()
            err_msg.setText('目录无效，重新选择')
            error_dialog.show()


    def get_env_settings(self):
        self.json_settings['FILE_LOCATION'] = self.file_local.text()
        return self.json_settings



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = EnvDialog()
    win.show()
    sys.exit(app.exec_())
