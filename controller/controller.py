from view.loading_view import LoadingView


class ScreenController:
    def __init__(self, app):
        # Constructor for the ScreenController class. It receives an instance of QApplication as an argument.
        self.app = app

    def show_loading_view(self):
        # Method to display the loading view.

        # Create an instance of the LoadingView class.
        self.loading_view = LoadingView()

        # Show the loading view, making it visible to the user.
        self.loading_view.show()
