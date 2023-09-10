from PyQt6.QtCore import QTimer

from model.account_model import AccountModel
from model.database_config_model import DatabaseConfigModel
from model.database_manager import DatabaseManager
from view.creat_account_view import CreateAccountView
from view.loading_view import LoadingView
from view.login_view import LoginView


class ScreenController:
    def __init__(self, app):

        # Constructor for the ScreenController class. It receives an instance of QApplication as an argument.
        self.app = app

        # Create an instance of DatabaseConfigModel
        self.db_config_model = DatabaseConfigModel()

        # Create an instance of DatabaseManager
        self.database_manager = DatabaseManager(self.db_config_model)

        self.create_account_view = CreateAccountView()

        # Configure a conexão entre a view e o controller
        self.create_account_view.set_controller(self)

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

    def create_account(self, first_name, last_name, email, password):

        # Create an AccountModel instance with the provided data
        account_model = AccountModel(first_name, last_name, email, password)
        print('TESTEe', account_model)

        # Attempt to save the account data to the database
        if self.database_manager.save_account(account_model):
            print('Account created and saved successfully!')

        else:
            # Handle the case where saving to the database failed
            print('Failed to create and save the account.')
