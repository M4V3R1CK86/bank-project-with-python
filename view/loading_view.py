from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QLabel

from view.base_view import BaseView


class LoadingView(BaseView):
    def __init__(self):
        super().__init__()

        # Create a QLabel for the title "DarkStar Bank" and set its style.
        title_label = QLabel("DarkStar Bank", self)
        title_label.setStyleSheet("color: #c9a9a8; font-size: 50px;")

        # Adjust the size of the title_label to fit the text.
        title_label.adjustSize()

        # Calculate the vertical position to center the title label.
        label_y = (self.height() - title_label.height()) // 2

        # Set the position of the title label to center it both horizontally and vertically.
        title_label.move((self.width() - title_label.width()) // 2, label_y)
        # Create a QMovie for the loading animation.
        loading_gif = QMovie('resources/img/gif/Spinner-1s-48px.gif')

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
