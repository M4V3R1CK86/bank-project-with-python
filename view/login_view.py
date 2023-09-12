import re  # Módulo para validação de e-mail

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QLabel, QLineEdit, QMessageBox, QPushButton

from view.base_view import BaseView


class LoginView(BaseView):
    def __init__(self):
        super().__init__()
        width_screen = self.width()
        width_input = 200
        width_btn = 100
        x = (width_screen - width_input) // 2
        x2 = (width_screen - width_btn) // 2

        styleSheet_input = "background-color: #331e1e; color: #ffffe8; border-radius: 10px; padding-left: 10px;"
        styleSheet_login_btn = "background-color: #331e1e; color: #ffffe8; border-radius: 10px;"
        styleSheet_create_account_btn = "background: none; border: none; color: #fea509;"

        PointingHandCursor = QCursor(Qt.CursorShape.PointingHandCursor)

        # Create a title label
        title_label = QLabel("DarkStar Bank", self)
        title_label.setStyleSheet("color: #ffffe8; font-size: 50px;")
        title_label.adjustSize()
        title_width = title_label.width()
        title_label.move((width_screen - title_width) // 2, 250)

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("E-mail")
        self.email_input.setGeometry(x, 320, width_input, 30)
        self.email_input.setStyleSheet(styleSheet_input)

        # Create a username input field
        # self.username_input = QLineEdit(self)
        # self.username_input.setPlaceholderText("User")
        # self.username_input.setGeometry(x, 320, width_input, 30)
        # self.username_input.setStyleSheet(styleSheet_input)

        # Create a password input field
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setGeometry(x, 360, width_input, 30)
        self.password_input.setStyleSheet(styleSheet_input)

        # Create a Login button
        login_btn = QPushButton("Login", self)
        login_btn.setGeometry(x2, 400, width_btn, 30)
        login_btn.setStyleSheet(styleSheet_login_btn)
        login_btn.setCursor(PointingHandCursor)

        login_btn.clicked.connect(self.logging_in)

        # Set the Enter key as a shortcut for the login button
        login_btn.setShortcut("Return")  # This sets Enter key as a shortcut

        # Create a Create Account button
        create_account_btn = QPushButton("Create Account", self)
        create_account_btn.setGeometry(x2, 440, width_btn, 30)
        create_account_btn.setStyleSheet(styleSheet_create_account_btn)
        create_account_btn.setCursor(PointingHandCursor)

        # Connect the Create Account button to a slot method
        create_account_btn.clicked.connect(self.on_create_account_btn_clicked)

    # Get the email and password from input fields
    def logging_in(self):
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()

        # Perform data validation
        if not self.is_valid_input(email, password):
            return  # Exit if validation fails

        # Call the logging_in method in the controller, passing the data
        if self.controller:
            self.controller.logging_in(email, password)

        # Clear the input fields
        self.email_input.setText("")
        self.password_input.setText("")

    def is_valid_input(self, email, password):

        # Perform data validation here and display error messages as needed
        if not email:
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

    # Slot method to handle the Create Account button click.
    def on_create_account_btn_clicked(self):
        if self.controller:
            self.controller.show_create_account_view()
