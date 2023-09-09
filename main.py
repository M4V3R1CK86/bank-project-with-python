from PyQt6.QtWidgets import QApplication

from controller.controller import ScreenController

if __name__ == "__main__":
    app = QApplication([])
    controller = ScreenController(app)
    controller.show_loading_view()
    app.exec()
