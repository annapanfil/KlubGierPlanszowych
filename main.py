from Main_app import Ui_MainWindow
from connection import MyConnection
from tables import *
import logging
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    connection = MyConnection()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.addConnection(connection)
    MainWindow.show()
    sys.exit(app.exec_())
