from PyQt6.QtGui import QIcon, QMovie
from PyQt6.QtWidgets import QLabel, QMainWindow


class LoadingView(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title.
        self.setWindowTitle("DarkStar Bank!")

        # Set the fixed size for the window.
        self.setFixedSize(1334, 750)

        # Set the background color of the window.
        self.setStyleSheet('background-color:#fe2757')

        # Set the window icon.
        self.setWindowIcon(QIcon('resources/img/icon/aviation.png'))

        # Get the screen's available geometry (size and position).
        screen_geo = self.screen().availableGeometry()

        # Calculate the x and y coordinates to center the window on the screen.
        x = (screen_geo.width() - self.width()) // 2
        y = (screen_geo.height() - self.height()) // 2

        # Move the window to the calculated position, centering it on the screen.
        self.move(x, y)

        # Create a QLabel for the title "DarkStar Bank" and set its style.
        title_label = QLabel("DarkStar Bank", self)
        title_label.setStyleSheet("color: #eec1c0; font-size: 50px;")

        # Adjust the size of the title_label to fit the text.
        title_label.adjustSize()

        # Calculate the vertical position to center the title label.
        label_y = (self.height() - title_label.height()) // 2

        # Set the position of the title label to center it both horizontally and vertically.
        title_label.move((self.width() - title_label.width()) // 2, label_y)

        # Create a QMovie for the loading animation.
        loading_gif = QMovie('resources/img/gif/spinner.gif')

        # Create a QLabel to display the loading animation.
        loading_label = QLabel(self)

        # Set the movie (animation) for the loading label and start the animation.
        loading_label.setMovie(loading_gif)
        loading_gif.start()

        # Calculate the vertical position to place the loading label below the title label.
        loading_y = label_y + title_label.height() + 20

        # Set the position of the loading label to center it horizontally.
        loading_label.move(
            (self.width() - loading_gif.frameRect().width()) // 2, loading_y)
