ButtonStyle = '''
    QPushButton{
    border:1px solid black;
    margin:15px;
    padding-left:10px;
    padding-right:10px;
    padding-top:5px;
    padding-bottom:5px;
    border-radius:4px;
    font-size:18px
    }
    QPushButton:hover{
    background-color:rgb(102,204,204);
    }
'''

LineEdit = '''
    QLineEdit{
    border:1px solid black;
    border-radius:5px;
    }

'''

menu = '''
    QMenu:hover{
    background-color:rgb(102,204,204)
    }

'''
QMenuBar = '''
    

    QMenuBar::item:selected {
        background: #66CCCC;
    }
'''

QStatusBar = '''
    QStatusBar{
    margin-bottom:2px;
    font-size:16px
    }
'''

QLabel = '''
    QLabel{
    border:1px solid black;
    background-color:none;
    margin-top:2px;
    margin-bottom:2px;
    margin-left:10px;
    margin-right:10px;
    padding:3px;
    }
'''


QTabWidget = '''

    QTabWidget::pane { /* The tab widget frame */
        border-top: 2px solid #C2C7CB;
    }
    QTabWidget::tab-bar {
        left: 20px; /* move to the right by 5px */
    }
    /* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */
    QTabBar::tab {
        width:80px;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
        padding: 2px;
        
    }
    QTabBar::tab:selected, QTabBar::tab:hover {
        background-color: #48D1CC;
        border-bottom-color: rgb(102,204,204); /* same as pane color */
    }
    
    QTabBar::tab:!selected {
        margin: 4px; /* make non-selected tabs look smaller */
    }
'''

QTreeView = '''
    QTreeView {
        font-size:18px;
    }
    QTreeView {
    show-decoration-selected: 1;
    }
    QTreeView::item {
        border: 1px solid #d9d9d9;
        border-top-color: transparent;
        border-bottom-color: transparent;
    }
    QTreeView::item:hover {
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);
        border: 1px solid #bfcde4;
    }
    QTreeView::item:selected {
       border: 1px solid #567dbc;
    }
    QTreeView::item:selected:active{
       background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);
    }
    QTreeView::item:selected:!active {
       background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);
    }

'''

QDoubleSpinBox = '''
    QDoubleSpinBox {
        padding-right: 15px; /* make room for the arrows */
        
    }
    QDoubleSpinBox::up-button {
        subcontrol-origin: border;
        subcontrol-position: top right; /* position at the top right corner */
        width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */
        background: rgb(100, 0, 0);
    }
    QDoubleSpinBox::up-button:hover {
        background: rgb(170, 0, 0);
    }
    QDoubleSpinBox::up-button:pressed {
        background: rgb(255, 0, 0);
    }
    QDoubleSpinBox::up-arrow {
        background: rgb(255,255,255);
        width: 10px;
        height: 10px;
    }
    QDoubleSpinBox::up-arrow:disabled, QDoubleSpinBox::up-arrow:off { /* off state when value is max */
        background: rgb(0,0,0);
        width: 10px;
        height: 10px;
    }
    QDoubleSpinBox::down-button {
        subcontrol-origin: border;
        subcontrol-position: bottom right; /* position at bottom right corner */
        width: 16px;
        background: rgb(0, 100, 0);
    }
    QDoubleSpinBox::down-button:hover {
        background: rgb(0, 170, 0);
    }
    QDoubleSpinBox::down-button:pressed {
        background: rgb(0, 255, 0);
    }
    QDoubleSpinBox::down-arrow {
        background: rgb(255,255,255);
        width: 10px;
        height: 10px;
    }
    /* off state when value in min */
    QDoubleSpinBox::down-arrow:disabled,QDoubleSpinBox::down-arrow:off { 
        background: rgb(0,0,0);
        width: 10px;
        height: 10px;
    }

'''

QTableWidget = '''
    QTableWidget{
    background:none;
    font-size:16px;
    padding:20px
    }

'''

