# view/loading_view.py

from PyQt6.QtGui import QIcon, QMovie
from PyQt6.QtWidgets import QLabel, QMainWindow


class LoadingView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DarkStar Bank!")
        self.setFixedSize(1334, 750)
        self.setStyleSheet('background-color:#fe2757')
        self.setWindowIcon(QIcon('resources/img/icon/aviation.png'))
