# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import json
import os
import sys
import filetype
import time
import shutil

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

from PyQt_Thread import FileListThread, FilePasteThread
from about import AboutDialog
from env_dialog import EnvDialog


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
        f_settings.close()

    '''软件主界面UI设置方法'''

    def setupUi(self, MainWindow):
        '''
        主页面desinger布局
        :param MainWindow:
        :return:
        '''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 900)
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
        self.file_tree.setFont(QFont("Roman times", 12, QFont.Light))

        # 文件树第一个节点
        self.root = QTreeWidgetItem(self.file_tree)
        self.settings['FILE_LOCATION'] = self.settings['FILE_LOCATION'].replace('\\', '/')
        self.root.setText(0, self.settings['FILE_LOCATION'].split('/')[-1])
        self.root.setText(1, self.settings['FILE_LOCATION'])
        self.root.setIcon(0, QIcon('UI/images/folder.png'))
        # 启用文件树构造线程
        self.file_thread = FileListThread(self.root, self.settings['FILE_LOCATION'])
        self.file_thread.start()
        self.file_thread.sinOut.connect(self.getTreeRoot)

        self.tabWidget = QTabWidget(self.splitter)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")

        '''文件管理'''
        self.managet_tab = QWidget()
        self.managet_tab.setObjectName("managet_tab")
        self.verticalLayout = QVBoxLayout(self.managet_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QTableView(self.managet_tab)
        self.tableView.setMinimumSize(QSize(0, 299))
        self.tableView.setLineWidth(10)
        self.tableView.setShowGrid(True)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.managet_tab.setContentsMargins(10, 10, 10, 10)
        self.tabWidget.addTab(self.managet_tab, "文件管理")

        '''文件属性'''
        self.property_tab = QWidget()
        self.property_tab.setObjectName("property_tab")
        self.label = QLabel(self.property_tab)
        self.label.setGeometry(QRect(160, 90, 351, 361))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.property_tab, "文件属性")

        '''文件预览'''
        self.preview_tab = QWidget()
        self.preview_tab.setObjectName('preview_tab')
        self.tab_layout = QVBoxLayout(self.preview_tab)
        self.browser = QWebEngineView(self.preview_tab)
        self.browser.setMinimumSize(QSize(200, 400))
        welcome_html = 'D:/graduation-project/UI/welcome.html'
        self.browser.load(QUrl(welcome_html))
        self.tab_layout.addWidget(self.browser)
        self.tabWidget.addTab(self.preview_tab, '文件预览')

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

        about.triggered.connect(self.showAboutWindow)
        env_set.triggered.connect(self.showEnvWindow)
        local_file.triggered.connect(self.openLocalFile)
        used_space.triggered.connect(self.spaceUsage)

        '''
        工具栏部分
        '''
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setContentsMargins(QMargins(20, 0, 20, 0))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        choose = QAction(QIcon('images/choose.png'), 'choose', self.mainwindow)
        self.toolBar.addAction(choose)
        delete = QAction(QIcon('images/delete.png'), 'delete', self.mainwindow)
        self.toolBar.addAction(delete)
        search_edit = QLineEdit()
        search_edit.setMaximumWidth(200)
        search_edit.setPlaceholderText('输入搜索内容')
        self.toolBar.addWidget(search_edit)
        search = QAction(QIcon('images/search.png'), 'search', self.mainwindow)
        self.toolBar.addAction(search)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    '''软件UI转换方法'''

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "网络文章下载与本地存储系统"))

    '''获取文件加载子线程返回的root节点'''

    def getTreeRoot(self, root):
        '''
        文件树添加item方法
        :param root:
        :return: None
        '''
        self.file_thread.wait()
        self.file_tree.addTopLevelItem(root)
        self.file_tree.doubleClicked.connect(self.fileItemDoubleClick)
        self.file_tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.file_tree.customContextMenuRequested.connect(self.fileTreeCustomRightMenu)

    '''文件树右键菜单'''

    def fileTreeCustomRightMenu(self, pos):
        item = self.file_tree.currentItem()
        file_path = item.text(1)
        menu = QMenu(self.file_tree)
        delete = menu.addAction('删除')
        copy = menu.addAction('复制')
        paste = menu.addAction('粘贴')
        openLocalFile = menu.addAction('浏览本地文件')
        action = menu.exec_(self.file_tree.mapToGlobal(pos))
        if action == delete:
            reply = QMessageBox.warning(self.mainwindow, '删除确认', '确认删除吗？', QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.No)
            if os.path.isdir(file_path) and reply == 16384:
                print('delete dir')
                # os.removedirs(file_path)
                shutil.rmtree(file_path)
            elif not os.path.isdir(file_path) and reply == 16384:
                print('delete file')
                # os.remove(file_path)
                self.updateFileTree()

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
            self.paste_thread.sinOut.connect(self.filePasteComplete)
            self.paste_thread.start()

        elif action == openLocalFile:
            if '/' in file_path:
                local_path = file_path.replace('/', '\\')
            os.system("explorer.exe %s" % os.path.dirname(local_path))
        else:
            QMessageBox.warning(self.mainwindow, '错误', '打开文件不存在')

    '''文件粘贴完毕后执行方法'''

    def filePasteComplete(self, msg):
        '''
        文件粘贴成功回调函数
        成功后刷新重构文件树
        :param msg:
        :return: None
        '''
        self.paste_thread.wait()
        self.updateFileTree()

    '''更新文件树方法'''

    def updateFileTree(self):
        self.file_tree.clear()
        self.root = QTreeWidgetItem(self.file_tree)
        self.root.setText(0, self.settings['FILE_LOCATION'].split('\\')[-1])
        self.root.setText(1, self.settings['FILE_LOCATION'])
        self.root.setIcon(0, QIcon('UI/images/folder.png'))
        self.file_thread = FileListThread(self.root, self.settings['FILE_LOCATION'])
        self.file_thread.start()
        self.file_thread.sinOut.connect(self.getTreeRoot)

    '''文件树item双击处理方法'''

    def fileItemDoubleClick(self):
        item = self.file_tree.currentItem()
        file_path = item.text(1)
        file_path = file_path.replace('\\', '/')
        print(file_path)
        if os.path.isdir(file_path):
            self.addTableItem(file_path)
        elif file_path.endswith('.html'):
            self.managet_tab.setVisible(False)
            self.browser.load(QUrl(file_path))

    '''添加菜单栏方法'''

    def addMenubar(self):
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

        about.triggered.connect(self.showAboutWindow)
        env_set.triggered.connect(self.showEnvWindow)

    '''展示关于窗口方法'''

    def showAboutWindow(self):
        '''
        打开关于窗口方法
        :return: None
        '''
        dialog = AboutDialog()
        if dialog.exec_() == QDialog.Accepted:
            pass

    '''展示环境设置窗口方法'''

    def showEnvWindow(self):
        '''
        打开环境设置窗口
        :return: None
        '''
        self.env_dialog = EnvDialog(self.settings)
        self.env_dialog.confirm.clicked.connect(self.updateSettings)
        self.env_dialog.exec_()

    '''更新软件配置文件方法'''

    def updateSettings(self):
        '''
        更改环境后，重新修改软件设置
        重新写入配置文件
        :return:
        '''
        self.settings = self.env_dialog.get_env_settings()
        f = open('settings.json', 'w')
        json.dump(self.settings, f)
        self.env_dialog.close()
        self.updateFileTree()

    '''打开本地文件方法'''

    def openLocalFile(self):
        '''
        菜单栏打开本地文件方法
        :return:
        '''
        local_path = self.settings['FILE_LOCATION']
        if '/' in local_path:
            local_path = local_path.replace('/', '\\')
        os.system("explorer.exe %s" % os.path.dirname(local_path))

    '''统计使用空间方法'''

    def spaceUsage(self):
        local_path = self.settings['FILE_LOCATION']
        if '/' in local_path:
            local_path = local_path.replace('/', '\\')
        file_size = os.path.getsize(local_path)
        file_size = self.approximateSize(file_size)
        QMessageBox.about(self.mainwindow, '占用空间', local_path + '：' + file_size)

    '''页面tableview添加item方法'''

    def addTableItem(self, file_path):
        '''
        针对文件夹进行访问，然后添加到文件管理页面
        :param file_path: 文件夹路径
        :return: None
        '''
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['状态', '文件名', '文件大小', '文件类型', '创建时间'])

        '''添加列表选项部分'''
        file_list = os.listdir(file_path)
        for index in range(len(file_list)):
            child_path = os.path.join(file_path, file_list[index])
            child_stat = os.stat(child_path)
            child_ctime = child_stat.st_ctime
            '''文件创建时间'''
            child_ctime = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(child_ctime))
            if os.path.isdir(child_path):
                child_type = 'folder'
                child_size = self.getDirSize(child_path)
            else:
                kind = filetype.guess(child_path)
                if kind is None:
                    child_type = 'other'
                else:
                    child_type = kind.extension
                child_size = os.path.getsize(child_path)

            '''child_size 单位换算'''
            child_size = self.approximateSize(child_size)

            '''列表项复选框部分'''
            item_checked = QStandardItem()
            item_checked.setCheckState(Qt.Unchecked)  # 设置默认显示复选框的状态
            item_checked.setCheckable(True)  # 设置复选框是否可以点点击
            child_column = [item_checked, file_list[index], child_size, child_type, child_ctime]  # 每一行记录的数据列表

            '''循环添加列表项'''
            for column_index in range(5):
                item = QStandardItem(child_column[column_index])
                item.setTextAlignment(Qt.AlignCenter)
                self.model.setItem(index, column_index, item)
        self.model.itemChanged.connect(self.modelChanged)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 表格不可编辑
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.tableView.setColumnWidth(0, 80)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setShowGrid(False)

    '''统一获取文件夹大小方法'''

    def getDirSize(slef, dir):
        size = 0
        for root, dirs, files in os.walk(dir):
            size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
        return size

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

    def tableViewItemSelect(self):
        indexs = self.tableView.selectionModel().selection().indexes()
        print(indexs)

    def modelChanged(self):
        pass
        # self.selected_indexs = self.tableView.selectionMode().selection().indexes()
        # print(self.selected_indexs)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
