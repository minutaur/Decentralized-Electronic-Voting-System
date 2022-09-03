from PyQt5.QtWidgets import *
import sys


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.text_lable = QLabel()

        self.list = QListWidget()
        self.list.addItem('아이템1')
        self.list.addItem('아이템2')
        self.list.clicked.connect(self.select_item)

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.text_lable)
        self.hbox_layout.addWidget(self.list)

        self.setLayout(self.hbox_layout)

    def select_item(self):
        item = self.list.currentItem()
        self.text_lable.setText(item.text())


def exception_hook(exept_type, value, traceback):
    print(exept_type, value, traceback)
    exit(1)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())
