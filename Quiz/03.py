from PyQt5.QtWidgets import *
import sys


class Tab1(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        # 레이아웃1======================================================
        self.layout_1 = QVBoxLayout()
        self.menu_button = QPushButton('투표조회')
        self.layout_1.addWidget(self.menu_button)
        # 레이아웃2======================================================
        self.votelist = QGroupBox('투표목록')
        self.layout_2 = QHBoxLayout()
        self.list = QListWidget()
        self.list.addItem('1')
        self.list.addItem('2')
        self.layout_2.addWidget(self.list)

        self.vote = QGroupBox('투표')

        # 레이아웃3======================================================
        self.layout_3 = QVBoxLayout()

        # =============================================================
        self.groupbox_1 = QGroupBox('메뉴')  # 메뉴
        self.groupbox_2 = QGroupBox()  # 투표목록
        self.groupbox_3 = QGroupBox('투표결과')  # 투표결과

        self.groupbox_1.setLayout(self.layout_1)
        self.groupbox_2.setLayout(self.layout_2)
        self.groupbox_3.setLayout(self.layout_3)

        self.layout_2.addWidget(self.votelist)
        self.layout_2.addWidget(self.vote)

        self.main_layout.addWidget(self.groupbox_1)
        self.main_layout.addWidget(self.groupbox_2)
        self.main_layout.addWidget(self.groupbox_3)
        self.setLayout(self.main_layout)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Tab2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.line_edit1 = QLineEdit()
        self.line_edit2 = QLineEdit()
        self.line_edit3 = QLineEdit()
        self.line_edit4 = QLineEdit()

        self.form_layout = QFormLayout()

        self.button1 = QPushButton('게시')
        self.button2 = QPushButton('초기화')
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.button1)
        self.hbox.addWidget(self.button2)

        self.grid_layout = QGridLayout()
        self.setLayout(self.form_layout)
        self.button1.clicked.connect(self.button1_click)
        self.button2.clicked.connect(self.button2_click)

        self.form_layout.addRow('질문:', self.line_edit1)
        self.form_layout.addRow('선택지:', self.line_edit2)
        self.form_layout.addRow('   ', self.line_edit3)
        self.form_layout.addRow('   ', self.line_edit4)
        self.form_layout.addRow(self.hbox)

        self.text_label = QLabel()

        self.vbox_layout = QVBoxLayout()

        self.vbox_layout.addWidget(self.text_label)
        self.setLayout(self.form_layout)

        self.form_layout = QFormLayout()
        self.line_edit = QLineEdit()

        self.form_layout.addRow('텍스트', self.line_edit)

    def button1_click(self):  # 게시
        pass

    def button2_click(self):  # 초기화
        pass


# ================================================================
class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('중앙전자투표시스템')

        self.tab1 = Tab1()
        self.tab2 = Tab2()

        self.tabs = QTabWidget()
        self.tabs.addTab(self.tab1, '투표')
        self.tabs.addTab(self.tab2, '투표생성')

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.tabs)

        self.setLayout(self.vbox_layout)


def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    exit(1)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())
