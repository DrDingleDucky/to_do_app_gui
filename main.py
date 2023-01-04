import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QApplication, QCheckBox, QGridLayout,
                             QLineEdit, QPushButton, QWidget)


class Box:
    def __init__(self, layout, row):
        self.layout = layout
        self.row = row

        self.checkbox = QCheckBox()
        self.layout.addWidget(self.checkbox, self.row, 0)

        self.input = QLineEdit()
        self.layout.addWidget(self.input, self.row, 1)

        self.button = QPushButton("X")
        self.button.clicked.connect(lambda: self.deleat())
        self.layout.addWidget(self.button, self.row, 2)

    def deleat(self):
        self.checkbox.hide()
        self.input.hide()
        self.button.hide()


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.row_index = 5  # Keep a record of the row.

        self.setWindowTitle("To Do")  # Window Title
        self.setWindowIcon(QIcon("icon/icon.png"))  # Window Icon
        self.setMinimumSize(450, 250)  # The window's smallest possible size.

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        Box(self.layout, 0)
        Box(self.layout, 1)
        Box(self.layout, 2)
        Box(self.layout, 3)
        Box(self.layout, 4)
        Box(self.layout, 5)

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add)
        self.layout.addWidget(self.add_button, 5, 1)

    def add(self):
        self.row_index += 1

        Box(self.layout, self.row_index)
        self.layout.addWidget(self.add_button, self.row_index + 1, 1)


def main():
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec())  # Make sure the programme terminates properly.


if __name__ == "__main__":
    main()
