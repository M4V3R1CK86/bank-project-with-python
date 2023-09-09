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

        # Calculate the position to center the window on the screen
        screen_geo = self.screen().availableGeometry()
        x = (screen_geo.width() - self.width()) // 2
        y = (screen_geo.height() - self.height()) // 2
        self.move(x, y)

        # Create a title label
        title_label = QLabel("DarkStar Bank", self)
        # Style the title label
        title_label.setStyleSheet("color: #eec1c0; font-size: 50px;")
        title_label.adjustSize()  # Adjust the label size based on its content
        title_label.move((self.width() - title_label.width()) //
                         2, 250)  # Center the label horizontally

        # Create a username input field
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText(
            "User")  # Set a placeholder text
        username_input_width = 200  # Define the desired width
        self.username_input.setGeometry(
            (self.width() - username_input_width) // 2, 320, username_input_width, 30)  # Set geometry and position
        self.username_input.setStyleSheet(
            "background-color: #7ceec1c0; color: #ffede9; border-radius: 10px; padding-left: 10px;")  # Style the input field

        # Create a password input field
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText(
            "Password")  # Set a placeholder text
        self.password_input.setEchoMode(
            QLineEdit.EchoMode.Password)  # Mask the password text
        self.password_input.setGeometry(
            (self.width() - username_input_width) // 2, 360, username_input_width, 30)  # Set geometry and position
        self.password_input.setStyleSheet(
            "background-color: #7ceec1c0; color: #ffede9; border-radius: 10px; padding-left: 10px;")  # Style the input field
