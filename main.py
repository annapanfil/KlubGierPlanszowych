from Main_app import Ui_MainWindow
from connection import MyConnection
from ekran_gui import Ui_EkranLogowania
from tables import *
import logging
from PyQt5 import QtCore, QtGui, QtWidgets
import sys



def create_connection():
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_EkranLogowania()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    app.exec_()
    connection = ui.get_connection()

    return connection


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    connection = create_connection()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.addConnection(connection)
    MainWindow.show()
    sys.exit(app.exec_())
