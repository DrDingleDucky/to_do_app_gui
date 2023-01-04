import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # self.setGeometry(20, 50, 800, 500)  # Window Size
        self.setWindowTitle("Python")  # Window Title
        self.setWindowIcon(QIcon("icon/icon.png"))  # Window Icon
        # self.setMinimumSize(500, 300)  # The window's smallest possible size.

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.lable_1 = QLabel("Username")
        self.layout.addWidget(self.lable_1, 0, 0)

        self.lable_2 = QLabel("Email")
        self.layout.addWidget(self.lable_2, 1, 0)

        self.input_1 = QLineEdit()
        self.layout.addWidget(self.input_1, 0, 1)

        self.input_2 = QLineEdit()
        self.layout.addWidget(self.input_2, 1, 1)

        self.button = QPushButton("Sign In")
        self.button.clicked.connect(self.display)
        self.layout.addWidget(self.button, 2, 1)

    def display(self):
        print(self.input_2.text())
        print(self.input_2.text())


def main():
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec())  # Make sure the programme terminates properly.


if __name__ == "__main__":
    main()
