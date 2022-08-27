from PyQt5.QtWidgets import *
import sys


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.button1 = QPushButton('버튼1')
        self.button2 = QPushButton('버튼2')
        self.button3 = QPushButton('버튼3')

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.button1, 0, 0, 1, 2)
        self.grid_layout.addWidget(self.button2, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.button3, 1, 1, 1, 1)

        self.setLayout(self.grid_layout)

def exception_hook(exept_type, value, traceback):
    print(exept_type, value, traceback)
    exit(1)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())