from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout, QWidget

from view.base_view import BaseView


class HomeView(BaseView):
    def __init__(self):
        super().__init__()

        # Crie uma QWidget principal para conter todos os elementos da tela
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Configure o layout principal da tela
        layout = QHBoxLayout()
        # Defina todas as margens para 0
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        central_widget.setLayout(layout)

        ################################### left box ################################################

        left_box = QFrame()
        left_box.setFixedWidth(136)
        left_box.setStyleSheet("background-color: rgba(255, 255, 255, 0.0);")

        layout.addWidget(left_box)

        style_text_label = "background: none; border: none; color: #c9a9a8; font-size: 15px;"

        text_label = QLabel("DarkStar Bank", left_box)
        text_label.setStyleSheet(style_text_label)
        text_label.adjustSize()
        title_width = text_label.width()
        text_label.move((136 - title_width) // 2, 40)

        ################################### center box ################################################
        # styleSheet_box = "background-color: none; color: #c9a9a8;border-color: #c9a9a8; border-radius: 20px; padding-left: 10px;"
        styleSheet_box = "border: 1px solid #c9a9a8; border-radius: 20px; padding-left: 10px;"

        central_box = QFrame()
        central_box.setFixedWidth(794)
        central_box.setFixedHeight(746)
        central_box.setStyleSheet(styleSheet_box)
        layout.addWidget(central_box)

        ################################## right box #################################################

        right_box = QFrame()
        right_box.setFixedWidth(390)
        right_box.setFixedHeight(746)
        right_box.setStyleSheet(styleSheet_box)

        layout.addWidget(right_box)
        ###################################################################################
