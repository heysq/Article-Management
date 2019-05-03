# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import json
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMargins, Qt, QSize, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QAction, QDialog, QToolBar, QLineEdit, \
    QTreeWidgetItem

from env_dialog import EnvDialog
from about import AboutDialog

from index_thread import FileListThread


class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        setting_file = open('../settings/settings.json', 'r')
        self.json_settings = json.load(setting_file)
        setting_file.close()

    def setupUi(self, MainWindow):
        self.mainwindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(992, 832)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        '''菜单栏部分'''
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 26))
        self.menubar.setObjectName("menubar")
        self.localfile = QtWidgets.QMenu(self.menubar)
        self.localfile.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.localfile.setToolTipDuration(5)
        self.localfile.setToolTipsVisible(False)
        self.localfile.setObjectName("localfile")
        self.localfile_action = QAction(self.mainwindow)
        self.localfile_action.setCheckable(False)
        self.localfile_action.setObjectName('localFileAction')
        self.localfile_action.triggered.connect(self.openLocalFile)
        self.localfile_action.setText('本地文件')

        self.usagespace = QtWidgets.QMenu(self.menubar)
        self.usagespace.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.usagespace.setToolTipsVisible(True)
        self.usagespace.setObjectName("usagespace")
        self.usagespace_action = QAction(self.mainwindow)
        self.usagespace_action.setCheckable(False)
        self.usagespace_action.setObjectName('usageSpaceAction')
        self.usagespace_action.triggered.connect(self.spaceUsage)
        self.usagespace_action.setText('占用空间')

        self.settings = QtWidgets.QMenu(self.menubar)
        self.settings.setToolTipsVisible(True)
        self.settings.setObjectName("settings")
        self.settings_action = QAction(self.mainwindow)
        self.settings_action.setCheckable(False)
        self.settings_action.setObjectName('settingAction')
        self.settings_action.triggered.connect(self.showEnvWindow)
        self.settings_action.setText('存储设置')

        self.about = QtWidgets.QMenu(self.menubar)
        self.about.setToolTipsVisible(True)
        self.about.setObjectName("about")
        self.about_action = QAction(self.mainwindow)
        self.about_action.setCheckable(False)
        self.about_action.setObjectName('aboutAction')
        self.about_action.triggered.connect(self.showAboutWindow)
        self.about_action.setText('关于')

        self.menubar.addAction(self.localfile_action)
        self.menubar.addAction(self.usagespace_action)
        self.menubar.addAction(self.settings_action)
        self.menubar.addAction(self.about_action)

        MainWindow.setMenuBar(self.menubar)

        '''工具栏部分'''
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setContentsMargins(QMargins(20, 0, 20, 0))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        choose = QAction(QIcon('../images/choose.png'), 'choose', self.mainwindow)
        self.toolBar.addAction(choose)
        delete = QAction(QIcon('../images/delete.png'), 'delete', self.mainwindow)
        self.toolBar.addAction(delete)
        search_edit = QLineEdit()
        search_edit.setMaximumWidth(200)
        search_edit.setPlaceholderText('输入搜索内容')
        self.toolBar.addWidget(search_edit)
        search = QAction(QIcon('../images/search.png'), 'search', self.mainwindow)
        self.toolBar.addAction(search)

        '''可调节伸缩区域'''
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        '''左侧'''
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_2.sizePolicy().hasHeightForWidth())
        self.treeWidget_2.setSizePolicy(sizePolicy)
        self.treeWidget_2.setMinimumSize(QtCore.QSize(300, 0))
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.treeWidget_2.setHeaderLabels(['文件名','文件路径'])
        # self.treeWidget_2.setHeaderHidden(True)
        # self.treeWidget_2.setColumnHidden(1,True)
        self.root = QTreeWidgetItem(self.treeWidget_2)
        # self.json_settings['FILE_LOCATION'] = self.json_settings['FILE_LOCATION'].replace('\\', '/')
        self.root.setText(0, self.json_settings['FILE_LOCATION'].split('/')[-1])
        self.root.setText(1, self.json_settings['FILE_LOCATION'])
        self.root.setIcon(0, QIcon('../images/folder.png'))

        self.file_thread = FileListThread(self.root, self.json_settings['FILE_LOCATION'])
        self.file_thread.start()
        self.file_thread.sinOut.connect(self.getTreeRoot)

        '''右侧文件管理'''
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableView = QtWidgets.QTableView(self.tab_3)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 651, 741))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab_3, "文件管理")

        '''右侧文件预览'''
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(160, 90, 351, 361))
        self.label.setToolTipDuration(0)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_4, "文件预览")
        self.browser = QWebEngineView(self.tab_4)
        self.browser.setMinimumSize(QSize(200, 400))
        self.preview_path = 'D:/graduation-project/allfile/UI_HTML/welcome.html'
        self.browser.load(QUrl(self.preview_path))
        self.horizontalLayout.addWidget(self.splitter)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        '''状态栏部分'''
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "文件管理"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "文件预览"))



    def menubar_triggered(self,q):
        print(q.text)

    def openLocalFile(self):
        '''
        菜单栏打开本地文件方法
        :return:
        '''
        local_path = self.json_settings['FILE_LOCATION']
        if '/' in local_path:
            local_path = local_path.replace('/', '\\')
        os.system("explorer.exe %s" % os.path.dirname(local_path))

    def spaceUsage(self):
        '''
        菜单栏占用空间方法
        :return:
        '''
        local_path = self.json_settings['FILE_LOCATION']
        if '/' in local_path:
            local_path = local_path.replace('/', '\\')
        file_size = os.path.getsize(local_path)
        file_size = self.approximateSize(file_size)
        QMessageBox.about(self.mainwindow, '占用空间', local_path + '：' + file_size)

    def showEnvWindow(self):
        self.env_dialog = EnvDialog(self.json_settings)
        self.env_dialog.confirm.clicked.connect(self.updateSettings)
        self.env_dialog.exec_()

    def updateSettings(self):
        '''
        更改环境后，重新修改软件设置
        重新写入配置文件
        :return:
        '''
        self.json_settings = self.env_dialog.get_env_settings()
        f = open('settings.json', 'w')
        json.dump(self.json_settings, f)
        self.env_dialog.close()
        # self.updateFileTree()

    def showAboutWindow(self):
        '''
        打开关于窗口方法
        :return: None
        '''
        dialog = AboutDialog()
        if dialog.exec_() == QDialog.Accepted:
            pass

    '''文件存储空间单位转换方法'''

    def approximateSize(self, size, a_kilobyte_is_1024_bytes=True):
        '''Convert a file size to human-readable form.

        Keyword arguments:
        size -- file size in bytes
        a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                    if False, use multiples of 1000

        Returns: string

        '''
        SUFFIXES = {1024: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
                    1000: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

        if size < 0:
            raise ValueError('number must be non-negative')
        multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
        for suffix in SUFFIXES[multiple]:
            size /= multiple
            if size < multiple:
                return '{0:.1f} {1}'.format(size, suffix)

    '''获取文件加载子线程返回的root节点'''

    def getTreeRoot(self, root):
        '''
        文件树添加item方法
        :param root:
        :return: None
        '''
        self.file_thread.wait()
        self.treeWidget_2.addTopLevelItem(root)
        self.treeWidget_2.doubleClicked.connect(self.fileItemDoubleClick)
        self.treeWidget_2.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.treeWidget_2.customContextMenuRequested.connect(self.fileTreeCustomRightMenu)

    def fileItemDoubleClick(self):
        item = self.treeWidget_2.currentItem()
        file_path = item.text(1)
        # file_path = file_path.replace('\\', '/')
        print(file_path)
        if os.path.isdir(file_path):
            pass
        else:
            if file_path.endswith('.html'):
                pass
            elif file_path.endswith('.jpg'):
                pass
            elif file_path.endswith('txt'):
                pass
            elif file_path.endswith('xlsx'):
                pass
            else:
                pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())