from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QIcon, QPalette
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QVBoxLayout, QWidget)


class CreateAccountView(QMainWindow):
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

        screen = QApplication.primaryScreen()
        screen_geo = screen.availableGeometry()
        x = (screen_geo.width() - self.width()) // 2
        y = (screen_geo.height() - self.height()) // 2
        self.move(x, y)

        title_label = QLabel("DarkStar Bank", self)
        title_label.setStyleSheet("color: #eec1c0; font-size: 50px;")
        title_label.adjustSize()
        title_label.move((self.width() - title_label.width()) // 2, 250)

        username_input = QLineEdit(self)
        username_input.setPlaceholderText("User Name")
        username_input_width = 200
        username_input.setGeometry(
            (self.width() - username_input_width) // 2, 320, username_input_width, 30)
        username_input.setStyleSheet(
            "background-color: #7ceec1c0; color: #ffede9; border-radius: 10px; padding-left: 10px;")

        email_input = QLineEdit(self)
        email_input.setPlaceholderText("User Name")
        email_input_width = 200
        email_input.setGeometry(
            (self.width() - email_input_width) // 2, 360, email_input_width, 30)
        email_input.setStyleSheet(
            "background-color: #7ceec1c0; color: #ffede9; border-radius: 10px; padding-left: 10px;")

        password_input = QLineEdit(self)
        password_input.setPlaceholderText("Password")
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        password_input.setGeometry(
            (self.width() - username_input_width) // 2, 400, username_input_width, 30)
        password_input.setStyleSheet(
            "background-color: #7ceec1c0; color: #ffede9; border-radius: 10px; padding-left: 10px;")

        # back_to_login_button = QPushButton("Back", self)
        # back_to_login_button.setGeometry(
        #     (self.width() - 200) // 2, 440, 50, 30)
        # back_to_login_button.setStyleSheet(
        #     "background-color: #eec1c0; color: #de9597; border-radius: 10px;")

        # back_to_login_button.clicked.connect(self.back_to_login_clicked)

    # def login_view(self):
    #     self.lv = LoginView()
    #     self.setCentralWidget(self.lv)

    # def back_to_login_clicked(self):
    #     self.back_to_login_callback()
