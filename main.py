import sys
import time
import random

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('猜数字')
        self.num = 0
        self.up = 100
        self.down = 0

        layout = QVBoxLayout()

        self.edit = QLineEdit(self)
        self.lb = QLabel('', self)
        self.btnStart = QPushButton('开始')
        self.btnOk = QPushButton('确定')

        layout.addWidget(self.edit)
        layout.addWidget(self.lb)
        layout.addWidget(self.btnStart)
        layout.addWidget(self.btnOk)

        self.btnOk.clicked.connect(self.ok)
        self.btnStart.clicked.connect(self.start)
        self.setLayout(layout)

        reg = QRegExp("[0-9]+$")
        p_validator = QRegExpValidator(self)
        p_validator.setRegExp(reg)
        self.edit.setValidator(p_validator)
        self.btnOk.hide()
        self.edit.setReadOnly(True)

    def ok(self):
        if self.edit.text().strip() == "":
            self.lb.setText("数字范围{}-{}，请输入".format(self.down, self.up))
            return
        s = int(self.edit.text().strip())
        if s == self.num:
            self.lb.setText("猜对了，游戏结束")
            self.edit.setText("")
            self.edit.setReadOnly(True)
            self.btnOk.hide()
            self.btnStart.show()
            self.up = 100
            self.down = 0
        elif s < self.down or s > self.up:
            self.lb.setText("数字范围{}-{}，请输入".format(self.down, self.up))
        elif s < self.num:
            self.down = s
            self.lb.setText("数字范围{}-{}，请输入".format(self.down, self.up))
        else:
            self.up = s
            self.lb.setText("数字范围{}-{}，请输入".format(self.down, self.up))

    def start(self):
        self.btnOk.show()
        self.btnStart.hide()
        self.edit.setReadOnly(False)
        self.num = random.randint(1, 99)
        self.lb.setText("数字范围{}-{}，请输入".format(self.down, self.up))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec())
