from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QCursor, QIcon, QPixmap
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton, QWidget

from view.base_view import BaseView


class HomeView(BaseView):
    def __init__(self, user_id, first_name, last_name):
        super().__init__()

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
        home_btn = QPushButton("Logout", left_box)
        icon = QIcon("resources/img/icon/icons8-logout-30.png")
        home_btn.setGeometry(25, 600, 150, 30)
        home_btn.setIcon(icon)
        home_btn.setStyleSheet(style_home_btn)
        home_btn.setCursor(PointingHandCursor)

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
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFixedWidth(80)
        label.setFixedHeight(80)
        label.setGeometry(20, 20, 80, 80)
        label.setStyleSheet("border-radius: 40px; background-color: white; ")

        nome = f"{first_name} {last_name}"
        welcome_text = f"Welcome, {nome}"
        welcome = QLabel(welcome_text, central_box)
        welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome.setGeometry(120, 50, 300, 30)
        welcome.setStyleSheet("color: #c9a9a8; font-size: 20px;")

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
        ###################################################################################
