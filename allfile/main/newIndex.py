# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import json
import os
import shutil
import sys
import time
import QSS
from os.path import getsize, join

from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import QMargins, Qt, QSize, QUrl, QMimeData
from PyQt5.QtGui import QIcon, QPixmap, QColor

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QAction, QDialog, QToolBar, QLineEdit, \
    QTreeWidgetItem, QVBoxLayout, QMenu, QPushButton, QDoubleSpinBox, \
    QHeaderView, QTableWidget, QTableWidgetItem, QAbstractItemView, QFrame

from env_dialog import EnvDialog
from about import AboutDialog
from index_thread import FileListThread, FilePasteThread
from file_status import FileStatusWindow
from MyBrowser import Browser



class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        setting_file = open('../settings/settings.json', 'r')
        self.json_settings = json.load(setting_file)
        setting_file.close()

    def setupUi(self, MainWindow):
        self.mainwindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
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
        self.menubar.setStyleSheet(QSS.QMenuBar)
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
        delete_button = QPushButton()
        delete_button.setText('删除')
        delete_icon = QIcon()
        delete_icon.addPixmap(QPixmap('../images/delete.png'), QIcon.Normal, QIcon.Off)
        delete_button.setIcon(delete_icon)
        delete_button.setIconSize(QSize(25, 25))
        delete_button.setStyleSheet(QSS.ButtonStyle)

        self.search_edit = QLineEdit()
        self.search_edit.setMaximumWidth(200)
        self.search_edit.setFixedHeight(30)
        self.search_edit.setPlaceholderText('输入搜索内容')
        self.search_edit.setStyleSheet(QSS.LineEdit)
        self.toolBar.addWidget(self.search_edit)

        search_button = QPushButton()
        search_button.setText('搜索')
        search_icon = QIcon()
        search_icon.addPixmap(QPixmap('../images/search.png'), QIcon.Normal, QIcon.Off)
        search_button.setIcon(search_icon)
        search_button.setIconSize(QSize(25, 25))
        search_button.setStyleSheet(QSS.ButtonStyle)
        search_button.clicked.connect(self._search)

        '''放大按钮'''
        self.zoom_in_button = QPushButton(self.mainwindow)
        self.zoom_in_button.setText('放大')
        zoom_in_icon = QIcon()
        zoom_in_icon.addPixmap(QPixmap('../images/zoom_in.png'), QIcon.Normal, QIcon.Off)
        self.zoom_in_button.setIcon(zoom_in_icon)
        self.zoom_in_button.setIconSize(QSize(25, 25))
        self.zoom_in_button.setStyleSheet(QSS.ButtonStyle)

        self.sp = QDoubleSpinBox(self.mainwindow)
        self.sp.setRange(1,4.95)
        self.sp.setValue(1.2)
        self.sp.setSingleStep(0.1)
        self.sp.setMinimum(1)
        self.sp.setMinimumHeight(35)
        self.sp.setMinimumWidth(60)
        self.sp.valueChanged.connect(self.sp_value_change)


        '''缩小按钮'''
        self.zoom_out_button = QPushButton(self.mainwindow)
        self.zoom_out_button.setText('缩小')
        zoom_out_icon = QIcon()
        zoom_out_icon.addPixmap(QPixmap('../images/zoom_out.png'), QIcon.Normal, QIcon.Off)
        self.zoom_out_button.setIcon(zoom_out_icon)
        self.zoom_out_button.setIconSize(QSize(25, 25))
        self.zoom_out_button.setStyleSheet(QSS.ButtonStyle)

        '''弹出页面url按钮'''
        url_button = QPushButton()
        url_button.setText('URL')
        url_icon = QIcon()
        url_icon.addPixmap(QPixmap('../images/url.png'), QIcon.Normal, QIcon.Off)
        url_button.setIcon(url_icon)
        url_button.setIconSize(QSize(25, 25))
        url_button.setStyleSheet(QSS.ButtonStyle)

        self.toolBar.addWidget(search_button)
        self.toolBar.addWidget(delete_button)
        self.toolBar.addWidget(self.zoom_in_button)
        self.toolBar.addWidget(self.sp)
        self.toolBar.addWidget(self.zoom_out_button)
        self.toolBar.addWidget(url_button)

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
        self.treeWidget_2.setStyleSheet(QSS.QTreeView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_2.sizePolicy().hasHeightForWidth())
        self.treeWidget_2.setSizePolicy(sizePolicy)
        self.treeWidget_2.setMinimumSize(QtCore.QSize(300, 0))
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.treeWidget_2.setHeaderLabels(['文件名', '文件路径'])
        self.treeWidget_2.setHeaderHidden(True)
        self.treeWidget_2.setColumnHidden(1, True)
        self.root = QTreeWidgetItem(self.treeWidget_2)
        self.json_settings['FILE_LOCATION'] = self.json_settings['FILE_LOCATION'].replace('\\', '/')
        self.root.setText(0, self.json_settings['FILE_LOCATION'].split('/')[-1])
        self.root.setText(1, self.json_settings['FILE_LOCATION'])
        self.root.setIcon(0, QIcon('../images/folder.png'))

        self.file_thread = FileListThread(self.root, self.json_settings['FILE_LOCATION'])
        self.file_thread.start()
        self.file_thread.sinOut.connect(self.getTreeRoot)

        '''右侧文件管理'''
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setStyleSheet(QSS.QTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.table_widget = self.get_file_list(self.json_settings['FILE_LOCATION'])
        self.paths = [self.json_settings['FILE_LOCATION'],]
        self.tab3_layout = QVBoxLayout(self.tab_3)
        self.tab3_layout.addWidget(self.tablewidget)
        self.tabWidget.addTab(self.tab_3, "文件管理")

        '''右侧文件预览'''
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "文件预览")
        self.browser = Browser(self.tab_4)
        self.zoom_in_button.clicked.connect(self.zoom_in_func)  # 放大与缩小按钮出发事件设置
        self.zoom_out_button.clicked.connect(self.zoom_out_func)
        self.sp.setValue(self.browser.zoomFactor())
        self.tab_layout = QVBoxLayout(self.tab_4)
        self.browser.setMinimumSize(QSize(400, 200))
        self.tab_layout.addWidget(self.browser)
        self.browser.load(QUrl('D:/graduation-project/allfile/UI_HTML/welcome.html'))
        self.tabWidget.setCurrentIndex(1)

        self.horizontalLayout.addWidget(self.splitter)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        '''状态栏部分'''
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        self.statusBar.showMessage('程序就绪！',msecs=5000)
        self.statusBar.setStyleSheet(QSS.QStatusBar)
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

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
        self.statusBar.showMessage('设置更新完毕')
        self.updateFileTree()

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


    '''搜索按钮点击事件函数'''
    def _search(self):
        print(self.search_edit.text())
        self.search_name = self.search_edit.text()
        self.search_res = []
        self.recursion_search(self.search_name,self.json_settings['FILE_LOCATION'],self.search_res)


    def recursion_search(self,search_name,search_path,res=[]):
        for filename in os.listdir(search_path):
            temp_path = os.path.join(search_path,filename)
            if os.path.isdir(temp_path):
                if search_name in filename:
                    res.append(temp_path)
                else:
                    self.recursion_search(search_name,temp_path,res)
            else:
                if search_name in filename:
                    res.append(temp_path)
                else:
                    return res



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
        self.treeWidget_2.customContextMenuRequested.connect(self.fileTreeCustomRightMenu)

    def fileItemDoubleClick(self):
        item = self.treeWidget_2.currentItem()
        file_path = item.text(1)
        # file_path = file_path.replace('\\', '/')
        print(file_path)
        if os.path.isdir(file_path):
            self.paths.append(file_path)
            self.tab3_layout.removeWidget(self.tablewidget)
            self.tablewidget = self.get_file_list(file_path)
            self.tab3_layout.addWidget(self.tablewidget)
            self.tablewidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.tablewidget.customContextMenuRequested['QPoint'].connect(self.tablewidget_right_menu)
            self.tabWidget.setCurrentIndex(0)
        else:
            if file_path.endswith('.html') or file_path.endswith('.jpg') or file_path.endswith('.png'):
                file_url = file_path.replace('\\', '/')
                self.browser.stop()
                self.browser.destroy()
                self.browser.close()
                del self.browser
                self.browser = Browser()
                self.tab_layout.addWidget(self.browser)
                self.browser.load(QUrl('file:///' + file_url))
                self.zoom_in_button.clicked.connect(self.zoom_in_func)  # 放大与缩小按钮出发事件设置
                self.zoom_out_button.clicked.connect(self.zoom_out_func)
                self.sp.setValue(self.browser.zoomFactor())
                filename = file_url.split('/')[-1]
                self.tabWidget.setCurrentIndex(1)
                self.statusBar.showMessage(f'预览文件 -> {filename} , 请等候...')
                self.browser.loadFinished.connect(self.browser_finished)
            else:
                reply = QMessageBox.information(self.mainwindow,
                                                "调用系统软件",
                                                "软件不支持此类型文件打开！\n是否调用系统程序打开此文件?",
                                                QMessageBox.Yes | QMessageBox.No)
                if reply == 16384:
                    os.startfile(file_path)

    '''文件树右键菜单'''

    def fileTreeCustomRightMenu(self, pos):
        item = self.treeWidget_2.currentItem()
        file_path = item.text(1)
        menu = QMenu(self.treeWidget_2)
        delete = menu.addAction('删除')
        copy = menu.addAction('复制')
        paste = menu.addAction('粘贴')
        openLocalFile = menu.addAction('浏览本地文件')
        file_roperty = menu.addAction("属性")
        action = menu.exec_(self.treeWidget_2.mapToGlobal(pos))
        if action == delete:
            reply = QMessageBox.warning(self.mainwindow, '删除确认', '确认删除吗？', QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.No)
            if os.path.isdir(file_path) and reply == 16384:
                print('delete dir')
                shutil.rmtree(file_path)
                self.statusBar.showMessage(f'删除 {file_path} 成功！')
                if file_path == self.paths[-1]:
                    # 删除的是当前文件管理显示的文件夹 需要推倒上一级
                    current_path = self.paths.pop()
                    self.paths.append(os.path.dirname(current_path))
                self.updateFileTree()
            elif not os.path.isdir(file_path) and reply == 16384:
                print('delete file')
                os.remove(file_path)
                self.statusBar.showMessage("删除 -> %s 成功!" % file_path)
                self.updateFileTree()
                self.statusBar.showMessage(f'删除 {file_path} 成功!')

        elif action == copy:
            try:
                data = QMimeData()
                url = QUrl.fromLocalFile(file_path)
                clipboard = QApplication.clipboard()
                data.setUrls([url])
                clipboard.setMimeData(data)
                self.statusBar.showMessage("已复制 -> %s 到剪切板" % file_path)
            except Exception as e:
                QMessageBox.about(self.mainwindow, '错误', '文件不存在!')
                self.statusBar.showMessage("复制 -> %s  出错，文件不存在!" % file_path)

        elif action == paste:
            data = QApplication.clipboard().mimeData()
            source_file_url = data.urls()[0].url()
            self.paste_thread = FilePasteThread(source_file_url[8:], file_path)
            self.paste_thread.sinOut.connect(self.filePasteComplete)
            self.paste_thread.start()


        elif action == openLocalFile:
            try:
                local_path = file_path.replace('/', '\\')
                os.system("explorer.exe %s" % os.path.dirname(local_path))
            except Exception as e:
                QMessageBox.warning(self.mainwindow, '错误', '打开文件不存在!')

        elif action == file_roperty:
            # print('查看文件属性')
            if os.path.isdir(file_path):
                file_type = '文件夹'
                file_image = '../images/folder_status.png'
                _dir = True
            else:
                _dir = False
                if file_path.endswith('.jpg'):
                    file_type = 'JPG图片文件( *.jpg )'
                    file_image = '../images/jpg_status.png'
                elif file_path.endswith('.html'):
                    file_type = 'HTML页面文件( *.html )'
                    file_image = '../images/html_status.png'
                elif file_path.endswith('.xlsx'):
                    file_type = 'XLSX表格文件( *.xlsx )'
                    file_image = '../images/excel_status.png'
                elif file_path.endswith('.png'):
                    file_type = 'XLSX表格文件( *.xlsx )'
                    file_image = '../images/png_status.png'
                else:
                    file_type = 'Other其他文件类型( *.%s)' % (os.path.splitext(file_path)[1])
                    file_image = '../images/file_status.png'
            if _dir:
                '''文件夹大小去要遍历每个子文件夹与文件累加'''
                file_size = self.getdirsize(file_path)
                # print(file_path)
                statinfo = os.stat(file_path)
            else:
                statinfo = os.stat(file_path)
                file_size = statinfo.st_size
            file_atime = self.time_format(statinfo.st_atime)  # 文件最后访问时间
            file_ctime = self.time_format(statinfo.st_ctime)  # 文件创建时间
            file_mtime = self.time_format(statinfo.st_mtime)  # 文件最后修改时间
            self.file_status_window = FileStatusWindow()
            self.file_status_window.filename = file_path.replace('\\', '/').split('/')[-1]
            self.status_main_window = QMainWindow(MainWindow)
            self.file_status_window.setupUi(self.status_main_window)
            self.file_status_window.lineEdit.setText(self.file_status_window.filename)
            self.file_status_window.label_3.setText(file_type)
            self.file_status_window.label_5.setText(file_path.replace('/', '\\'))
            self.file_status_window.label_9.setText(file_ctime)
            self.file_status_window.label_11.setText(file_mtime)
            self.file_status_window.label_13.setText(file_atime)
            self.file_status_window.label_7.setText(self.approximateSize(file_size))
            self.file_status_window.pushButton.clicked.connect(self.fileStatusUse)  # 应用按钮click出发函数
            self.file_status_window.pushButton_2.clicked.connect(self.fileStatusConfirm)
            self.file_status_window.pushButton_3.clicked.connect(self.fileStatusCancel)
            pix = QPixmap(file_image)
            self.file_status_window.label.setPixmap(pix)
            self.status_main_window.show()

    '''文件粘贴完毕后执行方法'''

    def filePasteComplete(self, msg):
        '''
        文件粘贴成功回调函数
        成功后刷新重构文件树
        :param msg:
        :return: None
        '''
        self.paste_thread.wait()
        self.statusBar.showMessage("粘贴文件 -> %s 成功!" % msg)
        self.updateFileTree()

    '''更新文件树方法'''

    def updateFileTree(self):
        self.treeWidget_2.clear()
        self.root = QTreeWidgetItem(self.treeWidget_2)
        self.root.setText(0, self.json_settings['FILE_LOCATION'].split('\\')[-1])
        self.root.setText(1, self.json_settings['FILE_LOCATION'])
        self.root.setIcon(0, QIcon('../images/folder.png'))

        self.tab3_layout.removeWidget(self.tablewidget)
        del self.tablewidget
        self.tablewidget = self.get_file_list(self.paths[-1])
        self.tab3_layout.addWidget(self.tablewidget)

        self.file_thread = FileListThread(self.root, self.json_settings['FILE_LOCATION'])
        self.file_thread.start()
        self.file_thread.sinOut.connect(self.getTreeRoot)

    def getdirsize(self, dir_path):
        size = 0
        for root, dirs, files in os.walk(dir_path):
            size += sum([getsize(join(root, name)) for name in files])
        return size

    def time_format(self, timestamp):
        time_array = time.localtime(timestamp)
        week = {
            '0': '星期日',
            '1': '星期一',
            '2': '星期二',
            '3': '星期三',
            '4': '星期四',
            '5': '星期五',
            '6': '星期六'
        }
        if time_array.tm_mon < 10:
            tm_mon = '0'+str(time_array.tm_mon)
        else:
            tm_mon = time_array.tm_mon
        if time_array.tm_mday < 10:
            tm_mday = '0' + str(time_array.tm_mday)
        else:
            tm_mday = time_array.tm_mday
        if time_array.tm_hour < 10:
            tm_hour = '0'+ str(time_array.tm_hour)
        else:
            tm_hour = time_array.tm_hour
        if time_array.tm_min < 10:
            tm_min = '0'+ str(time_array.tm_min)
        else:
            tm_min = time_array.tm_min
        if time_array.tm_sec < 10:
            tm_sec = '0'+ str(time_array.tm_sec)
        else:
            tm_sec = time_array.tm_sec

        return f'{time_array.tm_year}年 {tm_mon}月 {tm_mday}日, {week[str(time_array.tm_wday)]}, {tm_hour}:{tm_min}:{tm_sec}'

    def fileStatusConfirm(self):
        self.status_main_window.close()

    def fileStatusUse(self):
        status_filename = self.file_status_window.lineEdit.text()
        if status_filename != self.file_status_window.filename:
            print('修改文件名')
            old_file_path = self.file_status_window.label_5.text()
            # print(old_file_path)
            new_fila_path = '\\'.join(old_file_path.split('\\')[:-1]) + '\\' + status_filename
            os.rename(old_file_path, new_fila_path)
            self.statusBar.showMessage('重命名文件 -> %s' % new_fila_path)
            self.file_status_window.pushButton.setEnabled(False)
            self.updateFileTree()

    def fileStatusCancel(self):
        self.status_main_window.close()

    def browser_finished(self, ):
        url = self.browser.url().url()
        print(url)
        if url.startswith('file:///'):
            url = url[8:]
        self.statusBar.showMessage(f'预览文件 -> {url} 成功！')

    def zoom_in_func(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() + 0.3)
        self.sp.setValue(self.browser.zoomFactor())

    def zoom_out_func(self):
        if self.browser.zoomFactor() > 1:
            self.browser.setZoomFactor(self.browser.zoomFactor() - 0.2)
            self.sp.setValue(self.browser.zoomFactor())

    def sp_value_change(self):
        self.browser.setZoomFactor(self.sp.value())

    def get_file_list(self,file_path):
        file_list = os.listdir(file_path)
        rows = len(file_list)
        self.tablewidget = QTableWidget()
        self.tablewidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.tablewidget.setRowCount(rows)
        self.tablewidget.setColumnCount(4)
        self.tablewidget.setHorizontalHeaderLabels(['文件名', '最后修改日期', '类型', '大小'])
        self.tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablewidget.verticalHeader().setVisible(False)
        self.tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablewidget.setShowGrid(False)
        self.tablewidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tablewidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.tablewidget.setColumnWidth(1,100)
        self.tablewidget.setColumnWidth(2,50)
        self.tablewidget.setColumnWidth(3,50)
        self.tablewidget.setFocusPolicy(Qt.NoFocus)  #  去除选中后的虚线框
        self.tablewidget.itemDoubleClicked.connect(self.tablewidget_double_clicked)
        self.tablewidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tablewidget.customContextMenuRequested['QPoint'].connect(self.tablewidget_right_menu)


        table_header = self.tablewidget.horizontalHeader()
        table_header.setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        header_font = table_header.font()
        header_font.setBold(True)
        table_header.setFont(header_font)
        table_header.setStyleSheet('''
                QHeaderView::section{
                        padding-left: 30px;
                        height:40px;
                        font-size:18px; 
                        background-color: #D1D1D1;
                    }
                ''')
        for row_num in range(rows): # 行号
            if os.path.isdir(os.path.join(file_path,file_list[row_num])):
                file_type = '文件夹'
                statinfo = os.stat(os.path.join(file_path, file_list[row_num]))
                last_update_time = self.time_format(statinfo.st_mtime)  # 最后修改时间
                file_info = [file_list[row_num],last_update_time,file_type,'']
            else:
                if file_list[row_num].endswith('.jpg'):
                    file_type = 'JPG图片文件( *.jpg )'
                    file_image = '../images/jpg_status.png'
                elif file_list[row_num].endswith('.html'):
                    file_type = 'HTML页面文件( *.html )'
                    file_image = '../images/html_status.png'
                elif file_list[row_num].endswith('.xlsx'):
                    file_type = 'XLSX表格文件( *.xlsx )'
                    file_image = '../images/excel_status.png'
                elif file_list[row_num].endswith('.png'):
                    file_type = 'XLSX表格文件( *.xlsx )'
                    file_image = '../images/png_status.png'
                else:
                    file_type = 'Other其他文件类型( *.%s)' % (os.path.splitext(file_list[row_num])[1])
                    file_image = '../images/file_status.png'
                statinfo = os.stat(os.path.join(file_path, file_list[row_num]))
                last_update_time = self.time_format(statinfo.st_mtime)  # 最后修改时间
                file_size = self.approximateSize(statinfo.st_size)
                file_info = [file_list[row_num], last_update_time, file_type,file_size]


            for i in range(4):
                item = QTableWidgetItem(file_info[i])
                self.tablewidget.setItem(row_num,i,item)
            self.tablewidget.setRowHeight(row_num,50)
            self.tablewidget.setStyleSheet('''
                    QTableWidget::item {
                        padding: 10px;
                        border: 0px solid red;
                        
                        }
                    QTableWidget::item:selected {
                        color: black;
                        background-color: rgb(102,204,204);
                        }


            ''')
        return self.tablewidget

    def tablewidget_right_menu(self,pos):
        item_row = self.tablewidget.currentRow()
        item_column = self.tablewidget.currentColumn()
        file_name = self.tablewidget.item(item_row,0).text()
        file_path = os.path.join(self.paths[-1],file_name)
        file_path = file_path.replace('\\','/')
        print(file_path)
        menu = QMenu(self.tablewidget)
        delete = menu.addAction('删除')
        copy = menu.addAction('复制')
        paste = menu.addAction('粘贴')
        openLocalFile = menu.addAction('浏览本地文件')
        file_roperty = menu.addAction("属性")
        action = menu.exec_(self.tablewidget.mapToGlobal(pos))
        if action == delete:
            reply = QMessageBox.warning(self.mainwindow, '删除确认', '确认删除吗？', QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.No)
            if os.path.isdir(file_path) and reply == 16384:
                print('delete dir')
                shutil.rmtree(file_path)
                self.statusBar.showMessage(f'删除 {file_path} 成功！')
                self.updateFileTree()
            elif not os.path.isdir(file_path) and reply == 16384:
                print('delete file')
                os.remove(file_path)
                self.statusBar.showMessage("删除 -> %s 成功!" % file_path)
                print(self.paths)
                self.updateFileTree()
                self.statusBar.showMessage(f'删除 {file_path} 成功!')

        elif action == copy:
            try:
                data = QMimeData()
                url = QUrl.fromLocalFile(file_path)
                clipboard = QApplication.clipboard()
                data.setUrls([url])
                clipboard.setMimeData(data)
                self.statusBar.showMessage("已复制 -> %s 到剪切板" % file_path)
            except Exception as e:
                QMessageBox.about(self.mainwindow, '错误', '文件不存在!')
                self.statusBar.showMessage("复制 -> %s  出错，文件不存在!" % file_path)

        elif action == paste:
            data = QApplication.clipboard().mimeData()
            source_file_url = data.urls()[0].url()
            self.paste_thread = FilePasteThread(source_file_url[8:], file_path)
            self.paste_thread.sinOut.connect(self.filePasteComplete)
            self.paste_thread.start()


        elif action == openLocalFile:
            try:
                local_path = file_path.replace('/', '\\')
                os.system("explorer.exe %s" % os.path.dirname(local_path))
            except Exception as e:
                QMessageBox.warning(self.mainwindow, '错误', '打开文件不存在!')

        elif action == file_roperty:
            print('查看文件属性')
            if os.path.isdir(file_path):
                file_type = '文件夹'
                file_image = '../images/folder_status.png'
                _dir = True
            else:
                _dir = False
                if file_path.endswith('.jpg'):
                    file_type = 'JPG图片文件( *.jpg )'
                    file_image = '../images/jpg_status.png'
                elif file_path.endswith('.html'):
                    file_type = 'HTML页面文件( *.html )'
                    file_image = '../images/html_status.png'
                elif file_path.endswith('.xlsx'):
                    file_type = 'XLSX表格文件( *.xlsx )'
                    file_image = '../images/excel_status.png'
                elif file_path.endswith('.png'):
                    file_type = 'XLSX表格文件( *.xlsx )'
                    file_image = '../images/png_status.png'
                else:
                    file_type = 'Other其他文件类型( *.%s)' % (os.path.splitext(file_path)[1])
                    file_image = '../images/file_status.png'
            if _dir:
                '''文件夹大小去要遍历每个子文件夹与文件累加'''
                file_size = self.getdirsize(file_path)
                # print(file_path)
                statinfo = os.stat(file_path)
            else:
                statinfo = os.stat(file_path)
                file_size = statinfo.st_size
            file_atime = self.time_format(statinfo.st_atime)  # 文件最后访问时间
            file_ctime = self.time_format(statinfo.st_ctime)  # 文件创建时间
            file_mtime = self.time_format(statinfo.st_mtime)  # 文件最后修改时间
            self.file_status_window = FileStatusWindow()
            self.file_status_window.filename = file_path.replace('\\', '/').split('/')[-1]
            self.status_main_window = QMainWindow(MainWindow)
            self.file_status_window.setupUi(self.status_main_window)
            self.file_status_window.lineEdit.setText(self.file_status_window.filename)
            self.file_status_window.label_3.setText(file_type)
            self.file_status_window.label_5.setText(file_path.replace('/', '\\'))
            self.file_status_window.label_9.setText(file_ctime)
            self.file_status_window.label_11.setText(file_mtime)
            self.file_status_window.label_13.setText(file_atime)
            self.file_status_window.label_7.setText(self.approximateSize(file_size))
            self.file_status_window.pushButton.clicked.connect(self.fileStatusUse)  # 应用按钮click出发函数
            self.file_status_window.pushButton_2.clicked.connect(self.fileStatusConfirm)
            self.file_status_window.pushButton_3.clicked.connect(self.fileStatusCancel)
            pix = QPixmap(file_image)
            self.file_status_window.label.setPixmap(pix)
            self.status_main_window.show()

    def tablewidget_double_clicked(self):
        row = self.tablewidget.currentRow() # 拿到当前行
        file_name = self.tablewidget.item(row,0).text()
        print(file_name)
        file_path = os.path.join(self.paths[-1],file_name).replace('\\','/')
        if os.path.isdir(file_path):
            # 文件夹 执行打开操作
            self.paths.append(file_path)
            self.tab3_layout.removeWidget(self.tablewidget)
            del self.tablewidget
            self.tablewidget = self.get_file_list(self.paths[-1])
            self.tab3_layout.addWidget(self.tablewidget)

        else:
            # 不是文件夹  判断文件类型，执行预览操作
            if file_path.endswith('jpg') or file_path.endswith('.png') or file_path.endswith('html') or file_path.endswith('pdf'):
                file_path = file_path.replace('\\', '/')
                self.browser.stop()
                self.browser.destroy()
                self.browser.close()
                del self.browser
                self.browser = Browser()
                self.tab_layout.addWidget(self.browser)
                self.browser.load(QUrl('file:///' + file_path))
                self.zoom_in_button.clicked.connect(self.zoom_in_func)  # 放大与缩小按钮出发事件设置
                self.zoom_out_button.clicked.connect(self.zoom_out_func)
                self.sp.setValue(self.browser.zoomFactor())
                filename = file_path.split('/')[-1]
                self.tabWidget.setCurrentIndex(1)
                self.statusBar.showMessage(f'预览文件 -> {filename} , 请等候...')
                self.browser.loadFinished.connect(self.browser_finished)
            else:
                reply = QMessageBox.information(self.mainwindow,
                                                "调用系统软件",
                                                "软件不支持此类型文件打开！\n是否调用系统程序打开此文件?",
                                                QMessageBox.Yes | QMessageBox.No)
                if reply == 16384:
                    os.startfile(file_path)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # MainWindow.showFullScreen()
    MainWindow.show()
    sys.exit(app.exec_())
