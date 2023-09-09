from PyQt6.QtCore import QTimer

from view.loading_view import LoadingView
from view.login_view import LoginView


class ScreenController:
    def __init__(self, app):
        # Constructor for the ScreenController class. It receives an instance of QApplication as an argument.
        self.app = app

    def show_loading_view(self):
        # Method to display the loading view.

        # Create an instance of the LoadingView class.
        self.loading_view = LoadingView()

        # Show the loading view, making it visible to the user.
        self.loading_view.show()
        # Create a QTimer instance and schedule a single-shot timer event to call the self.show_login_view() function after 1000 milliseconds (1 second).

        QTimer().singleShot(1000, self.show_login_view)

    def show_login_view(self):
        # Define a method called show_login_view that belongs to the current class.

        self.login_view = LoginView()
        # Create an instance of the LoginView class and assign it to the instance variable self.login_view.

        self.login_view.show()
        # Show the login_view window.

        self.loading_view.close()
        # Close the loading_view window.
