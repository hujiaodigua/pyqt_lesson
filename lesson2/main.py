# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import sys


from PyQt5.QtWidgets import QApplication , QMainWindow
from PushButton import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())