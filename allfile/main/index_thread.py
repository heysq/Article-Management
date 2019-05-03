import os
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *



class FileListThread(QThread):
    sinOut = pyqtSignal(object)

    def __init__(self, key, filename, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.key = key
        self.filename = filename

    def run(self):
        self.file_list(self.key, self.filename)
        self.sinOut.emit(self.key)
        time.sleep(0.001)

    def file_list(self, key, filename):
        for file in os.listdir(filename):
            file_path = os.path.join(filename, file)
            if os.path.isdir(file_path):
                child = QTreeWidgetItem(key)
                child.setText(0, file)
                child.setText(1, file_path)
                child.setIcon(0, QIcon('../images/folder.png'))
                self.file_list(child, file_path)
            else:
                child = QTreeWidgetItem(key)
                child.setText(0, file)
                child.setText(1, file_path)
                if file.endswith('.jpg'):
                    child.setIcon(0, QIcon('../images/jpg.png'))
                elif file.endswith('.png'):
                    child.setIcon(0, QIcon('../images/png.png'))
                elif file.endswith('.zip'):
                    child.setIcon(0, QIcon('../images/zip.png'))
                elif file.endswith('.css'):
                    child.setIcon(0, QIcon('../images/css.png'))
                elif file.endswith(('.html', '.htm')):
                    child.setIcon(0, QIcon('../images/html.png'))
                elif file.endswith('.txt'):
                    child.setIcon(0, QIcon('../images/txt.png'))
                else:
                    child.setIcon(0, QIcon('../images/file.png'))


class FilePasteThread(QThread):
    '''
    文件粘贴线程
    '''
    sinOut = pyqtSignal(str)

    def __init__(self, source_absurl, des_url, parent=None):
        super(FilePasteThread, self).__init__(parent)
        self.source_absurl = source_absurl
        self.des_url = des_url

    def run(self):
        source_filename = os.path.basename(self.source_absurl)
        des_filename = source_filename
        if source_filename in os.listdir(os.path.dirname(self.des_url)):
            des_filename = '副本-' + source_filename
        des_absurl = os.path.join(os.path.dirname(self.des_url), des_filename)
        with open(self.source_absurl, 'rb') as fs:
            with open(des_absurl, 'wb') as fd:
                fd.write(fs.read())
        self.sinOut.emit(des_filename)







