import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLineEdit, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtCore import QUrl, QSettings

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Simple Browser")
        self.setGeometry(100, 100, 800, 600)

        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        self.create_actions()
        self.create_menu_bar()
        self.create_tool_bar()

    def create_actions(self):
        self.back_action = QAction("Back", self)
        self.back_action.triggered.connect(self.browser.back)

        self.forward_action = QAction("Forward", self)
        self.forward_action.triggered.connect(self.browser.forward)

        self.reload_action = QAction("Reload", self)
        self.reload_action.triggered.connect(self.browser.reload)

        self.home_action = QAction("Home", self)
        self.home_action.triggered.connect(self.navigate_home)

        self.quit_action = QAction("Quit", self)
        self.quit_action.triggered.connect(self.close)

    def create_menu_bar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        file_menu.addAction(self.quit_action)

    def create_tool_bar(self):
        toolbar = self.addToolBar("Navigation")
        toolbar.addAction(self.back_action)
        toolbar.addAction(self.forward_action)
        toolbar.addAction(self.reload_action)
        toolbar.addAction(self.home_action)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.on_search)
        toolbar.addWidget(self.url_bar)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def on_search(self):
        query = self.url_bar.text()
        if query:
            url = QUrl("https://www.google.com/search?q=" + query)
            self.browser.setUrl(url)
        else:
            QMessageBox.warning(self, "Warning", "Please enter a search query")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Enable all sites to set cookies with SameSite=None and Secure attributes
    settings = QSettings()
    settings.setValue('WebEngineSettings/ThirdPartyCookiesPolicy', 0)
    
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())
