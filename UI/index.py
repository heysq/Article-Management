# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import json
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from UI.PyQt_Thread import FileListThread, FilePasteThread
from UI.about import AboutDialog
from UI.env_dialog import EnvDialog


class Ui_MainWindow(object):
    def __init__(self, mainwindow):
        '''
        主页面初始化方法
        :param parent:
        '''
        super().__init__()
        f_settings = open('settings.json', 'r')
        self.settings = json.load(f_settings)
        self.mainwindow = mainwindow

    def setupUi(self, MainWindow):
        '''
        主页面desinger布局
        :param MainWindow:
        :return:
        '''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QWidget(MainWindow)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")

        '''
        分割器生成部分

        '''
        self.splitter = QSplitter(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        '''
        右侧文件树生成部分
        '''
        self.file_tree = QTreeWidget(self.splitter)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_tree.sizePolicy().hasHeightForWidth())
        self.file_tree.setSizePolicy(sizePolicy)
        self.file_tree.setMinimumSize(QSize(300, 0))
        self.file_tree.setObjectName("file_tree")
        self.file_tree.setHeaderLabels(['文件名', '文件路径'])
        self.file_tree.setHeaderHidden(True)
        self.file_tree.setColumnHidden(1, True)
        self.file_tree.setSortingEnabled(True)
        self.file_tree.setFont(QFont("Roman times",12,QFont.Light))

        # 文件树第一个节点
        self.root = QTreeWidgetItem(self.file_tree)
        self.root.setText(0, self.settings['FILE_LOCATION'].split('\\')[-1])
        self.root.setText(1, self.settings['FILE_LOCATION'])
        self.root.setIcon(0, QIcon('UI/images/folder.png'))
        # 启用文件树构造线程
        self.file_thread = FileListThread(self.root, self.settings['FILE_LOCATION'])
        self.file_thread.start()
        self.file_thread.sinOut.connect(self.get_tree_root)

        '''
        左侧文件管理区生成部分
        '''
        self.table_view = QTableView(self.splitter)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_view.sizePolicy().hasHeightForWidth())

        self.table_view.setSizePolicy(sizePolicy)
        self.table_view.setObjectName("table_view")
        self.horizontalLayout.addWidget(self.splitter)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        '''
        软件菜单栏生成部分
        '''
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 986, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        file = self.menubar.addMenu('文件')
        local_file = QAction('本地文件', self.mainwindow)
        local_file.setShortcut('Ctrl+E')
        file.addAction(local_file)
        used_space = QAction('占用空间', self.mainwindow)
        file.addAction(used_space)
        help = self.menubar.addMenu('帮助')
        about = QAction('关于', self.mainwindow)
        help.addAction(about)
        env_set = QAction('环境设置', self.mainwindow)
        help.addAction(env_set)

        about.triggered.connect(self.show_about_window)
        env_set.triggered.connect(self.show_env_window)
        local_file.triggered.connect(self.open_local_file)
        used_space.triggered.connect(self.space_usage)

        '''
        工具栏部分
        '''
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        choose = QAction(QIcon('UI/images/choose.png'), 'choose', self.mainwindow)
        self.toolBar.addAction(choose)
        delete = QAction(QIcon('UI/images/delete.png'), 'delete', self.mainwindow)
        self.toolBar.addAction(delete)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "网络文章下载与本地存储系统"))

    def get_tree_root(self, root):
        '''
        文件树添加item方法
        :param root:
        :return: None
        '''
        self.file_thread.wait()
        self.file_tree.addTopLevelItem(root)
        self.file_tree.doubleClicked.connect(self.file_item_double_clicked)
        self.file_tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.file_tree.customContextMenuRequested.connect(self.file_tree_custom_right_menu)

    def file_tree_custom_right_menu(self, pos):
        item = self.file_tree.currentItem()
        file_path = item.text(1)
        menu = QMenu(self.file_tree)
        delete = menu.addAction('删除')
        copy = menu.addAction('复制')
        paste = menu.addAction('粘贴')
        open_local_file = menu.addAction('浏览本地文件')
        action = menu.exec_(self.file_tree.mapToGlobal(pos))
        if action == delete:
            reply = QMessageBox.warning(self.mainwindow, '删除确认', '确认删除吗？', QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.No)
            if os.path.isdir(file_path) and reply == 16384:
                print('delete dir')
                # os.removedirs(file_path)
            elif not os.path.isdir(file_path) and reply == 16384:
                print('delete file')
                # os.remove(file_path)
                self.update_file_tree()

        elif action == copy:
            try:
                data = QMimeData()
                url = QUrl.fromLocalFile(file_path)
                clipboard = QApplication.clipboard()
                data.setUrls([url])
                clipboard.setMimeData(data)
            except Exception as e:
                QMessageBox.about(self.mainwindow, '错误', '文件不存在')
        elif action == paste:
            data = QApplication.clipboard().mimeData()
            source_file_url = data.urls()[0].url()
            self.paste_thread = FilePasteThread(source_file_url[8:], file_path)
            self.paste_thread.sinOut.connect(self.file_paste_complete)
            self.paste_thread.start()

        elif action == open_local_file:

            if '/' in file_path:
                local_path = file_path.replace('/', '\\')
            os.system("explorer.exe %s" % os.path.dirname(file_path))
        else:
            QMessageBox.warning(self.mainwindow, '错误', '打开文件不存在')

    def file_paste_complete(self, msg):
        '''
        文件粘贴成功回调函数
        成功后刷新重构文件树
        :param msg:
        :return: None
        '''
        self.paste_thread.wait()
        self.update_file_tree()

    def update_file_tree(self):
        self.file_tree.clear()
        self.root = QTreeWidgetItem(self.file_tree)
        self.root.setText(0, self.settings['FILE_LOCATION'].split('\\')[-1])
        self.root.setText(1, self.settings['FILE_LOCATION'])
        self.root.setIcon(0, QIcon('UI/images/folder.png'))
        self.file_thread = FileListThread(self.root, self.settings['FILE_LOCATION'])
        self.file_thread.start()
        self.file_thread.sinOut.connect(self.get_tree_root)

    def file_item_double_clicked(self):
        item = self.file_tree.currentItem()
        file_path = item.text(1)
        if os.path.isdir(file_path):
            pass
        else:
            pass

    def add_menubar(self):
        '''
        添加菜单栏
        :return: None
        '''
        munu_bar = self.menubar()
        file = munu_bar.addMenu('文件')
        local_file = QAction('本地文件', self)
        local_file.setShortcut('Ctrl+E')
        file.addAction(local_file)
        used_space = QAction('占用空间', self)
        file.addAction(used_space)
        help = munu_bar.addMenu('帮助')
        about = QAction('关于', self)
        help.addAction(about)
        env_set = QAction('环境设置', self)
        help.addAction(env_set)

        about.triggered.connect(self.show_about_window)
        env_set.triggered.connect(self.show_env_window)

    def show_about_window(self):
        '''
        打开关于窗口方法
        :return: None
        '''
        dialog = AboutDialog()
        if dialog.exec_() == QDialog.Accepted:
            pass

    def show_env_window(self):
        '''
        打开环境设置窗口
        :return: None
        '''
        self.env_dialog = EnvDialog(self.settings)
        self.env_dialog.confirm.clicked.connect(self.update_settings)
        self.env_dialog.exec_()

    def update_settings(self):
        '''
        更改环境后，重新修改软件设置
        重新写入配置文件
        :return:
        '''
        self.settings = self.env_dialog.get_env_settings()
        f = open('settings.json', 'w')
        json.dump(self.settings, f)
        self.env_dialog.close()
        self.update_file_tree()

    def open_local_file(self):
        '''
        菜单栏打开本地文件方法
        :return:
        '''
        local_path = self.settings['FILE_LOCATION']
        if '/' in local_path:
            local_path = local_path.replace('/','\\')
        os.system("explorer.exe %s" % os.path.dirname(local_path))


    def space_usage(self):
        local_path = self.settings['FILE_LOCATION']
        if '/' in local_path:
            local_path = local_path.replace('/', '\\')
        file_size = os.path.getsize(local_path)
        print(file_size)
        if file_size <= 1024:
            file_size = str(round(file_size,2)) + "K"
        elif file_size > 1024 and file_size <= 1048576:
            file_size = str(round(file_size/1024,2)) + 'M'
        else:
            file_size = str(round(file_size/(1024*1024),2)) + 'G'

        QMessageBox.about(self.mainwindow,'占用空间',local_path+'：'+file_size)








