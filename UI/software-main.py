import sys
from index import Ui_MainWindow

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())