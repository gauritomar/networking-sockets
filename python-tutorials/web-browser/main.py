from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class MyWebBrowser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)

        self.setWindowTitle("Gauri's Web Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        
        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)
        self.go_btn.clicked.connect(self.navigate_to_url)

        self.browser = QWebEngineView()  # Define browser before the buttons
        self.back_btn = QPushButton("Back")
        self.back_btn.setMinimumHeight(30)
        self.back_btn.clicked.connect(self.browser.back)  # Connect to self.browser
        

        self.forward_btn = QPushButton("Forward")
        self.forward_btn.setMinimumHeight(30)
        self.forward_btn.clicked.connect(self.browser.forward)  # Connect to self.browser

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://google.com"))

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('http'):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))

app = QApplication([])
window = MyWebBrowser()
window.show()
app.exec_()
