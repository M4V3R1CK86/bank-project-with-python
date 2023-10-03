import re

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QCursor, QIcon, QPixmap
from PyQt6.QtWidgets import (QDialog, QFrame, QHBoxLayout, QLabel, QMessageBox,
                             QPushButton, QWidget)

from view.base_view import BaseView
from view.transfer_dialog_view import TransferDialog


class HomeView(BaseView):
    def __init__(self, user_id, first_name, last_name, account_data):
        super().__init__()
        self.user_id = user_id
        self.balance = float(account_data[4]) if account_data else 0.0
        # Crie uma QWidget principal para conter todos os elementos da tela
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Configure o layout principal da tela
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        central_widget.setLayout(layout)
        PointingHandCursor = QCursor(Qt.CursorShape.PointingHandCursor)

        ################################### left box ################################################

        left_box = QFrame()
        left_box.setFixedWidth(200)
        left_box.setStyleSheet(
            "background-color: none ; padding-left: 0px;")
        style_text_label = "background: none; border: none; color: #c9a9a8; font-size: 20px;"

        text_label = QLabel("DarkStar Bank", left_box)
        text_label.setStyleSheet(style_text_label)
        text_label.adjustSize()
        title_width = text_label.width()
        text_label.move((200 - title_width) // 2, 50)

        style_home_btn = "color: #c9a9a8; font-size: 14px; margin-left: 0px; background-color: transparent;"

        # home_btn
        home_btn = QPushButton("    Home", left_box)
        icon = QIcon("resources/img/icon/icons8-home-30.png")
        home_btn.setGeometry(19, 200, 150, 30)
        home_btn.setIcon(icon)
        home_btn.setStyleSheet(style_home_btn)
        home_btn.setCursor(PointingHandCursor)

        # home_btn
        home_btn = QPushButton("    Home", left_box)
        icon = QIcon("resources/img/icon/icons8-home-30.png")
        home_btn.setGeometry(19, 250, 150, 30)
        home_btn.setIcon(icon)
        home_btn.setStyleSheet(style_home_btn)
        home_btn.setCursor(PointingHandCursor)

        # home_btn
        home_btn = QPushButton("    Settings", left_box)
        icon = QIcon("resources/img/icon/icons8-home-30.png")
        home_btn.setGeometry(25, 300, 150, 30)
        home_btn.setIcon(icon)
        home_btn.setStyleSheet(style_home_btn)
        home_btn.setCursor(PointingHandCursor)

        # home_btn
        logout_btn = QPushButton("Logout", left_box)
        logou_icon = QIcon("resources/img/icon/icons8-logout-30.png")
        logout_btn.setGeometry(25, 600, 150, 30)
        logout_btn.setIcon(logou_icon)
        logout_btn.setStyleSheet(style_home_btn)
        logout_btn.setCursor(PointingHandCursor)
        logout_btn.clicked.connect(self.go_back_to_login)

        layout.addWidget(left_box)

        # Adicione uma linha vertical
        line = QFrame()
        line.setFrameShape(QFrame.Shape.VLine)
        line.setLineWidth(1)
        line.setStyleSheet("color: #493837;")

        layout.addWidget(line)

        ################################### center box ################################################
        # styleSheet_box = "background-color: none; color: #c9a9a8;border-color: #c9a9a8; border-radius: 20px; padding-left: 10px;"
        styleSheet_box = "border: 0px solid #c9a9a8; border-radius: 20px; "
        # styleSheet_box2 = "background-color: #493837 ; border-radius: 00px; padding-left: 10px;"

        central_box = QFrame()
        central_box.setFixedWidth(730)
        central_box.setFixedHeight(746)
        # central_box.setStyleSheet("background-color: none ;")
        layout.addWidget(central_box)

        # Adiciona uma imagem circular (substitua pelo caminho da sua imagem)
        pixmap = QPixmap("resources/img/eu.jpg")
        label = QLabel(central_box)
        # label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # label.setFixedWidth(80)
        # label.setFixedHeight(80)
        label.setGeometry(20, 20, 80, 80)
        label.setStyleSheet(
            "border-radius: 40px; background-color: none; border: 3px solid #c9a9a8; ")

        nome = f"{first_name} {last_name}"
        welcome_text = f"Welcome, {nome}"
        welcome = QLabel(welcome_text, central_box)
        welcome.setAlignment(Qt.AlignmentFlag.AlignLeft)
        welcome.setGeometry(110, 50, 300, 30)
        welcome.setStyleSheet("color: #c9a9a8; font-size: 20px;")

        self.balance_text = (f"Balance: {self.balance:.2f} USD")
        self.label_balance = QLabel(self.balance_text, central_box)
        self.label_balance.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.label_balance.setGeometry(20, 120, 320, 30)
        self.label_balance.setStyleSheet("color: #c9a9a8; font-size: 20px;")

        chart = QFrame(central_box)
        chart.setGeometry(20, 170, 690, 220)
        chart.setStyleSheet(
            "border-radius: 40px; background-color: none; border: 3px solid #c9a9a8; ")
        # transfer_btn
        transfer_icon = QIcon("resources/img/icon/transfer.png")
        transfer_btn = QPushButton("Transfer", central_box)
        transfer_btn.setGeometry(21, 420, 152, 200)
        transfer_btn.setIcon(transfer_icon)
        transfer_btn.setStyleSheet("""
            border-radius: 40px;
            background-color: none;
            border: 3px solid #c9a9a8;
            color: #c9a9a8;
            font-size: 14px;
            margin-left: 0px;
            background-color: transparent;
            text-align: left; /* Alinha o texto e o ícone à esquerda */
            padding-left: 40px; /* Espaçamento à esquerda para o ícone */
        """)
        transfer_btn.setCursor(PointingHandCursor)
        transfer_btn.setFlat(True)

        def enter_event(event):
            transfer_btn.setStyleSheet("""
                border-radius: 40px;
                background-color: #fff;  /* Cor de fundo ao passar o mouse */
                border: 3px solid #fea509;
                color: #fff;  /* Cor do texto ao passar o mouse */
                font-size: 14px;
                margin-left: 0px;
                background-color: transparent;
                text-align: left;
                padding-left: 40px;
            """)

        def leave_event(event):
            transfer_btn.setStyleSheet("""
                border-radius: 40px;
                background-color: none;
                border: 3px solid #c9a9aD;
                color: #c9a9a8;
                font-size: 14px;
                margin-left: 0px;
                background-color: transparent;
                text-align: left;
                padding-left: 40px;
            """)

        transfer_btn.enterEvent = enter_event
        transfer_btn.leaveEvent = leave_event

        # Connect the "Transfer" button click event to the transfer function
        # transfer_btn.clicked.connect(self.show_transfer_dialog)
        # transfer_btn.clicked.connect(self.on_show_transfer_dialog_btn)
        # transfer_btn.clicked.connect(lambda: self.on_show_transfer_dialog_btn(balance))

        transfer_btn.clicked.connect(
            lambda: self.on_show_transfer_dialog_btn(self.balance))

       # deposit_btn
        deposit_icon = QIcon("resources/img/icon/deposit.png")
        deposit_btn = QPushButton("Deposit", central_box)
        deposit_btn.setGeometry(193, 420, 152, 200)
        deposit_btn.setIcon(deposit_icon)
        deposit_btn.setStyleSheet("""
            border-radius: 40px;
            background-color: none;
            border: 3px solid #c9a9a8;
            color: #c9a9a8;
            font-size: 14px;
            margin-left: 0px;
            background-color: transparent;
            text-align: left; /* Alinha o texto e o ícone à esquerda */
            padding-left: 40px; /* Espaçamento à esquerda para o ícone */
        """)
        deposit_btn.setCursor(PointingHandCursor)
        deposit_btn.setFlat(True)

        def enter_event(event):
            deposit_btn.setStyleSheet("""
                border-radius: 40px;
                background-color: #fff;  /* Cor de fundo ao passar o mouse */
                border: 3px solid #fea509;
                color: #fff;  /* Cor do texto ao passar o mouse */
                font-size: 14px;
                margin-left: 0px;
                background-color: transparent;
                text-align: left;
                padding-left: 40px;
            """)

        def leave_event(event):
            deposit_btn.setStyleSheet("""
                border-radius: 40px;
                background-color: none;
                border: 3px solid #c9a9aD;
                color: #c9a9a8;
                font-size: 14px;
                margin-left: 0px;
                background-color: transparent;
                text-align: left;
                padding-left: 40px;
            """)

        deposit_btn.enterEvent = enter_event
        deposit_btn.leaveEvent = leave_event

        # bill_btn
        bill_icon = QIcon("resources/img/icon/bill.png")
        bill_btn = QPushButton("Bill Payment", central_box)
        bill_btn.setGeometry(365, 420, 152, 200)
        bill_btn.setIcon(bill_icon)
        bill_btn.setStyleSheet("""
            border-radius: 40px;
            background-color: none;
            border: 3px solid #c9a9a8;
            color: #c9a9a8;
            font-size: 14px;
            margin-left: 0px;
            background-color: transparent;
            text-align: left; /* Alinha o texto e o ícone à esquerda */
            padding-left: 40px; /* Espaçamento à esquerda para o ícone */
        """)
        bill_btn.setCursor(PointingHandCursor)
        bill_btn.setFlat(True)

        def enter_event(event):
            bill_btn.setStyleSheet("""
                border-radius: 40px;
                background-color: #fff;  /* Cor de fundo ao passar o mouse */
                border: 3px solid #fea509;
                color: #fff;  /* Cor do texto ao passar o mouse */
                font-size: 14px;
                margin-left: 0px;
                background-color: transparent;
                text-align: left;
                padding-left: 40px;
            """)

        def leave_event(event):
            bill_btn.setStyleSheet("""
                border-radius: 40px;
                background-color: none;
                border: 3px solid #c9a9aD;
                color: #c9a9a8;
                font-size: 14px;
                margin-left: 0px;
                background-color: transparent;
                text-align: left;
                padding-left: 40px;
            """)

        bill_btn.enterEvent = enter_event
        bill_btn.leaveEvent = leave_event

        # loan_btn
        loan_icon = QIcon("resources/img/icon/loan.png")
        loan_btn = QPushButton("Loan", central_box)
        loan_btn.setGeometry(538, 420, 152, 200)
        loan_btn.setIcon(loan_icon)
        loan_btn.setStyleSheet("""
            border-radius: 40px;
            background-color: none;
            border: 3px solid #c9a9a8;
            color: #c9a9a8;
            font-size: 14px;
            margin-left: 0px;
            background-color: transparent;
            text-align: left; /* Alinha o texto e o ícone à esquerda */
            padding-left: 40px; /* Espaçamento à esquerda para o ícone */
        """)
        loan_btn.setCursor(PointingHandCursor)
        loan_btn.setFlat(True)

        def enter_event(event):
            loan_btn.setStyleSheet("""
                border-radius: 40px;
                background-color: #fff;  /* Cor de fundo ao passar o mouse */
                border: 3px solid #fea509;
                color: #fff;  /* Cor do texto ao passar o mouse */
                font-size: 14px;
                margin-left: 0px;
                background-color: transparent;
                text-align: left;
                padding-left: 40px;
            """)

        def leave_event(event):
            loan_btn.setStyleSheet("""
                border-radius: 40px;
                background-color: none;
                border: 3px solid #c9a9aD;
                color: #c9a9a8;
                font-size: 14px;
                margin-left: 0px;
                background-color: transparent;
                text-align: left;
                padding-left: 40px;
            """)

        loan_btn.enterEvent = enter_event
        loan_btn.leaveEvent = leave_event

        # Adicione uma linha vertical
        line = QFrame()
        line.setFrameShape(QFrame.Shape.VLine)
        line.setLineWidth(1)
        line.setStyleSheet("color: #493837;")

        layout.addWidget(line)

        ################################## right box #################################################

        right_box = QFrame()
        right_box.setFixedWidth(390)
        right_box.setFixedHeight(750)
        right_box.setStyleSheet(styleSheet_box)

        layout.addWidget(right_box)

        credit_card = QFrame(right_box)
        credit_card.setGeometry(20, 40, 350, 218)
        credit_card.setStyleSheet(
            "border-radius: 40px; background-color: none; border: 3px solid #c9a9a8; ")
        ###################################################################################

    def set_controller(self, controller):
        self.controller = controller

    def go_back_to_login(self):
        self.close()
        if self.controller:
            self.controller.show_login_view()

    def on_show_transfer_dialog_btn(self, balance):
        # Crie e exiba a caixa de diálogo de transferência
        if self.controller:
            self.controller.show_transfer_dialog_view(self.user_id, balance)

    def update_balance(self, new_balance):
        self.balance = new_balance
        self.label_balance.setText(f"Saldo: {self.balance:.2f} BRL")
