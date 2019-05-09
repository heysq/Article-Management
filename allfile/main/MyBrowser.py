from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QWebEngineView):

    def __init__(self,parent = None):
        # print('new browser')
        super().__init__(parent=parent)
        self.setZoomFactor(1.25)
        # print(self.zoomFactor())


if __name__ == '__main__':
    bro = Browser()
    bro.keyPressEvent()