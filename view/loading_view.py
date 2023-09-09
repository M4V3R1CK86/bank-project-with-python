from PyQt6.QtGui import QIcon, QMovie
from PyQt6.QtWidgets import QLabel, QMainWindow


class LoadingView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DarkStar Bank!")
        self.setFixedSize(1334, 750)
        self.setStyleSheet('background-color:#fe2757')
        self.setWindowIcon(QIcon('resources/img/icon/aviation.png'))

        screen_geo = self.screen().availableGeometry()
        x = (screen_geo.width() - self.width()) // 2
        y = (screen_geo.height() - self.height()) // 2
        self.move(x, y)

        title_label = QLabel("DarkStar Bank", self)
        title_label.setStyleSheet("color: #eec1c0; font-size: 50px;")
        title_label.adjustSize()
        label_y = (self.height() - title_label.height()) // 2
        title_label.move((self.width() - title_label.width()) // 2, label_y)

        loading_gif = QMovie('resources/img/gif/spinner.gif')

        loading_label = QLabel(self)
        loading_label.setMovie(loading_gif)
        loading_gif.start()

        loading_y = label_y + title_label.height() + 20
        loading_label.move(
            (self.width() - loading_gif.frameRect().width()) // 2, loading_y)
