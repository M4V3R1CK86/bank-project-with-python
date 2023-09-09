from PyQt6.QtCore import QTimer

from view.creat_account_view import CreateAccountView
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

        self.login_view = LoginView()
        self.login_view.controller = self  # Pass the controller instance
        self.login_view.show()
        self.loading_view.close()  # Close the loading_view window.

    def show_create_account_view(self):
        self.create_account_view = CreateAccountView()
        self.create_account_view.set_controller(self)
        self.create_account_view.show()
        self.login_view.close()  # Close the login_view window.

    #  # Define the back_to_login_callback method here
    # def back_to_login_callback(self):
    #     # Implement the logic to go back to the login view
    #     pass
