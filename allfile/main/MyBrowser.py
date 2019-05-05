from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication


class Browser(QWebEngineView):

    def __init__(self,parent = None):
        # print('new browser')
        super().__init__(parent=parent)
        self.setZoomFactor(1.25)
        print(self.zoomFactor())

    def zoom_in_func(self):
        self.setZoomFactor(self.zoomFactor() + 0.3)

    def zoom_out_func(self):
        if self.zoomFactor() > 1:
            self.setZoomFactor(self.zoomFactor() - 0.2)





if __name__ == '__main__':
    bro = Browser()
    bro.keyPressEvent()