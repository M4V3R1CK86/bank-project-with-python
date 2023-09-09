from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor, QIcon, QMovie, QPainter, QPixmap
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                             QMessageBox, QPushButton, QVBoxLayout, QWidget)


class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (QMainWindow)

        # Configure the main window properties
        self.setWindowTitle("DarkStar Bank!")  # Set the window title
        self.setFixedSize(1334, 750)  # Set the fixed size of the window
        # Set the background color using CSS style
        self.setStyleSheet('background-color:#fe2757')
        # Set the window icon
        self.setWindowIcon(QIcon('resources/img/icon/aviation.png'))
