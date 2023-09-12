from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow


class BaseView(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configure the main window properties

        self.setWindowTitle("DarkStar Bank")
        self.setFixedSize(1334, 750)
        self.setStyleSheet('background-color:#745b5b')
        self.setWindowIcon(QIcon('resources/img/icon/aviation.png'))

        # Calculate the position to center the window on the screen
        screen_geo = self.screen().availableGeometry()
        x = (screen_geo.width() - self.width()) // 2
        y = (screen_geo.height() - self.height()) // 2
        self.move(x, y)
