import re  # Módulo para validação de e-mail

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QCursor, QIcon, QKeySequence, QPalette, QPixmap
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                             QMessageBox, QPushButton, QWidget)


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

        self.first_name_input = QLineEdit(self)
        self.first_name_input.setPlaceholderText("First Name")
        first_name_input_width = 200
        self.first_name_input.setGeometry(
            (self.width() - first_name_input_width) // 2, 320, first_name_input_width, 30)
        self.first_name_input.setStyleSheet(
            "background-color: #7ceec1c0; color: #ffede9; border-radius: 10px; padding-left: 10px;")

        self.last_name_input = QLineEdit(self)
        self.last_name_input.setPlaceholderText("Last Name")
        last_name_input_width = 200
        self.last_name_input.setGeometry(
            (self.width() - last_name_input_width) // 2, 360, last_name_input_width, 30)
        self.last_name_input.setStyleSheet(
            "background-color: #7ceec1c0; color: #ffede9; border-radius: 10px; padding-left: 10px;")

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("E-mail")
        email_input_width = 200
        self.email_input.setGeometry(
            (self.width() - email_input_width) // 2, 400, email_input_width, 30)
        self.email_input.setStyleSheet(
            "background-color: #7ceec1c0; color: #ffede9; border-radius: 10px; padding-left: 10px;")

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        password_input_width = 200
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setGeometry(
            (self.width() - password_input_width) // 2, 440, password_input_width, 30)
        self.password_input.setStyleSheet(
            "background-color: #7ceec1c0; color: #ffede9; border-radius: 10px; padding-left: 10px;")

        # Create a "Create Account" button
        create_account_button = QPushButton("Create Account", self)
        create_account_button.setGeometry(
            (self.width() - 100) // 2, 480, 100, 30)  # Set geometry and position
        create_account_button.setStyleSheet(
            "background-color: #eec1c0; color: #de9597; border-radius: 10px;")  # Style the button
        create_account_button.setCursor(QCursor(
            Qt.CursorShape.PointingHandCursor))  # Set cursor shape
        # Connect the back_button click event to a method
        create_account_button.clicked.connect(self.create_account)

        # Create a QPushButton with an icon (image) to  "Back to Login"
        back_button = QPushButton(self)
        # Define the position and size of the button
        back_button.setGeometry(20, 20, 40, 40)
        # path
        arrow_icon = QIcon(QPixmap('resources/img/icon/left-arrow.png'))
        back_button.setIcon(arrow_icon)
        back_button.setIconSize(back_button.size())

        # Make the button flat (remove button styling)
        back_button.setFlat(True)
        back_button.setStyleSheet("QPushButton:pressed { border: none; }")
        # back_button.setStyleSheet("QPushButton:pressed { background-color: #DE959714; }")

        back_button.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))  # Set cursor shape

        # Connect the back_button click event to a method
        back_button.clicked.connect(self.go_back_to_login)

    def create_account(self):

        first_name = self.first_name_input.text().strip()
        last_name = self.last_name_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text()

        # validations
        if not first_name or not last_name or not email or not password:
            self.show_error_message("Please fill in all fields.")
        elif len(password) < 6:
            self.show_error_message(
                "Password must be at least 6 characters long.")
        elif not self.is_valid_email(email):
            self.show_error_message("Invalid email format.")
        else:
            # Clear the input fields
            self.first_name_input.setText("")
            self.last_name_input.setText("")
            self.email_input.setText("")
            self.password_input.setText("")

            print('Account created successfully!')
            print('First Name:', first_name)
            print('Last Name:', last_name)
            print('Email:', email)
            print('Password:', password)

    def is_valid_email(self, email):
        # Use a regular expression to validate the email format
        # This regular expression checks a simple email format
        email_pattern = r'^\S+@\S+\.\S+$'
        return re.match(email_pattern, email) is not None

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()
        msg.move(self.geometry().center())

    def set_controller(self, controller):
        self.controller = controller

    # Define a method to handle the back button click event
    def go_back_to_login(self):
        self.close()  # close create_account window
        if self.controller:
            # Call method on controller to show login screen
            self.controller.show_login_view()
