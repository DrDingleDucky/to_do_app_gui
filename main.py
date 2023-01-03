import sys

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 500)
        self.setWindowTitle("Python")
        self.setWindowIcon(QIcon("icon/icon.png"))
        self.setMinimumSize(500, 300)


def main():
    app = QApplication([])

    window = Window()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
