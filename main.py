from PyQt6.QtWidgets import QApplication

from controller.controller import ScreenController

if __name__ == "__main__":

    # Create a QApplication instance, which is necessary to run a PyQt application.
    app = QApplication([])

    # Create an instance of the ScreenController class, passing the QApplication instance as an argument.
    controller = ScreenController(app)

    # Call the show_loading_view() method of the controller to display the loading view.
    controller.show_loading_view()
    # controller.show_home_view()

    # Start the application event loop using app.exec(). This keeps the application running until the user closes it.
    app.exec()
