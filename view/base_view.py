from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow


class BaseView(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configure the main window properties
        self.setWindowTitle("DarkStar Bank!")
        self.setFixedSize(1334, 750)
        self.setStyleSheet('background-color:#fe2757')
        self.setWindowIcon(QIcon('resources/img/icon/aviation.png'))

        # Calculate the position to center the window on the screen
        screen_geo = self.screen().availableGeometry()
        x = (screen_geo.width() - self.width()) // 2
        y = (screen_geo.height() - self.height()) // 2
        self.move(x, y)

        # Create a title label
        # title_label = QLabel("DarkStar Bank", self)
        # title_label.setStyleSheet("color: #eec1c0; font-size: 50px;")
        # title_label.adjustSize()
        # title_label.move((self.width() - title_label.width()) // 2, 50)
