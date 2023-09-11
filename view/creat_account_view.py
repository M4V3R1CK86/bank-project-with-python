import re  # Módulo para validação de e-mail

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor, QIcon, QPixmap
from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QMessageBox,
                             QPushButton)

from view.base_view import BaseView


class CreateAccountView(BaseView):
    def __init__(self):
        super().__init__()

        width_screen = self.width()
        width_input = 200
        width_btn = 100
        x = (width_screen - width_input) // 2
        x2 = (width_screen - width_btn) // 2

        styleSheet_input = "background-color: #7ceec1c0; color: #ffede9; border-radius: 10px; padding-left: 10px;"
        styleSheet_login_btn = "background-color: #eec1c0; color: #de9597; border-radius: 10px;"
        styleSheet_create_account_btn = "background-color: #eec1c0; color: #de9597; border-radius: 10px;"

        PointingHandCursor = QCursor(Qt.CursorShape.PointingHandCursor)

        title_label = QLabel("DarkStar Bank", self)
        title_label.setStyleSheet("color: #eec1c0; font-size: 50px;")
        title_label.adjustSize()
        title_width = title_label.width()
        title_label.move((width_screen - title_width) // 2, 250)

        self.first_name_input = QLineEdit(self)
        self.first_name_input.setPlaceholderText("First Name")
        self.first_name_input.setGeometry(x, 320, width_input, 30)
        self.first_name_input.setStyleSheet(styleSheet_input)

        self.last_name_input = QLineEdit(self)
        self.last_name_input.setPlaceholderText("Last Name")
        self.last_name_input.setGeometry(x, 360, width_input, 30)
        self.last_name_input.setStyleSheet(styleSheet_input)

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("E-mail")
        self.email_input.setGeometry(x, 400, width_input, 30)
        self.email_input.setStyleSheet(styleSheet_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setGeometry(x, 440, width_input, 30)
        self.password_input.setStyleSheet(styleSheet_input)

        # Create a "Create Account" button
        create_account_button = QPushButton("Create Account", self)
        create_account_button.setGeometry(x2, 480, width_btn, 30)
        create_account_button.setStyleSheet(styleSheet_create_account_btn)
        create_account_button.setCursor(PointingHandCursor)

        # Connect the back_button click event to a method
        create_account_button.clicked.connect(self.create_account)

        # Create a QPushButton with an icon (image) to  "Back to Login"
        back_button = QPushButton(self)
        back_button.setGeometry(20, 20, 40, 40)
        arrow_icon = QIcon(QPixmap('resources/img/icon/left-arrow.png'))
        back_button.setIcon(arrow_icon)
        back_button.setIconSize(back_button.size())

        # Make the button flat (remove button styling)
        back_button.setFlat(True)
        back_button.setStyleSheet("QPushButton:pressed { border: none; }")
        back_button.setCursor(PointingHandCursor)

        # Connect the back_button click event to a method
        back_button.clicked.connect(self.go_back_to_login)

    def create_account(self):

        first_name = self.first_name_input.text().strip()
        last_name = self.last_name_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text()

        # Perform data validation
        if not self.is_valid_input(first_name, last_name, email, password):
            return  # Exit if validation fails

        # Call the create_account method in the controller, passing the data
        if self.controller:
            self.controller.create_account(
                first_name, last_name, email, password)

        # Clear the input fields
        self.first_name_input.setText("")
        self.last_name_input.setText("")
        self.email_input.setText("")
        self.password_input.setText("")

    def is_valid_input(self, first_name, last_name, email, password):

        # Perform data validation here and display error messages as needed
        if not first_name:
            self.show_error_message("Please enter your First Name.")
            return False

        elif not last_name:
            self.show_error_message("Please enter your Last Name.")
            return False

        elif not email:
            self.show_error_message("Please enter your Email.")
            return False

        elif not self.is_valid_email(email):
            self.show_error_message("Invalid email format.")
            return False

        elif len(password) < 6:
            self.show_error_message(
                "Password must be at least 6 characters long.")
            return False

        return True

    def is_valid_email(self, email):

        # Use a regular expression to validate the email format
        email_pattern = r'^\S+@\S+\.\S+$'
        return re.match(email_pattern, email) is not None

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()

    def set_controller(self, controller):
        self.controller = controller

    # Define a method to handle the back button click event
    def go_back_to_login(self):
        self.close()  # close create_account window
        if self.controller:
            # Call method on controller to show login screen
            self.controller.show_login_view()
