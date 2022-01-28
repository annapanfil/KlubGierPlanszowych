from PyQt5 import QtCore, QtGui, QtWidgets
from tables import *

class Ui_CreateSekcja(object):
    def setupUi(self, CreateSekcja, connection):
        CreateSekcja.setObjectName("CreateSekcja")
        CreateSekcja.resize(419, 174)
        self.lineEdit_nazwa = QtWidgets.QLineEdit(CreateSekcja)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(20, 90, 141, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.label = QtWidgets.QLabel(CreateSekcja)
        self.label.setGeometry(QtCore.QRect(30, 70, 47, 13))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(CreateSekcja)
        self.pushButton.setGeometry(QtCore.QRect(320, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(CreateSekcja)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 231, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(CreateSekcja)
        QtCore.QMetaObject.connectSlotsByName(CreateSekcja)

        self.window = CreateSekcja
        self.setupUi_my(connection)

    def retranslateUi(self, CreateSekcja):
        _translate = QtCore.QCoreApplication.translate
        CreateSekcja.setWindowTitle(_translate("CreateSekcja", "Dialog"))
        self.label.setText(_translate("CreateSekcja", "Nazwa"))
        self.pushButton.setText(_translate("CreateSekcja", "Utwórz"))
        self.label_2.setText(_translate("CreateSekcja", "Tworzysz nową sekcję"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection

    def button_fun(self):
        record = [self.lineEdit_nazwa.text()]
        add_record(self.connection, 0, record)
        self.window.close()

class Ui_AddCzlonek(object):
    def setupUi(self, AddCzlonek, connection):
        AddCzlonek.setObjectName("AddCzlonek")
        AddCzlonek.resize(574, 177)
        self.lineEdit_imie = QtWidgets.QLineEdit(AddCzlonek)
        self.lineEdit_imie.setGeometry(QtCore.QRect(30, 80, 113, 20))
        self.lineEdit_imie.setObjectName("lineEdit_imie")
        self.lineEdit_nazwisko = QtWidgets.QLineEdit(AddCzlonek)
        self.lineEdit_nazwisko.setGeometry(QtCore.QRect(160, 80, 113, 20))
        self.lineEdit_nazwisko.setObjectName("lineEdit_nazwisko")
        self.lineEdit_data_urodzenia = QtWidgets.QLineEdit(AddCzlonek)
        self.lineEdit_data_urodzenia.setGeometry(QtCore.QRect(290, 80, 113, 20))
        self.lineEdit_data_urodzenia.setObjectName("lineEdit_data_urodzenia")
        self.lineEdit_PESEL = QtWidgets.QLineEdit(AddCzlonek)
        self.lineEdit_PESEL.setGeometry(QtCore.QRect(420, 80, 113, 20))
        self.lineEdit_PESEL.setObjectName("lineEdit_PESEL")
        self.label = QtWidgets.QLabel(AddCzlonek)
        self.label.setGeometry(QtCore.QRect(50, 60, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddCzlonek)
        self.label_2.setGeometry(QtCore.QRect(170, 60, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddCzlonek)
        self.label_3.setGeometry(QtCore.QRect(300, 60, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AddCzlonek)
        self.label_4.setGeometry(QtCore.QRect(430, 60, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AddCzlonek)
        self.label_5.setGeometry(QtCore.QRect(220, 10, 171, 20))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(AddCzlonek)
        self.pushButton.setGeometry(QtCore.QRect(470, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(AddCzlonek)
        QtCore.QMetaObject.connectSlotsByName(AddCzlonek)
        self.AddCzlonek = AddCzlonek
        self.setupUi_my(connection)

    def retranslateUi(self, AddCzlonek):
        _translate = QtCore.QCoreApplication.translate
        AddCzlonek.setWindowTitle(_translate("AddCzlonek", "Dialog"))
        self.label.setText(_translate("AddCzlonek", "Imię"))
        self.label_2.setText(_translate("AddCzlonek", "Nazwisko"))
        self.label_3.setText(_translate("AddCzlonek", "Data Urodzenia"))
        self.label_4.setText(_translate("AddCzlonek", "PESEL"))
        self.label_5.setText(_translate("AddCzlonek", "Dodajesz Nowego członka"))
        self.pushButton.setText(_translate("AddCzlonek", "Dodaj"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection

    def button_fun(self):
        date = validate_date(self.lineEdit_data_urodzenia.text())
        pesel = validate_number(self.lineEdit_PESEL.text())

        if date is not None and pesel != None:
            record = [pesel, self.lineEdit_imie.text(), self.lineEdit_nazwisko.text()] #date
            add_record(self.connection, 1, record)
            self.AddCzlonek.close()

class Ui_AddSpotkanie(object):
    def setupUi(self, AddSpotkanie, connection):
        AddSpotkanie.setObjectName("AddSpotkanie")
        AddSpotkanie.resize(411, 149)
        self.label = QtWidgets.QLabel(AddSpotkanie)
        self.label.setGeometry(QtCore.QRect(150, 10, 111, 20))
        self.label.setObjectName("label")
        self.lineEdit_termin = QtWidgets.QLineEdit(AddSpotkanie)
        self.lineEdit_termin.setGeometry(QtCore.QRect(150, 60, 113, 20))
        self.lineEdit_termin.setObjectName("lineEdit_termin")
        self.label_2 = QtWidgets.QLabel(AddSpotkanie)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 47, 13))
        self.label_2.setObjectName("label_2")
        self.comboBox_sekcja = QtWidgets.QComboBox(AddSpotkanie)
        self.comboBox_sekcja.setGeometry(QtCore.QRect(20, 60, 111, 22))
        self.comboBox_sekcja.setObjectName("comboBox_sekcja")
        self.comboBox_miejsce = QtWidgets.QComboBox(AddSpotkanie)
        self.comboBox_miejsce.setGeometry(QtCore.QRect(280, 60, 111, 22))
        self.comboBox_miejsce.setObjectName("comboBox_miejsce")
        self.label_3 = QtWidgets.QLabel(AddSpotkanie)
        self.label_3.setGeometry(QtCore.QRect(290, 40, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AddSpotkanie)
        self.label_4.setGeometry(QtCore.QRect(160, 40, 47, 13))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(AddSpotkanie)
        self.pushButton.setGeometry(QtCore.QRect(320, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(AddSpotkanie)
        QtCore.QMetaObject.connectSlotsByName(AddSpotkanie)

        self.window = AddSpotkanie
        self.setupUi_my(connection)

    def retranslateUi(self, AddSpotkanie):
        _translate = QtCore.QCoreApplication.translate
        AddSpotkanie.setWindowTitle(_translate("AddSpotkanie", "Dialog"))
        self.label.setText(_translate("AddSpotkanie", "Dodajesz spotkanie"))
        self.label_2.setText(_translate("AddSpotkanie", "Sekcja:"))
        self.label_3.setText(_translate("AddSpotkanie", "Miejsce:"))
        self.label_4.setText(_translate("AddSpotkanie", "Termin"))
        self.pushButton.setText(_translate("AddSpotkanie", "Dodaj"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        sekcje = get_names(self.connection, 2, "nazwa")
        miejsca = get_names(self.connection, 2, "adres")
        self.comboBox_sekcja.addItems(sekcje)
        self.comboBox_miejsce.addItems(miejsca)

    def button_fun(self):
        termin = validate_date(self.lineEdit_termin.text())

        if termin is not None:
            record = [termin,
                    self.comboBox_sekcja.currentText(),
                    self.comboBox_miejsce.currentText()]
            add_record(self.connection, 2, record)
            self.window.close()

class Ui_AddPlacowka(object):
    def setupUi(self, AddPlacowka, connection):
        AddPlacowka.setObjectName("AddPlacowka")
        AddPlacowka.resize(400, 162)
        self.label = QtWidgets.QLabel(AddPlacowka)
        self.label.setGeometry(QtCore.QRect(116, 10, 151, 20))
        self.label.setObjectName("label")
        self.lineEdit_adres = QtWidgets.QLineEdit(AddPlacowka)
        self.lineEdit_adres.setGeometry(QtCore.QRect(20, 70, 113, 20))
        self.lineEdit_adres.setObjectName("lineEdit_adres")
        self.lineEdit_czynsz = QtWidgets.QLineEdit(AddPlacowka)
        self.lineEdit_czynsz.setGeometry(QtCore.QRect(150, 70, 113, 20))
        self.lineEdit_czynsz.setObjectName("lineEdit_czynsz")
        self.label_2 = QtWidgets.QLabel(AddPlacowka)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddPlacowka)
        self.label_3.setGeometry(QtCore.QRect(160, 50, 47, 13))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(AddPlacowka)
        self.pushButton.setGeometry(QtCore.QRect(300, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(AddPlacowka)
        QtCore.QMetaObject.connectSlotsByName(AddPlacowka)

        self.window = AddPlacowka
        self.setupUi_my(connection)

    def retranslateUi(self, AddPlacowka):
        _translate = QtCore.QCoreApplication.translate
        AddPlacowka.setWindowTitle(_translate("AddPlacowka", "Dialog"))
        self.label.setText(_translate("AddPlacowka", "Dodajesz Miejsce na spotkania"))
        self.label_2.setText(_translate("AddPlacowka", "Adres"))
        self.label_3.setText(_translate("AddPlacowka", "Czynsz"))
        self.pushButton.setText(_translate("AddPlacowka", "Dodaj"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection

    def button_fun(self):
        czynsz = validate_number(self.lineEdit_czynsz.text())

        if czynsz is not None:
            record = [self.lineEdit_adres.text(),
                    czynsz]
            add_record(self.connection, 3, record)
            self.window.close()

class Ui_AddEgzemplarz(object):
    def setupUi(self, AddEgzemplarz, connection):
        AddEgzemplarz.setObjectName("AddEgzemplarz")
        AddEgzemplarz.resize(400, 162)
        self.label = QtWidgets.QLabel(AddEgzemplarz)
        self.label.setGeometry(QtCore.QRect(140, 10, 141, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddEgzemplarz)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.comboBox_gra = QtWidgets.QComboBox(AddEgzemplarz)
        self.comboBox_gra.setGeometry(QtCore.QRect(30, 70, 101, 22))
        self.comboBox_gra.setObjectName("comboBox_gra")
        self.pushButton = QtWidgets.QPushButton(AddEgzemplarz)
        self.pushButton.setGeometry(QtCore.QRect(300, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_sekcja = QtWidgets.QComboBox(AddEgzemplarz)
        self.comboBox_sekcja.setGeometry(QtCore.QRect(268, 70, 101, 22))
        self.comboBox_sekcja.setObjectName("comboBox_sekcja")
        self.label_3 = QtWidgets.QLabel(AddEgzemplarz)
        self.label_3.setGeometry(QtCore.QRect(280, 50, 47, 13))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(AddEgzemplarz)
        QtCore.QMetaObject.connectSlotsByName(AddEgzemplarz)

        self.window = AddEgzemplarz
        self.setupUi_my(connection)

    def retranslateUi(self, AddEgzemplarz):
        _translate = QtCore.QCoreApplication.translate
        AddEgzemplarz.setWindowTitle(_translate("AddEgzemplarz", "Dialog"))
        self.label.setText(_translate("AddEgzemplarz", "Dodajesz egzemplarz"))
        self.label_2.setText(_translate("AddEgzemplarz", "Gra:"))
        self.pushButton.setText(_translate("AddEgzemplarz", "Dodaj"))
        self.label_3.setText(_translate("AddEgzemplarz", "Sekcja:"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection

        gry = get_names(connection, 15, "nazwa")
        sekcje = get_names(connection, 0, "nazwa")
        self.comboBox_sekcja.addItems(sekcje)
        self.comboBox_gra.addItems(gry)

    def button_fun(self):
        record = [self.comboBox_gra.currentText(),
                 self.comboBox_sekcja.currentText()]
        add_record(self.connection, 4, record)
        self.window.close()

class Ui_AddGraKomputerowa(object):
    def setupUi(self, AddGraKomputerowa, connection):
        AddGraKomputerowa.setObjectName("AddGraKomputerowa")
        AddGraKomputerowa.resize(485, 163)
        self.label = QtWidgets.QLabel(AddGraKomputerowa)
        self.label.setGeometry(QtCore.QRect(180, 10, 151, 16))
        self.label.setObjectName("label")
        self.lineEdit_nazwa = QtWidgets.QLineEdit(AddGraKomputerowa)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(20, 70, 113, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.comboBox_platforma = QtWidgets.QComboBox(AddGraKomputerowa)
        self.comboBox_platforma.setGeometry(QtCore.QRect(240, 70, 101, 22))
        self.comboBox_platforma.setObjectName("comboBox_platforma")
        self.lineEdit_cena = QtWidgets.QLineEdit(AddGraKomputerowa)
        self.lineEdit_cena.setGeometry(QtCore.QRect(150, 70, 71, 20))
        self.lineEdit_cena.setObjectName("lineEdit_cena")
        self.comboBox_wydawca = QtWidgets.QComboBox(AddGraKomputerowa)
        self.comboBox_wydawca.setGeometry(QtCore.QRect(360, 70, 101, 22))
        self.comboBox_wydawca.setObjectName("comboBox_wydawca")
        self.label_2 = QtWidgets.QLabel(AddGraKomputerowa)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddGraKomputerowa)
        self.label_3.setGeometry(QtCore.QRect(160, 50, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AddGraKomputerowa)
        self.label_4.setGeometry(QtCore.QRect(250, 50, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AddGraKomputerowa)
        self.label_5.setGeometry(QtCore.QRect(370, 50, 61, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(AddGraKomputerowa)
        self.pushButton.setGeometry(QtCore.QRect(390, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(AddGraKomputerowa)
        QtCore.QMetaObject.connectSlotsByName(AddGraKomputerowa)

        self.window = AddGraKomputerowa
        self.setupUi_my(connection)

    def retranslateUi(self, AddGraKomputerowa):
        _translate = QtCore.QCoreApplication.translate
        AddGraKomputerowa.setWindowTitle(_translate("AddGraKomputerowa", "Dialog"))
        self.label.setText(_translate("AddGraKomputerowa", "Dodajesz grę komputerową"))
        self.label_2.setText(_translate("AddGraKomputerowa", "Nazwa"))
        self.label_3.setText(_translate("AddGraKomputerowa", "Cena"))
        self.label_4.setText(_translate("AddGraKomputerowa", "Platforma:"))
        self.label_5.setText(_translate("AddGraKomputerowa", "Wydawca:"))
        self.pushButton.setText(_translate("AddGraKomputerowa", "Dodaj"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        wydawcy = get_names(connection, 8, "wydawca")
        platformy = get_names(connection, 7, "platforma")
        self.comboBox_platforma.addItems(platformy)
        self.comboBox_wydawca.addItems(wydawcy)

    def button_fun(self):
        cena = validate_number(self.lineEdit_cena.text())

        if cena is not None:
            record = [self.lineEdit_nazwa.text(),
                    cena,
                    self.comboBox_wydawca.currentText(),
                    self.comboBox_platforma.currentText()]
            add_record(self.connection, 5, record)
            self.window.close()

class Ui_AddGraPlanszowa(object):
    def setupUi(self, AddGraPlanszowa, connection):
        AddGraPlanszowa.setObjectName("AddGraPlanszowa")
        AddGraPlanszowa.resize(666, 160)
        self.label = QtWidgets.QLabel(AddGraPlanszowa)
        self.label.setGeometry(QtCore.QRect(260, 10, 241, 16))
        self.label.setObjectName("label")
        self.lineEdit_nazwa = QtWidgets.QLineEdit(AddGraPlanszowa)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(20, 70, 113, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.lineEdit_cena = QtWidgets.QLineEdit(AddGraPlanszowa)
        self.lineEdit_cena.setGeometry(QtCore.QRect(150, 70, 71, 20))
        self.lineEdit_cena.setObjectName("lineEdit_cena")
        self.comboBox_wydawca = QtWidgets.QComboBox(AddGraPlanszowa)
        self.comboBox_wydawca.setGeometry(QtCore.QRect(240, 70, 101, 22))
        self.comboBox_wydawca.setObjectName("comboBox_wydawca")
        self.lineEdit_maks_graczy = QtWidgets.QLineEdit(AddGraPlanszowa)
        self.lineEdit_maks_graczy.setGeometry(QtCore.QRect(460, 80, 81, 20))
        self.lineEdit_maks_graczy.setObjectName("lineEdit_maks_graczy")
        self.lineEdit_min_graczy = QtWidgets.QLineEdit(AddGraPlanszowa)
        self.lineEdit_min_graczy.setGeometry(QtCore.QRect(560, 80, 81, 20))
        self.lineEdit_min_graczy.setObjectName("lineEdit_min_graczy")
        self.lineEdit_waga = QtWidgets.QLineEdit(AddGraPlanszowa)
        self.lineEdit_waga.setGeometry(QtCore.QRect(360, 70, 81, 20))
        self.lineEdit_waga.setObjectName("lineEdit_waga")
        self.label_2 = QtWidgets.QLabel(AddGraPlanszowa)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddGraPlanszowa)
        self.label_3.setGeometry(QtCore.QRect(160, 50, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AddGraPlanszowa)
        self.label_4.setGeometry(QtCore.QRect(250, 50, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AddGraPlanszowa)
        self.label_5.setGeometry(QtCore.QRect(370, 50, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(AddGraPlanszowa)
        self.label_6.setGeometry(QtCore.QRect(470, 60, 47, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(AddGraPlanszowa)
        self.label_7.setGeometry(QtCore.QRect(570, 60, 51, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(AddGraPlanszowa)
        self.label_8.setGeometry(QtCore.QRect(470, 40, 91, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(AddGraPlanszowa)
        self.pushButton.setGeometry(QtCore.QRect(570, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(AddGraPlanszowa)
        QtCore.QMetaObject.connectSlotsByName(AddGraPlanszowa)

        self.window = AddGraPlanszowa
        self.setupUi_my(connection)

    def retranslateUi(self, AddGraPlanszowa):
        _translate = QtCore.QCoreApplication.translate
        AddGraPlanszowa.setWindowTitle(_translate("AddGraPlanszowa", "Dialog"))
        self.label.setText(_translate("AddGraPlanszowa", "Dodajesz gre planszową"))
        self.label_2.setText(_translate("AddGraPlanszowa", "Nazwa"))
        self.label_3.setText(_translate("AddGraPlanszowa", "Cena"))
        self.label_4.setText(_translate("AddGraPlanszowa", "Wydawca:"))
        self.label_5.setText(_translate("AddGraPlanszowa", "Waga"))
        self.label_6.setText(_translate("AddGraPlanszowa", "Maks."))
        self.label_7.setText(_translate("AddGraPlanszowa", "Min."))
        self.label_8.setText(_translate("AddGraPlanszowa", "Liczba Graczy:"))
        self.pushButton.setText(_translate("AddGraPlanszowa", "Dodaj"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        wydawcy = get_names(connection, 8, "wydawca")
        self.comboBox_wydawca.addItems(wydawcy)

    def button_fun(self):
        cena = validate_number(self.lineEdit_cena.text())
        waga = validate_number(self.lineEdit_waga.text())
        max_graczy = validate_number(self.lineEdit_maks_graczy.text())
        min_graczy = validate_number(self.lineEdit_min_graczy.text())

        if None not in [cena, waga, max_graczy, min_graczy]:
            record = [self.lineEdit_nazwa.text(),
                     cena,
                     self.comboBox_wydawca.currentText(),
                     waga,
                     min_graczy,
                     max_graczy]
            add_record(self.connection, 6, record)
            self.window.close()

class Ui_AddPlatforma(object):
    def setupUi(self, AddPlatforma, connection):
        AddPlatforma.setObjectName("AddPlatforma")
        AddPlatforma.resize(400, 130)
        self.lineEdit_nazwa = QtWidgets.QLineEdit(AddPlatforma)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(30, 60, 113, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.label = QtWidgets.QLabel(AddPlatforma)
        self.label.setGeometry(QtCore.QRect(40, 40, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddPlatforma)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 121, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(AddPlatforma)
        self.pushButton.setGeometry(QtCore.QRect(300, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(AddPlatforma)
        QtCore.QMetaObject.connectSlotsByName(AddPlatforma)

        self.window = AddPlatforma
        self.setupUi_my(connection)

    def retranslateUi(self, AddPlatforma):
        _translate = QtCore.QCoreApplication.translate
        AddPlatforma.setWindowTitle(_translate("AddPlatforma", "Dialog"))
        self.label.setText(_translate("AddPlatforma", "Nazwa:"))
        self.label_2.setText(_translate("AddPlatforma", "Dodajesz platformę"))
        self.pushButton.setText(_translate("AddPlatforma", "Dodaj"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection

    def button_fun(self):
        record = [self.lineEdit_nazwa.text()]
        add_record(self.connection, 7, record)
        self.window.close()

class Ui_AddWydawca(object):
    def setupUi(self, AddWydawca, connection):
        AddWydawca.setObjectName("AddWydawca")
        AddWydawca.resize(400, 130)
        self.lineEdit_nazwa = QtWidgets.QLineEdit(AddWydawca)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(30, 60, 113, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.label = QtWidgets.QLabel(AddWydawca)
        self.label.setGeometry(QtCore.QRect(40, 40, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddWydawca)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 121, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(AddWydawca)
        self.pushButton.setGeometry(QtCore.QRect(300, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(AddWydawca)
        QtCore.QMetaObject.connectSlotsByName(AddWydawca)
        self.window = AddWydawca
        self.setupUi_my(connection)

    def retranslateUi(self, AddWydawca):
        _translate = QtCore.QCoreApplication.translate
        AddWydawca.setWindowTitle(_translate("AddWydawca", "Dialog"))
        self.label.setText(_translate("AddWydawca", "Nazwa:"))
        self.label_2.setText(_translate("AddWydawca", "Dodajesz wydawcę"))
        self.pushButton.setText(_translate("AddWydawca", "Dodaj"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection

    def button_fun(self):
        record = [self.lineEdit_nazwa.text()]
        add_record(self.connection, 8, record)
        self.window.close()

class Ui_AddEvent(object):
    def setupUi(self, AddEvent, connection):
        AddEvent.setObjectName("AddEvent")
        AddEvent.resize(607, 143)
        self.label = QtWidgets.QLabel(AddEvent)
        self.label.setGeometry(QtCore.QRect(170, 10, 131, 16))
        self.label.setObjectName("label")
        self.lineEdit_nazwa = QtWidgets.QLineEdit(AddEvent)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.lineEdit_data = QtWidgets.QLineEdit(AddEvent)
        self.lineEdit_data.setGeometry(QtCore.QRect(150, 60, 113, 20))
        self.lineEdit_data.setObjectName("lineEdit_data")
        self.comboBox_sekcja = QtWidgets.QComboBox(AddEvent)
        self.comboBox_sekcja.setGeometry(QtCore.QRect(440, 60, 141, 22))
        self.comboBox_sekcja.setObjectName("comboBox_sekcja")
        self.label_2 = QtWidgets.QLabel(AddEvent)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddEvent)
        self.label_3.setGeometry(QtCore.QRect(160, 40, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AddEvent)
        self.label_4.setGeometry(QtCore.QRect(450, 40, 121, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(AddEvent)
        self.pushButton.setGeometry(QtCore.QRect(500, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_adres = QtWidgets.QComboBox(AddEvent)
        self.comboBox_adres.setGeometry(QtCore.QRect(280, 60, 141, 22))
        self.comboBox_adres.setObjectName("comboBox_adres")
        self.label_5 = QtWidgets.QLabel(AddEvent)
        self.label_5.setGeometry(QtCore.QRect(290, 40, 47, 13))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(AddEvent)
        QtCore.QMetaObject.connectSlotsByName(AddEvent)

        self.window = AddEvent
        self.setupUi_my(connection)

    def retranslateUi(self, AddEvent):
        _translate = QtCore.QCoreApplication.translate
        AddEvent.setWindowTitle(_translate("AddEvent", "Dialog"))
        self.label.setText(_translate("AddEvent", "Dodajesz nowy event"))
        self.label_2.setText(_translate("AddEvent", "Nazwa"))
        self.label_3.setText(_translate("AddEvent", "Data"))
        self.label_4.setText(_translate("AddEvent", "Sekcja odpowiedzialna:"))
        self.pushButton.setText(_translate("AddEvent", "Dodaj"))
        self.label_5.setText(_translate("AddEvent", "Adres:"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        sekcje = get_names(connection, 0, "nazwa")
        self.comboBox_sekcja.addItems(sekcje)
        miejsca = get_names(connection, 10, "adres")
        self.comboBox_adres.addItems(miejsca)

    def button_fun(self):
        date = validate_date(self.lineEdit_data.text())

        if date is not None:
            record = [self.lineEdit_nazwa.text(),
                     date,
                     self.comboBox_sekcja.currentText(),
                     self.comboBox_adres.currentText()]
            add_record(self.connection, 9, record)
            self.window.close()

class Ui_AddMiejsce(object):
    def setupUi(self, AddMiejsce, connection):
        AddMiejsce.setObjectName("AddMiejsce")
        AddMiejsce.resize(400, 150)
        self.label = QtWidgets.QLabel(AddMiejsce)
        self.label.setGeometry(QtCore.QRect(130, 10, 171, 20))
        self.label.setObjectName("label")
        self.lineEdit_adres = QtWidgets.QLineEdit(AddMiejsce)
        self.lineEdit_adres.setGeometry(QtCore.QRect(20, 70, 113, 20))
        self.lineEdit_adres.setObjectName("lineEdit_adres")
        self.lineEdit_cena = QtWidgets.QLineEdit(AddMiejsce)
        self.lineEdit_cena.setGeometry(QtCore.QRect(150, 70, 81, 20))
        self.lineEdit_cena.setObjectName("lineEdit_cena")
        self.lineEdit_max_osob = QtWidgets.QLineEdit(AddMiejsce)
        self.lineEdit_max_osob.setGeometry(QtCore.QRect(250, 70, 91, 20))
        self.lineEdit_max_osob.setObjectName("lineEdit_max_osob")
        self.label_2 = QtWidgets.QLabel(AddMiejsce)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddMiejsce)
        self.label_3.setGeometry(QtCore.QRect(160, 50, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AddMiejsce)
        self.label_4.setGeometry(QtCore.QRect(260, 50, 51, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(AddMiejsce)
        self.pushButton.setGeometry(QtCore.QRect(300, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(AddMiejsce)
        QtCore.QMetaObject.connectSlotsByName(AddMiejsce)

        self.window = AddMiejsce
        self.setupUi_my(connection)

    def retranslateUi(self, AddMiejsce):
        _translate = QtCore.QCoreApplication.translate
        AddMiejsce.setWindowTitle(_translate("AddMiejsce", "Dialog"))
        self.label.setText(_translate("AddMiejsce", "Dodajesz Miejsce naEvent"))
        self.label_2.setText(_translate("AddMiejsce", "Adres"))
        self.label_3.setText(_translate("AddMiejsce", "Cena"))
        self.label_4.setText(_translate("AddMiejsce", "Max osób"))
        self.pushButton.setText(_translate("AddMiejsce", "Dodaj"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection

    def button_fun(self):
        cena = validate_number(self.lineEdit_cena.text())
        max_osob = validate_number(self.lineEdit_max_osob.text())

        if None not in [cena, max_osob]:
            record = [self.lineEdit_adres.text(),
            cena,
            max_osob]
            add_record(self.connection, 10, record)
            self.window.close()

class Ui_AddSponsor(object):
    def setupUi(self, AddSponsor, connection):
        AddSponsor.setObjectName("AddSponsor")
        AddSponsor.resize(396, 122)
        self.label = QtWidgets.QLabel(AddSponsor)
        self.label.setGeometry(QtCore.QRect(160, 10, 111, 20))
        self.label.setObjectName("label")
        self.lineEdit_nazwa = QtWidgets.QLineEdit(AddSponsor)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.label_2 = QtWidgets.QLabel(AddSponsor)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 47, 13))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(AddSponsor)
        self.pushButton.setGeometry(QtCore.QRect(300, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(AddSponsor)
        QtCore.QMetaObject.connectSlotsByName(AddSponsor)

        self.window = AddSponsor
        self.setupUi_my(connection)

    def retranslateUi(self, AddSponsor):
        _translate = QtCore.QCoreApplication.translate
        AddSponsor.setWindowTitle(_translate("AddSponsor", "Dialog"))
        self.label.setText(_translate("AddSponsor", "Dodajesz sponsora"))
        self.label_2.setText(_translate("AddSponsor", "Nazwa"))
        self.pushButton.setText(_translate("AddSponsor", "Dodaj"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection

    def button_fun(self):
        record = [self.lineEdit_nazwa.text()]
        add_record(self.connection, 11, record)
        self.window.close()

class Ui_AddTurniej(object):
    def setupUi(self, AddTurniej, connection):
        AddTurniej.setObjectName("AddTurniej")
        AddTurniej.resize(401, 154)
        self.label = QtWidgets.QLabel(AddTurniej)
        self.label.setGeometry(QtCore.QRect(160, 10, 101, 20))
        self.label.setObjectName("label")
        self.lineEdit_nazwa = QtWidgets.QLineEdit(AddTurniej)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(20, 70, 101, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.lineEdit_godzina = QtWidgets.QLineEdit(AddTurniej)
        self.lineEdit_godzina.setGeometry(QtCore.QRect(140, 70, 71, 20))
        self.lineEdit_godzina.setObjectName("lineEdit_godzina")
        self.comboBox = QtWidgets.QComboBox(AddTurniej)
        self.comboBox.setGeometry(QtCore.QRect(230, 70, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(AddTurniej)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddTurniej)
        self.label_3.setGeometry(QtCore.QRect(150, 50, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AddTurniej)
        self.label_4.setGeometry(QtCore.QRect(240, 50, 51, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(AddTurniej)
        self.pushButton.setGeometry(QtCore.QRect(310, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(AddTurniej)
        QtCore.QMetaObject.connectSlotsByName(AddTurniej)

        self.window = AddTurniej
        self.setupUi_my(connection)

    def retranslateUi(self, AddTurniej):
        _translate = QtCore.QCoreApplication.translate
        AddTurniej.setWindowTitle(_translate("AddTurniej", "Dialog"))
        self.label.setText(_translate("AddTurniej", "Dodajesz turniej"))
        self.label_2.setText(_translate("AddTurniej", "Nazwa"))
        self.label_3.setText(_translate("AddTurniej", "Godzina"))
        self.label_4.setText(_translate("AddTurniej", "Event:"))
        self.pushButton.setText(_translate("AddTurniej", "Dodaj"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        eventy = get_names(connection, 9, "event")
        self.comboBox.addItems(eventy)

    def button_fun(self):
        hour = validate_hour(self.lineEdit_godzina.text())

        if None not in [hour]:
            record = [self.lineEdit_nazwa.text(),
                    self.comboBox.currentText(),
                    hour]
            add_record(self.connection, 12, record)
            self.window.close()

class Ui_AddUczestnik(object):
    def setupUi(self, AddUczestnik, connection):
        AddUczestnik.setObjectName("AddUczestnik")
        AddUczestnik.resize(519, 162)
        self.label = QtWidgets.QLabel(AddUczestnik)
        self.label.setGeometry(QtCore.QRect(170, 10, 191, 20))
        self.label.setObjectName("label")
        self.lineEdit_imie = QtWidgets.QLineEdit(AddUczestnik)
        self.lineEdit_imie.setGeometry(QtCore.QRect(20, 70, 101, 20))
        self.lineEdit_imie.setObjectName("lineEdit_imie")
        self.lineEdit_nazwisko = QtWidgets.QLineEdit(AddUczestnik)
        self.lineEdit_nazwisko.setGeometry(QtCore.QRect(140, 70, 101, 20))
        self.lineEdit_nazwisko.setObjectName("lineEdit_nazwisko")
        self.comboBox_event = QtWidgets.QComboBox(AddUczestnik)
        self.comboBox_event.setGeometry(QtCore.QRect(260, 70, 101, 22))
        self.comboBox_event.setObjectName("comboBox_event")
        self.comboBox_turniej = QtWidgets.QComboBox(AddUczestnik)
        self.comboBox_turniej.setGeometry(QtCore.QRect(380, 70, 101, 22))
        self.comboBox_turniej.setObjectName("comboBox_turniej")
        self.label_2 = QtWidgets.QLabel(AddUczestnik)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddUczestnik)
        self.label_3.setGeometry(QtCore.QRect(150, 50, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AddUczestnik)
        self.label_4.setGeometry(QtCore.QRect(270, 50, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AddUczestnik)
        self.label_5.setGeometry(QtCore.QRect(390, 50, 51, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(AddUczestnik)
        self.pushButton.setGeometry(QtCore.QRect(420, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(AddUczestnik)
        QtCore.QMetaObject.connectSlotsByName(AddUczestnik)

        self.window = AddUczestnik
        self.setupUi_my(connection)

    def retranslateUi(self, AddUczestnik):
        _translate = QtCore.QCoreApplication.translate
        AddUczestnik.setWindowTitle(_translate("AddUczestnik", "Dialog"))
        self.label.setText(_translate("AddUczestnik", "Dodajesz uczestnika turnieju"))
        self.label_2.setText(_translate("AddUczestnik", "Imie"))
        self.label_3.setText(_translate("AddUczestnik", "Nazwisko"))
        self.label_4.setText(_translate("AddUczestnik", "Event:"))
        self.label_5.setText(_translate("AddUczestnik", "Turniej:"))
        self.pushButton.setText(_translate("AddUczestnik", "Dodaj"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        turnieje = get_names(connection, 12, "turniej")
        # eventy = get_names(connection, 9, "event")
        # self.comboBox_event.addItems(eventy)
        self.comboBox_turniej.addItems(turnieje)

    def button_fun(self):
        record = [self.lineEdit_imie.text(),
                self.lineEdit_nazwisko.text(),
                self.comboBox_turniej.currentText()]
        add_record(self.connection, 13, record)
        self.window.close()

class Ui_AddWygrany(object):
    def setupUi(self, AddWygrany, connection):
        AddWygrany.setObjectName("AddWygrany")
        AddWygrany.resize(619, 155)
        self.label = QtWidgets.QLabel(AddWygrany)
        self.label.setGeometry(QtCore.QRect(240, 10, 151, 20))
        self.label.setObjectName("label")
        self.lineEdit_id_uczestnika = QtWidgets.QLineEdit(AddWygrany)
        self.lineEdit_id_uczestnika.setGeometry(QtCore.QRect(20, 70, 113, 20))
        self.lineEdit_id_uczestnika.setObjectName("lineEdit_id_uczestnika")
        # self.comboBox_event = QtWidgets.QComboBox(AddWygrany)
        # self.comboBox_event.setGeometry(QtCore.QRect(150, 70, 101, 22))
        # self.comboBox_event.setObjectName("comboBox_event")
        self.comboBox_turniej = QtWidgets.QComboBox(AddWygrany)
        self.comboBox_turniej.setGeometry(QtCore.QRect(270, 70, 101, 22))
        self.comboBox_turniej.setObjectName("comboBox_turniej")
        self.lineEdit_miejsce = QtWidgets.QLineEdit(AddWygrany)
        self.lineEdit_miejsce.setGeometry(QtCore.QRect(390, 70, 81, 20))
        self.lineEdit_miejsce.setObjectName("lineEdit_miejsce")
        self.lineEdit_nagroda = QtWidgets.QLineEdit(AddWygrany)
        self.lineEdit_nagroda.setGeometry(QtCore.QRect(490, 70, 101, 20))
        self.lineEdit_nagroda.setObjectName("lineEdit_nagroda")
        self.label_2 = QtWidgets.QLabel(AddWygrany)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddWygrany)
        self.label_3.setGeometry(QtCore.QRect(160, 50, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AddWygrany)
        self.label_4.setGeometry(QtCore.QRect(280, 50, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AddWygrany)
        self.label_5.setGeometry(QtCore.QRect(400, 50, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(AddWygrany)
        self.label_6.setGeometry(QtCore.QRect(500, 50, 51, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(AddWygrany)
        self.pushButton.setGeometry(QtCore.QRect(530, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(AddWygrany)
        QtCore.QMetaObject.connectSlotsByName(AddWygrany)

        self.window = AddWygrany
        self.setupUi_my(connection)

    def retranslateUi(self, AddWygrany):
        _translate = QtCore.QCoreApplication.translate
        AddWygrany.setWindowTitle(_translate("AddWygrany", "Dialog"))
        self.label.setText(_translate("AddWygrany", "Dodajesz nowego wygranego"))
        self.label_2.setText(_translate("AddWygrany", "Id_uczestnika"))
        self.label_3.setText(_translate("AddWygrany", "Event:"))
        self.label_4.setText(_translate("AddWygrany", "Turniej:"))
        self.label_5.setText(_translate("AddWygrany", "Miejsce"))
        self.label_6.setText(_translate("AddWygrany", "Nagroda"))
        self.pushButton.setText(_translate("AddWygrany", "Dodaj"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        # eventy = get_names(connection, 9, "event")
        turnieje = get_names(connection, 12, "turniej")
        # self.comboBox_event.addItems(eventy)
        self.comboBox_turniej.addItems(turnieje)

    def button_fun(self):
        numer_miejsca = validate_number(self.lineEdit_miejsce.text())
        id_uczestnika = validate_number(self.lineEdit_id_uczestnika.text())

        if None not in [numer_miejsca, id_uczestnika]:
            record = [
                numer_miejsca,
                self.comboBox_turniej.currentText(),
                id_uczestnika,
                self.lineEdit_nagroda.text()]
        add_record(self.connection, 14, record)
        self.window.close()


class Ui_DeleteWithLineEdit(object):
    def setupUi(self, DeleteObject, table_nr, name, field, connection):
        DeleteObject.setObjectName("DeleteObject")
        DeleteObject.resize(391, 172)
        self.label = QtWidgets.QLabel(DeleteObject)
        self.label.setGeometry(QtCore.QRect(50, 70, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(DeleteObject)
        self.lineEdit.setGeometry(QtCore.QRect(40, 90, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(DeleteObject)
        self.pushButton.setGeometry(QtCore.QRect(300, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(DeleteObject)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 141, 41))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(DeleteObject, name, field)
        QtCore.QMetaObject.connectSlotsByName(DeleteObject)

        self.window = DeleteObject
        self.field = field
        self.setupUi_my(connection, table_nr)

    def retranslateUi(self, DeleteObject, name, field):
        _translate = QtCore.QCoreApplication.translate
        DeleteObject.setWindowTitle(_translate("DeleteObject", "Dialog"))
        self.label.setText(_translate("DeleteObject", field))
        self.pushButton.setText(_translate("DeleteObject", "Usuń"))
        self.label_2.setText(_translate("DeleteObject", f"Usuwasz {name}"))

    def setupUi_my(self, connection, table_nr):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        self.table_nr = table_nr

    def button_fun(self):
        record = self.lineEdit.text()

        if self.field[:2] == "ID":
            record = validate_number(record)
        else:
            record = "'" + record + "'" #pass as string string

        if record is not None:
            remove_record(self.connection, self.table_nr, f"{self.field} = {record}")
            self.window.close()

class Ui_DeleteSpotkanie(object):
    def setupUi(self, DeleteSpotkanie, connection):
        DeleteSpotkanie.setObjectName("DeleteSpotkanie")
        DeleteSpotkanie.resize(411, 149)
        self.label = QtWidgets.QLabel(DeleteSpotkanie)
        self.label.setGeometry(QtCore.QRect(150, 10, 111, 20))
        self.label.setObjectName("label")
        self.lineEdit_termin = QtWidgets.QLineEdit(DeleteSpotkanie)
        self.lineEdit_termin.setGeometry(QtCore.QRect(150, 60, 113, 20))
        self.lineEdit_termin.setObjectName("lineEdit_termin")
        self.label_2 = QtWidgets.QLabel(DeleteSpotkanie)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 47, 13))
        self.label_2.setObjectName("label_2")
        self.comboBox_sekcja = QtWidgets.QComboBox(DeleteSpotkanie)
        self.comboBox_sekcja.setGeometry(QtCore.QRect(20, 60, 111, 22))
        self.comboBox_sekcja.setObjectName("comboBox_sekcja")
        self.comboBox_miejsce = QtWidgets.QComboBox(DeleteSpotkanie)
        self.comboBox_miejsce.setGeometry(QtCore.QRect(280, 60, 111, 22))
        self.comboBox_miejsce.setObjectName("comboBox_miejsce")
        self.label_3 = QtWidgets.QLabel(DeleteSpotkanie)
        self.label_3.setGeometry(QtCore.QRect(290, 40, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(DeleteSpotkanie)
        self.label_4.setGeometry(QtCore.QRect(160, 40, 47, 13))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(DeleteSpotkanie)
        self.pushButton.setGeometry(QtCore.QRect(320, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(DeleteSpotkanie)
        QtCore.QMetaObject.connectSlotsByName(DeleteSpotkanie)

        self.window = DeleteSpotkanie
        self.setupUi_my(connection)

    def retranslateUi(self, DeleteSpotkanie):
        _translate = QtCore.QCoreApplication.translate
        DeleteSpotkanie.setWindowTitle(_translate("DeleteSpotkanie", "Dialog"))
        self.label.setText(_translate("DeleteSpotkanie", "Usuwasz spotkanie"))
        self.label_2.setText(_translate("DeleteSpotkanie", "Sekcja:"))
        self.label_3.setText(_translate("DeleteSpotkanie", "Miejsce:"))
        self.label_4.setText(_translate("DeleteSpotkanie", "Termin"))
        self.pushButton.setText(_translate("DeleteSpotkanie", "Usuń"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        sekcje = get_names(connection, 0, "nazwa")
        miejsca = get_names(connection, 3, "adres")
        self.comboBox_sekcja.addItems(sekcje)
        self.comboBox_miejsce.addItems(miejsca)

    def button_fun(self):
        id = get_id_by_name(self.connection, 0, self.comboBox_sekcja.currentText())
        cond1 = f"id_sekcji = {id}"
        cond2 = f"adres = '{self.comboBox_miejsce.currentText()}'"
        cond3 = f"termin = '{self.lineEdit_termin.text()}'"

        remove_record(self.connection, 2, f"{cond1} AND {cond2} AND {cond3}")
        self.window.close()

class Ui_DeleteGraKomputerowa(object):
    def setupUi(self, DeleteGraKomputerowa, connection):
        DeleteGraKomputerowa.setObjectName("DeleteGraKomputerowa")
        DeleteGraKomputerowa.resize(400, 165)
        self.label = QtWidgets.QLabel(DeleteGraKomputerowa)
        self.label.setGeometry(QtCore.QRect(160, 10, 81, 20))
        self.label.setObjectName("label")
        self.lineEdit_nazwa = QtWidgets.QLineEdit(DeleteGraKomputerowa)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(20, 80, 113, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.label_2 = QtWidgets.QLabel(DeleteGraKomputerowa)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 51, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(DeleteGraKomputerowa)
        self.pushButton.setGeometry(QtCore.QRect(300, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_platforma = QtWidgets.QComboBox(DeleteGraKomputerowa)
        self.comboBox_platforma.setGeometry(QtCore.QRect(150, 80, 101, 22))
        self.comboBox_platforma.setObjectName("comboBox_platforma")
        self.comboBox_wydawca = QtWidgets.QComboBox(DeleteGraKomputerowa)
        self.comboBox_wydawca.setGeometry(QtCore.QRect(270, 80, 101, 22))
        self.comboBox_wydawca.setObjectName("comboBox_wydawca")
        self.label_3 = QtWidgets.QLabel(DeleteGraKomputerowa)
        self.label_3.setGeometry(QtCore.QRect(160, 60, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(DeleteGraKomputerowa)
        self.label_4.setGeometry(QtCore.QRect(280, 60, 61, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(DeleteGraKomputerowa)
        QtCore.QMetaObject.connectSlotsByName(DeleteGraKomputerowa)

        self.window = DeleteGraKomputerowa
        self.setupUi_my(connection)

    def retranslateUi(self, DeleteGraKomputerowa):
        _translate = QtCore.QCoreApplication.translate
        DeleteGraKomputerowa.setWindowTitle(_translate("DeleteGraKomputerowa", "Dialog"))
        self.label.setText(_translate("DeleteGraKomputerowa", "Usuwasz gre"))
        self.label_2.setText(_translate("DeleteGraKomputerowa", "Nazwa"))
        self.pushButton.setText(_translate("DeleteGraKomputerowa", "Usuń"))
        self.label_3.setText(_translate("DeleteGraKomputerowa", "Platforma"))
        self.label_4.setText(_translate("DeleteGraKomputerowa", "Wydawca"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        platformy = get_names(connection, 7, "platforma")
        wydawcy = get_names(connection, 8, "wydawca")
        self.comboBox_platforma.addItems(platformy)
        self.comboBox_wydawca.addItems(wydawcy)

    def button_fun(self):
        cond1 = f"platforma = '{self.comboBox_platforma.currentText()}'"
        cond2 = f"wydawca = '{self.comboBox_wydawca.currentText()}'"
        cond3 = f"nazwa = '{self.lineEdit_nazwa.text()}'"

        remove_record(self.connection, 5, f"{cond1} AND {cond2} AND {cond3}")
        self.window.close()

class Ui_DeleteGraPlanszowa(object):
    def setupUi(self, DeleteGraPlanszowa, connection):
        DeleteGraPlanszowa.setObjectName("DeleteGraPlanszowa")
        DeleteGraPlanszowa.resize(400, 130)
        self.lineEdit_nazwa = QtWidgets.QLineEdit(DeleteGraPlanszowa)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(20, 70, 113, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.comboBox_wydawca = QtWidgets.QComboBox(DeleteGraPlanszowa)
        self.comboBox_wydawca.setGeometry(QtCore.QRect(150, 70, 101, 22))
        self.comboBox_wydawca.setObjectName("comboBox_wydawca")
        self.label = QtWidgets.QLabel(DeleteGraPlanszowa)
        self.label.setGeometry(QtCore.QRect(30, 50, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DeleteGraPlanszowa)
        self.label_2.setGeometry(QtCore.QRect(160, 50, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DeleteGraPlanszowa)
        self.label_3.setGeometry(QtCore.QRect(130, 10, 151, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(DeleteGraPlanszowa)
        self.pushButton.setGeometry(QtCore.QRect(300, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(DeleteGraPlanszowa)
        QtCore.QMetaObject.connectSlotsByName(DeleteGraPlanszowa)

        self.window = DeleteGraPlanszowa
        self.setupUi_my(connection)

    def retranslateUi(self, DeleteGraPlanszowa):
        _translate = QtCore.QCoreApplication.translate
        DeleteGraPlanszowa.setWindowTitle(_translate("DeleteGraPlanszowa", "Dialog"))
        self.label.setText(_translate("DeleteGraPlanszowa", "Nazwa"))
        self.label_2.setText(_translate("DeleteGraPlanszowa", "Wydawca"))
        self.label_3.setText(_translate("DeleteGraPlanszowa", "Usuwasz gre planszową"))
        self.pushButton.setText(_translate("DeleteGraPlanszowa", "Usuń"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        wydawcy = get_names(connection, 8, "wydawca")
        self.comboBox_wydawca.addItems(wydawcy)

    def button_fun(self):
        id = get_id_by_name(self.connection, 8, self.comboBox_wydawca.currentText())
        cond1 = f"wydawca = '{id}'"
        cond2 = f"nazwa = '{self.lineEdit_nazwa.text()}'"

        remove_record(self.connection, 15, f"{cond1} AND {cond2}")
        self.window.close()

class Ui_DeleteTurniej(object):
    def setupUi(self, DeleteTurniej, connection):
        DeleteTurniej.setObjectName("DeleteTurniej")
        DeleteTurniej.resize(400, 130)
        self.label = QtWidgets.QLabel(DeleteTurniej)
        self.label.setGeometry(QtCore.QRect(150, 0, 111, 20))
        self.label.setObjectName("label")
        self.lineEdit_nazwa = QtWidgets.QLineEdit(DeleteTurniej)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.comboBox_event = QtWidgets.QComboBox(DeleteTurniej)
        self.comboBox_event.setGeometry(QtCore.QRect(150, 60, 111, 22))
        self.comboBox_event.setObjectName("comboBox_event")
        self.pushButton = QtWidgets.QPushButton(DeleteTurniej)
        self.pushButton.setGeometry(QtCore.QRect(300, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(DeleteTurniej)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DeleteTurniej)
        self.label_3.setGeometry(QtCore.QRect(160, 40, 51, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(DeleteTurniej)
        QtCore.QMetaObject.connectSlotsByName(DeleteTurniej)

        self.window = DeleteTurniej
        self.setupUi_my(connection)

    def retranslateUi(self, DeleteTurniej):
        _translate = QtCore.QCoreApplication.translate
        DeleteTurniej.setWindowTitle(_translate("DeleteTurniej", "Dialog"))
        self.label.setText(_translate("DeleteTurniej", "Usuwasz Turniej"))
        self.pushButton.setText(_translate("DeleteTurniej", "Usuń"))
        self.label_2.setText(_translate("DeleteTurniej", "Nazwa"))
        self.label_3.setText(_translate("DeleteTurniej", "Event:"))


    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        eventy = get_names(connection, 9, "event")
        self.comboBox_event.addItems(eventy)

    def button_fun(self):
        cond1 = f"event = '{self.comboBox_event.currentText()}'"
        cond2 = f"nazwa = '{self.lineEdit_nazwa.text()}'"

        remove_record(self.connection, 12, f"{cond1} AND {cond2}")
        self.window.close()


class Ui_UpdateNameName(object):
    def setupUi(self, UpdateObject, tab_nr: int, what: str,  connection):
        UpdateObject.setObjectName("UpdateObject")
        UpdateObject.resize(431, 160)
        self.label = QtWidgets.QLabel(UpdateObject)
        self.label.setGeometry(QtCore.QRect(150, 10, 131, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(UpdateObject)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 101, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_nowa_nazwa = QtWidgets.QLineEdit(UpdateObject)
        self.lineEdit_nowa_nazwa.setGeometry(QtCore.QRect(260, 70, 113, 20))
        self.lineEdit_nowa_nazwa.setObjectName("lineEdit_nowa_nazwa")
        self.comboBox_stara_nazwa = QtWidgets.QComboBox(UpdateObject)
        self.comboBox_stara_nazwa.setGeometry(QtCore.QRect(20, 70, 101, 22))
        self.comboBox_stara_nazwa.setObjectName("comboBox_stara_nazwa")
        self.label_3 = QtWidgets.QLabel(UpdateObject)
        self.label_3.setGeometry(QtCore.QRect(270, 50, 91, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(UpdateObject)
        self.pushButton.setGeometry(QtCore.QRect(340, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(UpdateObject, what)
        QtCore.QMetaObject.connectSlotsByName(UpdateObject)

        self.tab_nr = tab_nr
        self.window = UpdateObject
        self.setupUi_my(connection, tab_nr, what)

    def retranslateUi(self, UpdateObject, what: str):
        _translate = QtCore.QCoreApplication.translate
        UpdateObject.setWindowTitle(_translate("UpdateObject", "Dialog"))
        self.label.setText(_translate("UpdateObject", f"Zmieniasz nazwę {what}"))
        self.label_2.setText(_translate("UpdateObject", "Stara nazwa:"))
        self.label_3.setText(_translate("UpdateObject", "Nowa nazwa"))
        self.pushButton.setText(_translate("UpdateObject", "Zmień"))

    def setupUi_my(self, connection, tab_nr, what):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        nazwa = what[:-1]+"a"
        if nazwa == "sekcja": nazwa = "nazwa"
        old = get_names(connection, tab_nr, nazwa)
        self.comboBox_stara_nazwa.addItems(old)

    def button_fun(self):
        cond = f"nazwa = '{self.comboBox_stara_nazwa.currentText()}'"
        new = f"nazwa = '{self.lineEdit_nowa_nazwa.text()}'"

        update_record(self.connection, self.tab_nr, new, cond)
        self.window.close()

class Ui_UpdateAdrCost(object):
    def setupUi(self, UpdateObject, tab_nr: int, what: str, costname: str, connection):
        UpdateObject.setObjectName("UpdateObject")
        UpdateObject.resize(400, 186)
        self.label = QtWidgets.QLabel(UpdateObject)
        self.label.setGeometry(QtCore.QRect(130, 10, 181, 20))
        self.label.setObjectName("label")
        self.comboBox_adres = QtWidgets.QComboBox(UpdateObject)
        self.comboBox_adres.setGeometry(QtCore.QRect(40, 80, 101, 22))
        self.comboBox_adres.setObjectName("comboBox_adres")
        self.label_2 = QtWidgets.QLabel(UpdateObject)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit_koszt = QtWidgets.QLineEdit(UpdateObject)
        self.lineEdit_koszt.setGeometry(QtCore.QRect(240, 80, 113, 20))
        self.lineEdit_koszt.setObjectName("lineEdit_koszt")
        self.label_3 = QtWidgets.QLabel(UpdateObject)
        self.label_3.setGeometry(QtCore.QRect(250, 60, 47, 13))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(UpdateObject)
        self.pushButton.setGeometry(QtCore.QRect(300, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(UpdateObject, what, costname)
        QtCore.QMetaObject.connectSlotsByName(UpdateObject)

        self.tab_nr = tab_nr
        self.costname = costname
        self.window = UpdateObject
        self.setupUi_my(connection, tab_nr)

    def retranslateUi(self, UpdateObject, what, costname):
        _translate = QtCore.QCoreApplication.translate
        UpdateObject.setWindowTitle(_translate("UpdateObject", "Dialog"))
        self.label.setText(_translate("UpdateObject", f"Zmieniasz {what}"))
        self.label_2.setText(_translate("UpdateObject", "Adres:"))
        self.label_3.setText(_translate("UpdateObject", costname))
        self.pushButton.setText(_translate("UpdateObject", "Zmień"))

    def setupUi_my(self, connection, tab_nr):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        old = get_names(connection, tab_nr, "adres")
        self.comboBox_adres.addItems(old)

    def button_fun(self):
        cond = f"adres = '{self.comboBox_adres.currentText()}'"
        cost = validate_number(self.lineEdit_koszt.text())

        if cost is not None:
            new = f"{self.costname} = {cost}"
            update_record(self.connection, self.tab_nr, new, cond)
            self.window.close()


class Ui_AddSponsoring(object):
    def setupUi(self, AddSponsoring, connection):
        AddSponsoring.setObjectName("AddSponsoring")
        AddSponsoring.resize(400, 162)
        self.label = QtWidgets.QLabel(AddSponsoring)
        self.label.setGeometry(QtCore.QRect(140, 20, 111, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddSponsoring)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 51, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(AddSponsoring)
        self.pushButton.setGeometry(QtCore.QRect(300, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_event = QtWidgets.QComboBox(AddSponsoring)
        self.comboBox_event.setGeometry(QtCore.QRect(150, 80, 101, 22))
        self.comboBox_event.setObjectName("comboBox_event")
        self.label_3 = QtWidgets.QLabel(AddSponsoring)
        self.label_3.setGeometry(QtCore.QRect(160, 60, 51, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_kwota = QtWidgets.QLineEdit(AddSponsoring)
        self.lineEdit_kwota.setGeometry(QtCore.QRect(270, 80, 91, 20))
        self.lineEdit_kwota.setObjectName("lineEdit_kwota")
        self.label_4 = QtWidgets.QLabel(AddSponsoring)
        self.label_4.setGeometry(QtCore.QRect(280, 60, 47, 13))
        self.label_4.setObjectName("label_4")
        self.comboBox_sponsor = QtWidgets.QComboBox(AddSponsoring)
        self.comboBox_sponsor.setGeometry(QtCore.QRect(18, 80, 111, 22))
        self.comboBox_sponsor.setObjectName("comboBox_sponsor")

        self.retranslateUi(AddSponsoring)
        QtCore.QMetaObject.connectSlotsByName(AddSponsoring)

        self.window = AddSponsoring
        self.setupUi_my(connection)

    def retranslateUi(self, AddSponsoring):
        _translate = QtCore.QCoreApplication.translate
        AddSponsoring.setWindowTitle(_translate("AddSponsoring", "Dialog"))
        self.label.setText(_translate("AddSponsoring", "Dodajesz sponsoring"))
        self.label_2.setText(_translate("AddSponsoring", "Nazwa"))
        self.pushButton.setText(_translate("AddSponsoring", "Dodaj"))
        self.label_3.setText(_translate("AddSponsoring", "Event:"))
        self.label_4.setText(_translate("AddSponsoring", "Kwota"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        eventy = get_names(connection, 9, "event")
        sponsorzy = get_names(connection, 11, "nazwa")
        self.comboBox_event.addItems(eventy)
        self.comboBox_sponsor.addItems(sponsorzy)

    def button_fun(self):
        amount = self.lineEdit_kwota.text()

        if validate_number(amount) is not None:
            record = [amount,
                    self.comboBox_sponsor.currentText(),
                    self.comboBox_event.currentText(),
                    ]
            add_record(self.connection, 16, record)
            self.window.close()

class Ui_AssignCzlonekSekcja(object):
    def setupUi(self, AssignCzlonekSekcja, connection):
        AssignCzlonekSekcja.setObjectName("AssignCzlonekSekcja")
        AssignCzlonekSekcja.resize(432, 174)
        self.label = QtWidgets.QLabel(AssignCzlonekSekcja)
        self.label.setGeometry(QtCore.QRect(130, 20, 161, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AssignCzlonekSekcja)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AssignCzlonekSekcja)
        self.label_3.setGeometry(QtCore.QRect(210, 90, 47, 13))
        self.label_3.setObjectName("label_3")
        self.comboBox_sekcja = QtWidgets.QComboBox(AssignCzlonekSekcja)
        self.comboBox_sekcja.setGeometry(QtCore.QRect(290, 90, 101, 22))
        self.comboBox_sekcja.setObjectName("comboBox_sekcja")
        self.label_4 = QtWidgets.QLabel(AssignCzlonekSekcja)
        self.label_4.setGeometry(QtCore.QRect(300, 70, 47, 13))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(AssignCzlonekSekcja)
        self.pushButton.setGeometry(QtCore.QRect(340, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_PESEL = QtWidgets.QComboBox(AssignCzlonekSekcja)
        self.comboBox_PESEL.setGeometry(QtCore.QRect(30, 90, 111, 22))
        self.comboBox_PESEL.setObjectName("comboBox_PESEL")

        self.retranslateUi(AssignCzlonekSekcja)
        QtCore.QMetaObject.connectSlotsByName(AssignCzlonekSekcja)

        self.window = AssignCzlonekSekcja
        self.setupUi_my(connection)

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        pesele = get_names(connection, 1, "pesel")
        sekcje = get_names(connection, 0, "nazwa")
        self.comboBox_PESEL.addItems(pesele)
        self.comboBox_sekcja.addItems(sekcje)

    def button_fun(self):
        record = [self.comboBox_PESEL.currentText(),
                self.comboBox_sekcja.currentText()]
        add_record(self.connection, 18, record)
        self.window.close()


    def retranslateUi(self, AssignCzlonekSekcja):
        _translate = QtCore.QCoreApplication.translate
        AssignCzlonekSekcja.setWindowTitle(_translate("AssignCzlonekSekcja", "Dialog"))
        self.label.setText(_translate("AssignCzlonekSekcja", "Przypisujesz czlonka do sekcji"))
        self.label_2.setText(_translate("AssignCzlonekSekcja", "PESEL"))
        self.label_3.setText(_translate("AssignCzlonekSekcja", "do"))
        self.label_4.setText(_translate("AssignCzlonekSekcja", "Sekcja"))
        self.pushButton.setText(_translate("AssignCzlonekSekcja", "Przypisz"))
# -----------------------------------

class Ui_AddGraTurniej(object):
    def setupUi(self, AddGraTurniej, connection):
        AddGraTurniej.setObjectName("AddGraTurniej")
        AddGraTurniej.resize(400, 136)
        self.lineEdit_id_gra = QtWidgets.QLineEdit(AddGraTurniej)
        self.lineEdit_id_gra.setGeometry(QtCore.QRect(30, 60, 113, 20))
        self.lineEdit_id_gra.setObjectName("lineEdit_id_gra")
        self.label = QtWidgets.QLabel(AddGraTurniej)
        self.label.setGeometry(QtCore.QRect(40, 40, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddGraTurniej)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 131, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(AddGraTurniej)
        self.pushButton.setGeometry(QtCore.QRect(300, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_turniej = QtWidgets.QComboBox(AddGraTurniej)
        self.comboBox_turniej.setGeometry(QtCore.QRect(160, 60, 101, 22))
        self.comboBox_turniej.setObjectName("comboBox_turniej")
        self.label_3 = QtWidgets.QLabel(AddGraTurniej)
        self.label_3.setGeometry(QtCore.QRect(170, 40, 51, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(AddGraTurniej)
        QtCore.QMetaObject.connectSlotsByName(AddGraTurniej)
        self.window = AddGraTurniej
        self.setupUi_my(connection)

    def retranslateUi(self, AddGraTurniej):
        _translate = QtCore.QCoreApplication.translate
        AddGraTurniej.setWindowTitle(_translate("AddGraTurniej", "Dialog"))
        self.label.setText(_translate("AddGraTurniej", "ID egzemplarza"))
        self.label_2.setText(_translate("AddGraTurniej", "Dodajesz gre do turnieju"))
        self.pushButton.setText(_translate("AddGraTurniej", "Dodaj"))
        self.label_3.setText(_translate("AddGraTurniej", "Turniej"))

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        turnieje = get_names(connection, 12, "turniej")
        self.comboBox_turniej.addItems(turnieje)

    def button_fun(self):
        print("button pushed")
        turniej = validate_number(self.lineEdit_id_gra.text())

        if turniej is not None:
            record = [turniej,
                    self.comboBox_turniej.currentText()
                    ]
            add_record(self.connection, 17, record)
            self.window.close()

class Ui_DeleteGraTurniej(object):
    def setupUi(self, DeleteGraTurniej, connection):
        DeleteGraTurniej.setObjectName("DeleteGraTurniej")
        DeleteGraTurniej.resize(400, 136)
        self.lineEdit_id_gra = QtWidgets.QLineEdit(DeleteGraTurniej)
        self.lineEdit_id_gra.setGeometry(QtCore.QRect(30, 60, 113, 20))
        self.lineEdit_id_gra.setObjectName("lineEdit_id_gra")
        self.label = QtWidgets.QLabel(DeleteGraTurniej)
        self.label.setGeometry(QtCore.QRect(40, 40, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DeleteGraTurniej)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 131, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(DeleteGraTurniej)
        self.pushButton.setGeometry(QtCore.QRect(300, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(DeleteGraTurniej)
        self.label_3.setGeometry(QtCore.QRect(170, 40, 51, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_turniej = QtWidgets.QComboBox(DeleteGraTurniej)
        self.comboBox_turniej.setGeometry(QtCore.QRect(160, 60, 101, 22))
        self.comboBox_turniej.setObjectName("comboBox_turniej")

        self.retranslateUi(DeleteGraTurniej)
        QtCore.QMetaObject.connectSlotsByName(DeleteGraTurniej)

        self.window = DeleteGraTurniej
        self.setupUi_my(connection)

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        turnieje = get_names(connection, 12, "turniej")
        self.comboBox_turniej.addItems(turnieje)

    def button_fun(self):
        gra = validate_number(self.lineEdit_id_gra.text())

        if gra is not None:
            id_turnieju = get_id_by_name(self.connection, 12, self.comboBox_turniej.currentText())
            cond1 = f"id_egzemplarza = '{gra}'"
            cond2 = f"turniej = '{id_turnieju}'"
            remove_record(self.connection, 17, f"{cond1} AND {cond2}")
            self.window.close()

    def retranslateUi(self, DeleteGraTurniej):
        _translate = QtCore.QCoreApplication.translate
        DeleteGraTurniej.setWindowTitle(_translate("DeleteGraTurniej", "Dialog"))
        self.label.setText(_translate("DeleteGraTurniej", "ID egzemplarza"))
        self.label_2.setText(_translate("DeleteGraTurniej", "Usuwasz gre z turnieju"))
        self.pushButton.setText(_translate("DeleteGraTurniej", "Usuń"))
        self.label_3.setText(_translate("DeleteGraTurniej", "Turniej"))

class Ui_UpdateEventSekcja(object):
    def setupUi(self, UpdateEventSekcja, connection):
        UpdateEventSekcja.setObjectName("UpdateEventSekcja")
        UpdateEventSekcja.resize(441, 143)
        self.label = QtWidgets.QLabel(UpdateEventSekcja)
        self.label.setGeometry(QtCore.QRect(120, 10, 241, 20))
        self.label.setObjectName("label")
        self.comboBox_sekcja = QtWidgets.QComboBox(UpdateEventSekcja)
        self.comboBox_sekcja.setGeometry(QtCore.QRect(280, 60, 141, 22))
        self.comboBox_sekcja.setObjectName("comboBox_sekcja")
        self.label_2 = QtWidgets.QLabel(UpdateEventSekcja)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(UpdateEventSekcja)
        self.label_4.setGeometry(QtCore.QRect(290, 40, 121, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(UpdateEventSekcja)
        self.pushButton.setGeometry(QtCore.QRect(350, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_nazwa = QtWidgets.QComboBox(UpdateEventSekcja)
        self.comboBox_nazwa.setGeometry(QtCore.QRect(20, 60, 121, 22))
        self.comboBox_nazwa.setObjectName("comboBox_nazwa")

        self.retranslateUi(UpdateEventSekcja)
        QtCore.QMetaObject.connectSlotsByName(UpdateEventSekcja)

        self.window = UpdateEventSekcja
        self.setupUi_my(connection)

    def setupUi_my(self, connection):
        self.pushButton.clicked.connect(self.button_fun)
        self.connection = connection
        eventy = get_names(connection, 9, "event")
        sekcje = get_names(connection, 0, "nazwa")
        self.comboBox_nazwa.addItems(eventy)
        self.comboBox_sekcja.addItems(sekcje)

    def button_fun(self):
        # cond1 = f"nazwa = '{gra}'"
        # cond2 = f"turniej = '{self.comboBox_turniej.currentText()}'"


        # record = [self.comboBox_sekcja.currentText(),
        #         self.comboBox_nazwa.currentText()]
        # update_record(self.connection, 17, record)
        self.window.close()

    def retranslateUi(self, UpdateEventSekcja):
        _translate = QtCore.QCoreApplication.translate
        UpdateEventSekcja.setWindowTitle(_translate("UpdateEventSekcja", "Dialog"))
        self.label.setText(_translate("UpdateEventSekcja", "Zmieniasz sekcje odpowiedzialną za event"))
        self.label_2.setText(_translate("UpdateEventSekcja", "Nazwa"))
        self.label_4.setText(_translate("UpdateEventSekcja", "Sekcja odpowiedzialna:"))
        self.pushButton.setText(_translate("UpdateEventSekcja", "Zmień"))
