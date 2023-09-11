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

        styleSheet_input = "background-color: #7ceec1c0; color: #ffede9; border-radius: 10px; padding-left: 10px;"
        styleSheet_login_btn = "background-color: #eec1c0; color: #de9597; border-radius: 10px;"
        styleSheet_create_account_btn = "background: none; border: none; color: #de9597;"

        PointingHandCursor = QCursor(Qt.CursorShape.PointingHandCursor)

        # Create a title label
        title_label = QLabel("DarkStar Bank", self)
        title_label.setStyleSheet("color: #eec1c0; font-size: 50px;")
        title_label.adjustSize()
        title_width = title_label.width()
        title_label.move((width_screen - title_width) // 2, 250)

        # Create a username input field
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("User")
        self.username_input.setGeometry(x, 320, width_input, 30)
        self.username_input.setStyleSheet(styleSheet_input)

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

        login_btn.clicked.connect(self.validate_login)

        # Create a Create Account button
        create_account_btn = QPushButton("Create Account", self)
        create_account_btn.setGeometry(x2, 440, width_btn, 30)
        create_account_btn.setStyleSheet(styleSheet_create_account_btn)
        create_account_btn.setCursor(PointingHandCursor)

        # Connect the Create Account button to a slot method
        create_account_btn.clicked.connect(self.on_create_account_btn_clicked)

    # Set the controller instance
    def set_controller(self, controller):
        self.controller = controller

    # Slot method to handle the Create Account button click.
    def on_create_account_btn_clicked(self):
        if self.controller:
            self.controller.show_create_account_view()

    # Get the username and password from input fields
    def validate_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Check if username or password are empty
        if not username or not password:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please fill in all fields.")
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()
            msg.move(self.geometry().center())

        # Check if the password length is less than 6 characters
        elif len(password) < 6:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Password must be at least 6 characters long.")
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()
            msg.move(self.geometry().center())

        # Check if username and password are correct
        elif username != "correct_user" or password != "correct_password":
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Incorrect username or password.")
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()
            msg.move(self.geometry().center())

        else:
            # If validation is successful, close the login window
            self.close()
