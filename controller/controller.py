from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMessageBox

from model.account_model import AccountModel
from model.database_config_model import DatabaseConfigModel
from model.database_manager import DatabaseManager
from view.creat_account_view import CreateAccountView
from view.home_view import HomeView
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
        QTimer().singleShot(2000, self.show_login_view)

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

        # Attempt to save the account data to the database
        if self.database_manager.save_account(account_model):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Account created successfully!!")
            msg.setWindowTitle("success!")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            QTimer.singleShot(200, self.close_create_account_and_show_login)

        else:
            # Handle the case where saving to the database failed
            print('Failed to create and save the account.')

    def logging_in(self, email, password):

        # Chame are_credentials_valid com db_params como argumento
        if self.database_manager.are_credentials_valid(email, password):
            # Credenciais válidas, exiba a HomeView
            self.show_home_view()
            self.login_view.close()
        else:
            # Credenciais inválidas, exiba uma mensagem de erro
            self.login_view.show_error_message("Invalid email or password")

    def close_create_account_and_show_login(self):
        # Fecha a janela de create_account
        self.create_account_view.close()

        # Mostra a tela de login
        self.show_login_view()

    def show_home_view(self):

        self.home_view = HomeView()
        self.home_view.show()
