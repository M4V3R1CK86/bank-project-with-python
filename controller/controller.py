import bcrypt
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMessageBox

from model.database_config_model import DatabaseConfigModel
from model.database_manager import DatabaseManager
from model.users_model import UsersModel
from view.base_view import BaseView
from view.create_account_view import CreateAccountView
from view.home_view import HomeView
from view.loading_view import LoadingView
from view.login_view import LoginView
from view.transfer_dialog_view import TransferDialog


class ScreenController:

    def __init__(self, app):
        # Constructor for the ScreenController class.
        # It receives an instance of QApplication as an argument.
        self.app = app

        # Create an instance of DatabaseConfigModel to handle database configuration.
        self.db_config_model = DatabaseConfigModel()

        # Create an instance of DatabaseManager to manage database operations.
        self.database_manager = DatabaseManager(self.db_config_model)

    def show_loading_view(self):
        # Method to display the loading view.

        # Create an instance of the LoadingView class.
        self.loading_view = LoadingView()

        # Show the loading view, making it visible to the user.
        self.loading_view.show()

        # Create a QTimer instance and schedule a single-shot timer event
        # to call the self.show_login_view() function
        #  after 2000 milliseconds (2 seconds).
        QTimer().singleShot(2000, self.show_login_view)

    def show_login_view(self):
        # Method to show the login view.

        # Create an instance of the LoginView class.
        self.login_view = LoginView()

        # Pass the controller instance to the login view.
        self.login_view.set_controller(self)

        # Show the login view.
        self.login_view.show()

        # Close the loading_view window.
        self.loading_view.close()

    def show_create_account_view(self):
        # Method to show the create account view.

        # Create an instance of the CreateAccountView class.
        self.create_account_view = CreateAccountView()

        # Set the controller for the create account view.
        self.create_account_view.set_controller(self)

        # Show the create account view.
        self.create_account_view.show()

        # Close the login_view window.
        self.login_view.close()

    def show_home_view(self, user_id, first_name, last_name, account_data):
        # Method to show the home view for an authenticated user.

        # Create an instance of HomeView with user information.
        self.home_view = HomeView(user_id, first_name, last_name, account_data)

        self.home_view.set_controller(self)

        # Show the home view.
        self.home_view.show()

    def create_account(self, first_name, last_name, email, password):

        # Method to create a new user account.

        # Check if the provided email already exists in the database
        if self.database_manager.is_email_registered(email):
            # Display an error message if the email is already registered.
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Email is already registered.")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        # Create an instance of UsersModel with user information.
        users_model = UsersModel(first_name, last_name, email)

        # Set the hashed password for the user.
        users_model.set_password(password)

        # Attempt to save the user account in the database and get the id of the user
        user_id = self.database_manager.save_account(users_model)

        if user_id is not None:
            # Display a success message if the account is created and saved.
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("User created successfully!!")
            msg.setWindowTitle("Success!")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()

            # Call the create_account_bank method to associate the bank account with the user
            # Pass user_id as an argument to the method
            if self.database_manager.create_account_bank(user_id):
                # Display a success message if the bank account is created and associated.
                bank_msg = QMessageBox()
                bank_msg.setIcon(QMessageBox.Icon.Information)
                bank_msg.setText(
                    "Bank account created and associated to User successfully!!")
                bank_msg.setWindowTitle("Success!")
                bank_msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                bank_msg.exec()
            else:
                # Handle errors if creating the bank account fails.
                print('Failed to create and associate the bank account.')

            # Close the create_account_view and show the login view after a delay.
            QTimer.singleShot(200, self.close_create_account_and_show_login)
        else:
            # Display an error message if the account creation fails.
            print('Failed to create and save the account.')

    def logging_in(self, email, password):
        # Method to handle user login.

        # Check if the provided email and password are valid credentials.
        user_data = self.database_manager.are_credentials_valid(
            email, password)

        if user_data:
            # If valid credentials, extract user information.
            user_id, first_name, last_name = user_data

            # Chame o método para obter os dados da conta
            account_data = self.database_manager.get_user_account_data(user_id)

            # Show the home view for the authenticated user.
            self.show_home_view(user_id, first_name, last_name, account_data)

            # Close the login_view.
            self.login_view.close()
        else:
            # Show an error message for invalid credentials.
            self.login_view.show_error_message("Invalid email or password")

    def show_transfer_dialog_view(self, user_id, balance):

        self.transfer_view = TransferDialog(user_id, balance)
        self.transfer_view.set_controller(self)
        self.transfer_view.show()

    def is_valid_amount(self, amount, balance):
        try:
            amount = float(amount)
            balance = float(balance)
            if amount > balance:
                return False  # O valor de transferência não pode ser maior que o saldo
        except ValueError:
            return False
        return True

    def transfer(self, user_id, balance, amount, recipient, branch):
        # Verificar se o valor da transferência é válido
        if not self.is_valid_amount(amount, balance):
            self.transfer_view.show_error_message("Valor inválido.")
            return

        # Verificar se a conta de destino existe
        if not self.database_manager.is_valid_account(recipient, branch):
            self.transfer_view.show_error_message("Conta de destino inválida.")
            return

        # Se todas as verificações passarem, execute a transferência
        if self.database_manager.transfer_funds(user_id, recipient, amount):
            self.transfer_view.show_message("Transferência bem-sucedida.")
            # Atualize o saldo exibido na interface do usuário (opcional)
            # self.transfer_view.update_balance(new_balance)

            # Feche a TransferDialog
            self.transfer_view.close()

            # Atualize o saldo na HomeView (supondo que o método `update_balance` exista)
            if self.home_view:
                new_balance = balance - float(amount)
                self.home_view.update_balance(new_balance)
        else:
            self.transfer_view.show_error_message("Falha na transferência.")

    def close_create_account_and_show_login(self):
        # Method to close the create_account_view and show the login view.

        # Close the create_account_view.
        self.create_account_view.close()

        # Show the login view.
        self.show_login_view()
