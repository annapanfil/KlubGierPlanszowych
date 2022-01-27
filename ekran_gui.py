from connection import MyConnection
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EkranLogowania(object):
    def setupUi(self, EkranLogowania):
        EkranLogowania.setObjectName("EkranLogowania")
        EkranLogowania.resize(256, 295)
        self.centralwidget = QtWidgets.QWidget(EkranLogowania)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_adres = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_adres.setObjectName("lineEdit_adres")
        self.verticalLayout.addWidget(self.lineEdit_adres)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_nazwa_uzytkownika = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nazwa_uzytkownika.setObjectName("lineEdit_nazwa_uzytkownika")
        self.verticalLayout.addWidget(self.lineEdit_nazwa_uzytkownika)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_haslo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_haslo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_haslo.setObjectName("lineEdit_haslo")
        self.verticalLayout.addWidget(self.lineEdit_haslo)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_3.raise_()
        self.lineEdit_nazwa_uzytkownika.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit_haslo.raise_()
        self.pushButton.raise_()
        self.lineEdit_adres.raise_()
        EkranLogowania.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EkranLogowania)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 256, 21))
        self.menubar.setObjectName("menubar")
        EkranLogowania.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EkranLogowania)
        self.statusbar.setObjectName("statusbar")
        EkranLogowania.setStatusBar(self.statusbar)

        self.window = EkranLogowania
        self.retranslateUi(EkranLogowania)
        QtCore.QMetaObject.connectSlotsByName(EkranLogowania)
        self.setupUi_my()

    def retranslateUi(self, EkranLogowania):
        _translate = QtCore.QCoreApplication.translate
        EkranLogowania.setWindowTitle(_translate("EkranLogowania", "MainWindow"))
        self.label_3.setText(_translate("EkranLogowania", "Adres IP"))
        self.lineEdit_adres.setText(_translate("EkranLogowania", "localhost"))
        self.label.setText(_translate("EkranLogowania", "Nazwa użytkownika"))
        self.lineEdit_nazwa_uzytkownika.setText(_translate("EkranLogowania", "anna"))
        self.label_2.setText(_translate("EkranLogowania", "Hasło"))
        self.pushButton.setText(_translate("EkranLogowania", "Połącz"))

    def setupUi_my(self):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = None

    def button_fun(self):
        login = self.lineEdit_nazwa_uzytkownika.text()
        passwd = self.lineEdit_haslo.text()
        host = self.lineEdit_adres.text()

        self.connection = MyConnection(login, passwd, host)
        self.window.close()

    def get_connection(self):
        return self.connection
