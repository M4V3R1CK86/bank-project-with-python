from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QCursor, QIcon, QKeySequence, QPalette, QPixmap
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

        first_name_input = QLineEdit(self)
        first_name_input.setPlaceholderText("First Name")
        first_name_input_width = 200
        first_name_input.setGeometry(
            (self.width() - first_name_input_width) // 2, 320, first_name_input_width, 30)
        first_name_input.setStyleSheet(
            "background-color: #7ceec1c0; color: #ffede9; border-radius: 10px; padding-left: 10px;")

        last_name_input = QLineEdit(self)
        last_name_input.setPlaceholderText("Last Name")
        last_name_input_width = 200
        last_name_input.setGeometry(
            (self.width() - last_name_input_width) // 2, 360, last_name_input_width, 30)
        last_name_input.setStyleSheet(
            "background-color: #7ceec1c0; color: #ffede9; border-radius: 10px; padding-left: 10px;")

        email_input = QLineEdit(self)
        email_input.setPlaceholderText("E-mail")
        email_input_width = 200
        email_input.setGeometry(
            (self.width() - email_input_width) // 2, 400, email_input_width, 30)
        email_input.setStyleSheet(
            "background-color: #7ceec1c0; color: #ffede9; border-radius: 10px; padding-left: 10px;")

        password_input = QLineEdit(self)
        password_input.setPlaceholderText("Password")
        password_input_width = 200
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        password_input.setGeometry(
            (self.width() - password_input_width) // 2, 440, password_input_width, 30)
        password_input.setStyleSheet(
            "background-color: #7ceec1c0; color: #ffede9; border-radius: 10px; padding-left: 10px;")

        # Create a "Create Account" button
        create_account_button = QPushButton("Create Account", self)
        create_account_button.setGeometry(
            (self.width() - 100) // 2, 480, 100, 30)  # Set geometry and position
        create_account_button.setStyleSheet(
            "background-color: #eec1c0; color: #de9597; border-radius: 10px;")  # Style the button
        create_account_button.setCursor(QCursor(
            Qt.CursorShape.PointingHandCursor))  # Set cursor shape

        # Create a QPushButton with an icon (image) to  "Back to Login"
        back_button = QPushButton(self)
        # Define the position and size of the button
        back_button.setGeometry(20, 20, 40, 40)
        arrow_icon = QIcon(QPixmap('resources/img/icon/left-arrow.png'))
        back_button.setIcon(arrow_icon)
        back_button.setIconSize(back_button.size())

        # Make the button flat (remove button styling)
        back_button.setFlat(True)
        back_button.setStyleSheet("QPushButton:pressed { border: none; }")
        # back_button.setStyleSheet("QPushButton:pressed { background-color: #DE959714; }")

        back_button.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))  # Set cursor shape

        # Connect the back_button click event to a method (e.g., go_back_to_login)
        back_button.clicked.connect(self.go_back_to_login)

    # Define a method to handle the back button click event
    def go_back_to_login(self):
        # Implement the logic to go back to the login view here
        pass
