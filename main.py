from PyQt5.QtWidgets import *


def main():

    app = QApplication([])    # Creating app with an empty list
    window = QWidget()      # Creating app window
    # Create a new Label widget and set its text to "Hello world"
    label1 = QLabel(window)
    label1.setText("Hello World")
    # putting the window running
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
