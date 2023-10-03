from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QDialog, QLabel, QLineEdit, QMessageBox,
                             QPushButton, QVBoxLayout)


class TransferDialog(QDialog):
    def __init__(self, user_id, balance, parent=None):
        super().__init__(parent)
        self.user_id = user_id
        self.balance = balance
        self.setWindowTitle("Transfer Money")
        self.setStyleSheet('background-color:#543d3c')
        self.setFixedSize(500, 250)

        layout = QVBoxLayout()

        self.amount_label = QLabel("Enter Amount to Transfer:")
        self.amount_input = QLineEdit()
        self.amount_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.amount_input.setPlaceholderText("100.0")

        self.recipient_label = QLabel("Enter Recipient Account Number:")
        self.recipient_input = QLineEdit()
        self.recipient_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.recipient_input.setPlaceholderText("000000001-2")

        self.branch_label = QLabel("Enter Branch:")
        self.branch_input = QLineEdit()
        self.branch_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.branch_input.setPlaceholderText("1234")

        self.transfer_button = QPushButton("Transfer")
        self.transfer_button.clicked.connect(self.validate_fields)

        layout.addWidget(self.amount_label)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.recipient_label)
        layout.addWidget(self.recipient_input)
        layout.addWidget(self.branch_label)
        layout.addWidget(self.branch_input)
        layout.addWidget(self.transfer_button)

        self.setLayout(layout)

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()

    def show_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("success")
        msg.setText(message)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def is_valid_amount(self, text):
        try:
            amount = float(text)
            if amount < 0:
                return False
        except ValueError:
            return False
        return True

    def is_valid_recipient(self, text):
        if len(text) != 11:
            return False
        if not text[:9].isdigit() or text[9] != '-' or not text[10].isdigit():
            return False
        return True

    def is_valid_branch(self, branch):
        if not branch:
            return False
        if not branch.isdigit() or len(branch) != 4:
            return False
        return True

    def validate_fields(self):

        amount = self.amount_input.text().strip()
        recipient = self.recipient_input.text().strip()
        branch = self.branch_input.text().strip()
        user_id = self.user_id
        balance = self.balance
        if not self.is_valid_input(amount, recipient, branch):
            return

        if self.controller:
            self.controller.transfer(
                user_id, balance, amount, recipient, branch)

    def is_valid_input(self, amount, recipient, branch):

        if not amount:
            self.show_error_message("Please enter amount.")
            return False

        if not self.is_valid_amount(amount):
            self.show_error_message("Invalid amount format.")
            return False

        if not recipient:
            self.show_error_message("Please enter recipient.")
            return False

        if not self.is_valid_recipient(recipient):
            self.show_error_message("Invalid recipient format.\n xxxxxxxxx-x")
            return False

        if not branch:
            self.show_error_message("Please enter branch.")
            return False

        if not self.is_valid_branch(branch):
            self.show_error_message(
                "Invalid branch format. Branch should be 4 digits.")
            return False

        return True

    def get_transfer_data(self):
        amount = self.amount_input.text()
        recipient_account = self.recipient_input.text()
        branch = self.branch_input.text()
        return amount, recipient_account, branch

    def set_controller(self, controller):
        self.controller = controller
