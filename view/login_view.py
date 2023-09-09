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

        # Create a "Login" button
        login_button = QPushButton("Login", self)
        login_button.setGeometry(
            (self.width() - 100) // 2, 400, 100, 30)  # Set geometry and position
        login_button.setStyleSheet(
            "background-color: #eec1c0; color: #de9597; border-radius: 10px;")  # Style the button
        login_button.setCursor(QCursor(
            Qt.CursorShape.PointingHandCursor))  # Set cursor shape
        # Connect a click event to the validate_login method
        login_button.clicked.connect(self.validate_login)

        # Create a "Create Account" button
        create_account_button = QPushButton("Create Account", self)
        create_account_button.setGeometry(
            (self.width() - 100) // 2, 440, 100, 30)  # Set geometry and position
        create_account_button.setStyleSheet(
            "background: none; border: none; color: #de9597;")  # Style the button
        create_account_button.setCursor(QCursor(
            Qt.CursorShape.PointingHandCursor))  # Set cursor shape

    def validate_login(self):
        # Get the username and password from input fields
        username = self.username_input.text()
        password = self.password_input.text()

        # Check if username or password are empty
        if not username or not password:
            # Create a QMessageBox for displaying an error message
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please fill in all fields.")
            # Set the icon to a critical error
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()  # Display the message box
            # Center the message box on the window
            msg.move(self.geometry().center())

        # Check if the password length is less than 6 characters
        elif len(password) < 6:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Password must be at least 6 characters long.")
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()
            msg.move(self.geometry().center())

        # Check if username and password are correct (you can replace these with your own logic)
        elif username != "correct_user" or password != "correct_password":
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Incorrect username or password.")
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()
            msg.move(self.geometry().center())

        else:
            # If validation is successful, close the login window (you can add your logic here)
            self.close()
