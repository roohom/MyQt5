#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Qt01.py
# Author: roohom
# Date  : 2018/10/25 0025

import sys
from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("Hello PyQt5!")
widget.show()
sys.exit(app.exec_())