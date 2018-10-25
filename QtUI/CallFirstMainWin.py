#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : CallFirstMainWin.py
# Author: roohom
# Date  : 2018/10/25 0025

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from firstMainWin import *


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUI(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())