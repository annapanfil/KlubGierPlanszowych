from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateSekcja(object):
    def setupUi(self, CreateSekcja):
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

        self.setupUi_my()

    def setupUi_my(self):
        print("create")
        self.pushButton.clicked.connect(self.button_fun)
    
    def button_fun(self):
        print(f"dodaje sekcje {self.lineEdit_nazwa.text()}")

    def retranslateUi(self, CreateSekcja):
        _translate = QtCore.QCoreApplication.translate
        CreateSekcja.setWindowTitle(_translate("CreateSekcja", "Dialog"))
        self.label.setText(_translate("CreateSekcja", "Nazwa"))
        self.pushButton.setText(_translate("CreateSekcja", "Utwórz"))
        self.label_2.setText(_translate("CreateSekcja", "Tworzysz nową sekcję"))

class Ui_DeleteSekcja(object):
    def setupUi(self, DeleteSekcja):
        DeleteSekcja.setObjectName("DeleteSekcja")
        DeleteSekcja.resize(391, 172)
        self.label = QtWidgets.QLabel(DeleteSekcja)
        self.label.setGeometry(QtCore.QRect(50, 70, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit_nazwa = QtWidgets.QLineEdit(DeleteSekcja)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(40, 90, 141, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.pushButton = QtWidgets.QPushButton(DeleteSekcja)
        self.pushButton.setGeometry(QtCore.QRect(300, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(DeleteSekcja)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 141, 41))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(DeleteSekcja)
        QtCore.QMetaObject.connectSlotsByName(DeleteSekcja)

    def retranslateUi(self, DeleteSekcja):
        _translate = QtCore.QCoreApplication.translate
        DeleteSekcja.setWindowTitle(_translate("DeleteSekcja", "Dialog"))
        self.label.setText(_translate("DeleteSekcja", "Nazwa"))
        self.pushButton.setText(_translate("DeleteSekcja", "Usuń"))
        self.label_2.setText(_translate("DeleteSekcja", "Usuwasz sekcję"))

class Ui_AddCzlonek(object):
    def setupUi(self, AddCzlonek):
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

    def retranslateUi(self, AddCzlonek):
        _translate = QtCore.QCoreApplication.translate
        AddCzlonek.setWindowTitle(_translate("AddCzlonek", "Dialog"))
        self.label.setText(_translate("AddCzlonek", "Imię"))
        self.label_2.setText(_translate("AddCzlonek", "Nazwisko"))
        self.label_3.setText(_translate("AddCzlonek", "Data Urodzenia"))
        self.label_4.setText(_translate("AddCzlonek", "PESEL"))
        self.label_5.setText(_translate("AddCzlonek", "Dodajesz Nowego członka"))
        self.pushButton.setText(_translate("AddCzlonek", "Dodaj"))

class Ui_DeleteCzlonek(object):
    def setupUi(self, DeleteCzlonek):
        DeleteCzlonek.setObjectName("DeleteCzlonek")
        DeleteCzlonek.resize(410, 167)
        self.label = QtWidgets.QLabel(DeleteCzlonek)
        self.label.setGeometry(QtCore.QRect(50, 60, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(DeleteCzlonek)
        self.lineEdit.setGeometry(QtCore.QRect(40, 80, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(DeleteCzlonek)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 121, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(DeleteCzlonek)
        self.pushButton.setGeometry(QtCore.QRect(310, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(DeleteCzlonek)
        QtCore.QMetaObject.connectSlotsByName(DeleteCzlonek)

    def retranslateUi(self, DeleteCzlonek):
        _translate = QtCore.QCoreApplication.translate
        DeleteCzlonek.setWindowTitle(_translate("DeleteCzlonek", "Dialog"))
        self.label.setText(_translate("DeleteCzlonek", "PESEL"))
        self.lineEdit.setWhatsThis(_translate("DeleteCzlonek", "<html><head/><body><p>PESEL spisywany przez klienta.</p></body></html>"))
        self.label_2.setText(_translate("DeleteCzlonek", "Usuwasz członka"))
        self.pushButton.setText(_translate("DeleteCzlonek", "Usuń"))

class Ui_AssignCzlonekSekcja(object):
    def setupUi(self, AssignCzlonekSekcja):
        AssignCzlonekSekcja.setObjectName("AssignCzlonekSekcja")
        AssignCzlonekSekcja.resize(432, 174)
        self.label = QtWidgets.QLabel(AssignCzlonekSekcja)
        self.label.setGeometry(QtCore.QRect(130, 20, 161, 16))
        self.label.setObjectName("label")
        self.lineEdit_PESEL = QtWidgets.QLineEdit(AssignCzlonekSekcja)
        self.lineEdit_PESEL.setGeometry(QtCore.QRect(30, 90, 113, 20))
        self.lineEdit_PESEL.setObjectName("lineEdit_PESEL")
        self.label_2 = QtWidgets.QLabel(AssignCzlonekSekcja)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AssignCzlonekSekcja)
        self.label_3.setGeometry(QtCore.QRect(210, 90, 47, 13))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(AssignCzlonekSekcja)
        self.comboBox.setGeometry(QtCore.QRect(290, 90, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(AssignCzlonekSekcja)
        self.label_4.setGeometry(QtCore.QRect(300, 70, 47, 13))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(AssignCzlonekSekcja)
        self.pushButton.setGeometry(QtCore.QRect(340, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(AssignCzlonekSekcja)
        QtCore.QMetaObject.connectSlotsByName(AssignCzlonekSekcja)
        
        self.setupUI_my()

    def setupUI_my(self):
        self.comboBox.addItem("planszowe")
        self.comboBox.addItem("komputerowe")

        self.pushButton.clicked.connect(self.button_fun)
    
    def button_fun(self):
        print(f'Przypisano do {self.comboBox.currentText()}')


    def retranslateUi(self, AssignCzlonekSekcja):
        _translate = QtCore.QCoreApplication.translate
        AssignCzlonekSekcja.setWindowTitle(_translate("AssignCzlonekSekcja", "Dialog"))
        self.label.setText(_translate("AssignCzlonekSekcja", "Przypisujesz czlonka do sekcji"))
        self.label_2.setText(_translate("AssignCzlonekSekcja", "PESEL"))
        self.label_3.setText(_translate("AssignCzlonekSekcja", "do"))
        self.label_4.setText(_translate("AssignCzlonekSekcja", "Sekcja"))
        self.pushButton.setText(_translate("AssignCzlonekSekcja", "Przypisz"))

class Ui_AddSpotkanie(object):
    def setupUi(self, AddSpotkanie):
        AddSpotkanie.setObjectName("AddSpotkanie")
        AddSpotkanie.resize(411, 149)
        self.label = QtWidgets.QLabel(AddSpotkanie)
        self.label.setGeometry(QtCore.QRect(150, 10, 111, 20))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(AddSpotkanie)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 60, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
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

    def retranslateUi(self, AddSpotkanie):
        _translate = QtCore.QCoreApplication.translate
        AddSpotkanie.setWindowTitle(_translate("AddSpotkanie", "Dialog"))
        self.label.setText(_translate("AddSpotkanie", "Dodajesz spotkanie"))
        self.label_2.setText(_translate("AddSpotkanie", "Sekcja:"))
        self.label_3.setText(_translate("AddSpotkanie", "Miejsce:"))
        self.label_4.setText(_translate("AddSpotkanie", "Termin"))
        self.pushButton.setText(_translate("AddSpotkanie", "Dodaj"))

class Ui_DeleteSpotkanie(object):
    def setupUi(self, DeleteSpotkanie):
        DeleteSpotkanie.setObjectName("DeleteSpotkanie")
        DeleteSpotkanie.resize(411, 149)
        self.label = QtWidgets.QLabel(DeleteSpotkanie)
        self.label.setGeometry(QtCore.QRect(150, 10, 111, 20))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(DeleteSpotkanie)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 60, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
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

    def retranslateUi(self, DeleteSpotkanie):
        _translate = QtCore.QCoreApplication.translate
        DeleteSpotkanie.setWindowTitle(_translate("DeleteSpotkanie", "Dialog"))
        self.label.setText(_translate("DeleteSpotkanie", "Usuwasz spotkanie"))
        self.label_2.setText(_translate("DeleteSpotkanie", "Sekcja:"))
        self.label_3.setText(_translate("DeleteSpotkanie", "Miejsce:"))
        self.label_4.setText(_translate("DeleteSpotkanie", "Termin"))
        self.pushButton.setText(_translate("DeleteSpotkanie", "Usuń"))

class Ui_AddPlacowka(object):
    def setupUi(self, AddPlacowka):
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

    def retranslateUi(self, AddPlacowka):
        _translate = QtCore.QCoreApplication.translate
        AddPlacowka.setWindowTitle(_translate("AddPlacowka", "Dialog"))
        self.label.setText(_translate("AddPlacowka", "Dodajesz Miejsce na spotkania"))
        self.label_2.setText(_translate("AddPlacowka", "Adres"))
        self.label_3.setText(_translate("AddPlacowka", "Czynsz"))
        self.pushButton.setText(_translate("AddPlacowka", "Dodaj"))

class Ui_DeletePlacowka(object):
    def setupUi(self, DeletePlacowka):
        DeletePlacowka.setObjectName("DeletePlacowka")
        DeletePlacowka.resize(400, 156)
        self.label = QtWidgets.QLabel(DeletePlacowka)
        self.label.setGeometry(QtCore.QRect(130, 10, 161, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(DeletePlacowka)
        self.lineEdit.setGeometry(QtCore.QRect(30, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(DeletePlacowka)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(DeletePlacowka)
        self.pushButton.setGeometry(QtCore.QRect(300, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(DeletePlacowka)
        QtCore.QMetaObject.connectSlotsByName(DeletePlacowka)

    def retranslateUi(self, DeletePlacowka):
        _translate = QtCore.QCoreApplication.translate
        DeletePlacowka.setWindowTitle(_translate("DeletePlacowka", "Dialog"))
        self.label.setText(_translate("DeletePlacowka", "Usuwasz miejsce spotkań"))
        self.label_2.setText(_translate("DeletePlacowka", "Adres"))
        self.pushButton.setText(_translate("DeletePlacowka", "Usuń"))

class Ui_UpdatePlacowka(object):
    def setupUi(self, UpdatePlacowka):
        UpdatePlacowka.setObjectName("UpdatePlacowka")
        UpdatePlacowka.resize(400, 186)
        self.label = QtWidgets.QLabel(UpdatePlacowka)
        self.label.setGeometry(QtCore.QRect(130, 10, 181, 20))
        self.label.setObjectName("label")
        self.comboBox_adres = QtWidgets.QComboBox(UpdatePlacowka)
        self.comboBox_adres.setGeometry(QtCore.QRect(40, 80, 101, 22))
        self.comboBox_adres.setObjectName("comboBox_adres")
        self.label_2 = QtWidgets.QLabel(UpdatePlacowka)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit_czynsz = QtWidgets.QLineEdit(UpdatePlacowka)
        self.lineEdit_czynsz.setGeometry(QtCore.QRect(240, 80, 113, 20))
        self.lineEdit_czynsz.setObjectName("lineEdit_czynsz")
        self.label_3 = QtWidgets.QLabel(UpdatePlacowka)
        self.label_3.setGeometry(QtCore.QRect(250, 60, 47, 13))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(UpdatePlacowka)
        self.pushButton.setGeometry(QtCore.QRect(300, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(UpdatePlacowka)
        QtCore.QMetaObject.connectSlotsByName(UpdatePlacowka)

    def retranslateUi(self, UpdatePlacowka):
        _translate = QtCore.QCoreApplication.translate
        UpdatePlacowka.setWindowTitle(_translate("UpdatePlacowka", "Dialog"))
        self.label.setText(_translate("UpdatePlacowka", "Zmieniasz czynsz placówki"))
        self.label_2.setText(_translate("UpdatePlacowka", "Adres:"))
        self.label_3.setText(_translate("UpdatePlacowka", "Czynsz"))
        self.pushButton.setText(_translate("UpdatePlacowka", "Zmień"))

class Ui_AddEgzemplarz(object):
    def setupUi(self, AddEgzemplarz):
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

    def retranslateUi(self, AddEgzemplarz):
        _translate = QtCore.QCoreApplication.translate
        AddEgzemplarz.setWindowTitle(_translate("AddEgzemplarz", "Dialog"))
        self.label.setText(_translate("AddEgzemplarz", "Dodajesz egzemplarz"))
        self.label_2.setText(_translate("AddEgzemplarz", "Gra:"))
        self.pushButton.setText(_translate("AddEgzemplarz", "Dodaj"))
        self.label_3.setText(_translate("AddEgzemplarz", "Sekcja:"))

class Ui_DeleteEgzemplarz(object):
    def setupUi(self, DeleteEgzemplarz):
        DeleteEgzemplarz.setObjectName("DeleteEgzemplarz")
        DeleteEgzemplarz.resize(400, 132)
        self.label = QtWidgets.QLabel(DeleteEgzemplarz)
        self.label.setGeometry(QtCore.QRect(140, 20, 141, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(DeleteEgzemplarz)
        self.lineEdit.setGeometry(QtCore.QRect(30, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(DeleteEgzemplarz)
        self.pushButton.setGeometry(QtCore.QRect(290, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(DeleteEgzemplarz)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 47, 13))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(DeleteEgzemplarz)
        QtCore.QMetaObject.connectSlotsByName(DeleteEgzemplarz)

    def retranslateUi(self, DeleteEgzemplarz):
        _translate = QtCore.QCoreApplication.translate
        DeleteEgzemplarz.setWindowTitle(_translate("DeleteEgzemplarz", "Dialog"))
        self.label.setText(_translate("DeleteEgzemplarz", "Usuwasz egzemplarz gry"))
        self.pushButton.setText(_translate("DeleteEgzemplarz", "Usuń"))
        self.label_2.setText(_translate("DeleteEgzemplarz", "ID"))

class Ui_AddGraKomputerowa(object):
    def setupUi(self, AddGraKomputerowa):
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

    def retranslateUi(self, AddGraKomputerowa):
        _translate = QtCore.QCoreApplication.translate
        AddGraKomputerowa.setWindowTitle(_translate("AddGraKomputerowa", "Dialog"))
        self.label.setText(_translate("AddGraKomputerowa", "Dodajesz grę komputerową"))
        self.label_2.setText(_translate("AddGraKomputerowa", "Nazwa"))
        self.label_3.setText(_translate("AddGraKomputerowa", "Cena"))
        self.label_4.setText(_translate("AddGraKomputerowa", "Platforma:"))
        self.label_5.setText(_translate("AddGraKomputerowa", "Wydawca:"))
        self.pushButton.setText(_translate("AddGraKomputerowa", "Dodaj"))

class Ui_DeleteGraKomputerowa(object):
    def setupUi(self, DeleteGraKomputerowa):
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

    def retranslateUi(self, DeleteGraKomputerowa):
        _translate = QtCore.QCoreApplication.translate
        DeleteGraKomputerowa.setWindowTitle(_translate("DeleteGraKomputerowa", "Dialog"))
        self.label.setText(_translate("DeleteGraKomputerowa", "Usuwasz gre"))
        self.label_2.setText(_translate("DeleteGraKomputerowa", "Nazwa"))
        self.pushButton.setText(_translate("DeleteGraKomputerowa", "Usuń"))
        self.label_3.setText(_translate("DeleteGraKomputerowa", "Platforma"))
        self.label_4.setText(_translate("DeleteGraKomputerowa", "Wydawca"))

class Ui_AddGraPlanszowa(object):
    def setupUi(self, AddGraPlanszowa):
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

class Ui_DeleteGraPlanszowa(object):
    def setupUi(self, DeleteGraPlanszowa):
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

    def retranslateUi(self, DeleteGraPlanszowa):
        _translate = QtCore.QCoreApplication.translate
        DeleteGraPlanszowa.setWindowTitle(_translate("DeleteGraPlanszowa", "Dialog"))
        self.label.setText(_translate("DeleteGraPlanszowa", "Nazwa"))
        self.label_2.setText(_translate("DeleteGraPlanszowa", "Wydawca"))
        self.label_3.setText(_translate("DeleteGraPlanszowa", "Usuwasz gre planszową"))
        self.pushButton.setText(_translate("DeleteGraPlanszowa", "Usuń"))

class Ui_AddPlatforma(object):
    def setupUi(self, AddPlatforma):
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

    def retranslateUi(self, AddPlatforma):
        _translate = QtCore.QCoreApplication.translate
        AddPlatforma.setWindowTitle(_translate("AddPlatforma", "Dialog"))
        self.label.setText(_translate("AddPlatforma", "Nazwa:"))
        self.label_2.setText(_translate("AddPlatforma", "Dodajesz platformę"))
        self.pushButton.setText(_translate("AddPlatforma", "Dodaj"))

class Ui_DeletePlatforma(object):
    def setupUi(self, DeletePlatforma):
        DeletePlatforma.setObjectName("DeletePlatforma")
        DeletePlatforma.resize(400, 130)
        self.lineEdit_nazwa = QtWidgets.QLineEdit(DeletePlatforma)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(30, 60, 113, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.label = QtWidgets.QLabel(DeletePlatforma)
        self.label.setGeometry(QtCore.QRect(40, 40, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DeletePlatforma)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 121, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(DeletePlatforma)
        self.pushButton.setGeometry(QtCore.QRect(300, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(DeletePlatforma)
        QtCore.QMetaObject.connectSlotsByName(DeletePlatforma)

    def retranslateUi(self, DeletePlatforma):
        _translate = QtCore.QCoreApplication.translate
        DeletePlatforma.setWindowTitle(_translate("DeletePlatforma", "Dialog"))
        self.label.setText(_translate("DeletePlatforma", "Nazwa:"))
        self.label_2.setText(_translate("DeletePlatforma", "Usuwasz platformę"))
        self.pushButton.setText(_translate("DeletePlatforma", "Usuń"))

class Ui_AddWydawca(object):
    def setupUi(self, AddWydawca):
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

    def retranslateUi(self, AddWydawca):
        _translate = QtCore.QCoreApplication.translate
        AddWydawca.setWindowTitle(_translate("AddWydawca", "Dialog"))
        self.label.setText(_translate("AddWydawca", "Nazwa:"))
        self.label_2.setText(_translate("AddWydawca", "Dodajesz wydawcę"))
        self.pushButton.setText(_translate("AddWydawca", "Dodaj"))

class Ui_DeletePlatforma(object):
    def setupUi(self, DeletePlatforma):
        DeletePlatforma.setObjectName("DeletePlatforma")
        DeletePlatforma.resize(400, 130)
        self.lineEdit_nazwa = QtWidgets.QLineEdit(DeletePlatforma)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(30, 60, 113, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.label = QtWidgets.QLabel(DeletePlatforma)
        self.label.setGeometry(QtCore.QRect(40, 40, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DeletePlatforma)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 121, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(DeletePlatforma)
        self.pushButton.setGeometry(QtCore.QRect(300, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(DeletePlatforma)
        QtCore.QMetaObject.connectSlotsByName(DeletePlatforma)

    def retranslateUi(self, DeletePlatforma):
        _translate = QtCore.QCoreApplication.translate
        DeletePlatforma.setWindowTitle(_translate("DeletePlatforma", "Dialog"))
        self.label.setText(_translate("DeletePlatforma", "Nazwa:"))
        self.label_2.setText(_translate("DeletePlatforma", "Usuwasz wydawcę"))
        self.pushButton.setText(_translate("DeletePlatforma", "Usuń"))

class Ui_AddEvent(object):
    def setupUi(self, AddEvent):
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

    def retranslateUi(self, AddEvent):
        _translate = QtCore.QCoreApplication.translate
        AddEvent.setWindowTitle(_translate("AddEvent", "Dialog"))
        self.label.setText(_translate("AddEvent", "Dodajesz nowy event"))
        self.label_2.setText(_translate("AddEvent", "Nazwa"))
        self.label_3.setText(_translate("AddEvent", "Data"))
        self.label_4.setText(_translate("AddEvent", "Sekcja odpowiedzialna:"))
        self.pushButton.setText(_translate("AddEvent", "Dodaj"))
        self.label_5.setText(_translate("AddEvent", "Adres:"))

class Ui_DeleteEvent(object):
    def setupUi(self, DeleteEvent):
        DeleteEvent.setObjectName("DeleteEvent")
        DeleteEvent.resize(441, 143)
        self.label = QtWidgets.QLabel(DeleteEvent)
        self.label.setGeometry(QtCore.QRect(200, 10, 81, 20))
        self.label.setObjectName("label")
        self.lineEdit_nazwa = QtWidgets.QLineEdit(DeleteEvent)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.label_2 = QtWidgets.QLabel(DeleteEvent)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 51, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(DeleteEvent)
        self.pushButton.setGeometry(QtCore.QRect(350, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(DeleteEvent)
        QtCore.QMetaObject.connectSlotsByName(DeleteEvent)

    def retranslateUi(self, DeleteEvent):
        _translate = QtCore.QCoreApplication.translate
        DeleteEvent.setWindowTitle(_translate("DeleteEvent", "Dialog"))
        self.label.setText(_translate("DeleteEvent", "Usuwasz event"))
        self.label_2.setText(_translate("DeleteEvent", "Nazwa"))
        self.pushButton.setText(_translate("DeleteEvent", "Usuń"))

    def setupUi(self, UpdateEventSekcja):
        UpdateEventSekcja.setObjectName("UpdateEventSekcja")
        UpdateEventSekcja.resize(441, 143)
        self.label = QtWidgets.QLabel(UpdateEventSekcja)
        self.label.setGeometry(QtCore.QRect(200, 10, 81, 20))
        self.label.setObjectName("label")
        self.lineEdit_nazwa = QtWidgets.QLineEdit(UpdateEventSekcja)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
        self.label_2 = QtWidgets.QLabel(UpdateEventSekcja)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 51, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(UpdateEventSekcja)
        self.pushButton.setGeometry(QtCore.QRect(350, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(UpdateEventSekcja)
        QtCore.QMetaObject.connectSlotsByName(UpdateEventSekcja)

    def retranslateUi(self, UpdateEventSekcja):
        _translate = QtCore.QCoreApplication.translate
        UpdateEventSekcja.setWindowTitle(_translate("UpdateEventSekcja", "Dialog"))
        self.label.setText(_translate("UpdateEventSekcja", "Usuwasz event"))
        self.label_2.setText(_translate("UpdateEventSekcja", "Nazwa"))
        self.pushButton.setText(_translate("UpdateEventSekcja", "Usuń"))

class Ui_UpdateEventSekcja(object):
    def setupUi(self, UpdateEventSekcja):
        UpdateEventSekcja.setObjectName("UpdateEventSekcja")
        UpdateEventSekcja.resize(441, 143)
        self.label = QtWidgets.QLabel(UpdateEventSekcja)
        self.label.setGeometry(QtCore.QRect(120, 10, 241, 20))
        self.label.setObjectName("label")
        self.lineEdit_nazwa = QtWidgets.QLineEdit(UpdateEventSekcja)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
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

        self.retranslateUi(UpdateEventSekcja)
        QtCore.QMetaObject.connectSlotsByName(UpdateEventSekcja)

    def retranslateUi(self, UpdateEventSekcja):
        _translate = QtCore.QCoreApplication.translate
        UpdateEventSekcja.setWindowTitle(_translate("UpdateEventSekcja", "Dialog"))
        self.label.setText(_translate("UpdateEventSekcja", "Zmieniasz sekcje odpowiedzialną za event"))
        self.label_2.setText(_translate("UpdateEventSekcja", "Nazwa"))
        self.label_4.setText(_translate("UpdateEventSekcja", "Sekcja odpowiedzialna:"))
        self.pushButton.setText(_translate("UpdateEventSekcja", "Zmień"))

class Ui_UpdateMiejsceCena(object):
    def setupUi(self, UpdateMiejsceCena):
        UpdateMiejsceCena.setObjectName("UpdateMiejsceCena")
        UpdateMiejsceCena.resize(400, 143)
        self.label = QtWidgets.QLabel(UpdateMiejsceCena)
        self.label.setGeometry(QtCore.QRect(150, 10, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(UpdateMiejsceCena)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 161, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_adres = QtWidgets.QLineEdit(UpdateMiejsceCena)
        self.lineEdit_adres.setGeometry(QtCore.QRect(30, 60, 113, 20))
        self.lineEdit_adres.setObjectName("lineEdit_adres")
        self.lineEdit_cena = QtWidgets.QLineEdit(UpdateMiejsceCena)
        self.lineEdit_cena.setGeometry(QtCore.QRect(240, 60, 113, 20))
        self.lineEdit_cena.setObjectName("lineEdit_cena")
        self.label_3 = QtWidgets.QLabel(UpdateMiejsceCena)
        self.label_3.setGeometry(QtCore.QRect(40, 40, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(UpdateMiejsceCena)
        self.label_4.setGeometry(QtCore.QRect(250, 40, 81, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(UpdateMiejsceCena)
        self.pushButton.setGeometry(QtCore.QRect(300, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(UpdateMiejsceCena)
        QtCore.QMetaObject.connectSlotsByName(UpdateMiejsceCena)

    def retranslateUi(self, UpdateMiejsceCena):
        _translate = QtCore.QCoreApplication.translate
        UpdateMiejsceCena.setWindowTitle(_translate("UpdateMiejsceCena", "Dialog"))
        self.label_2.setText(_translate("UpdateMiejsceCena", "Zmieniasz cene wynajmu"))
        self.label_3.setText(_translate("UpdateMiejsceCena", "Adres"))
        self.label_4.setText(_translate("UpdateMiejsceCena", "Nowa cena"))
        self.pushButton.setText(_translate("UpdateMiejsceCena", "Zmień"))

class Ui_AddMiejsce(object):
    def setupUi(self, AddMiejsce):
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

    def retranslateUi(self, AddMiejsce):
        _translate = QtCore.QCoreApplication.translate
        AddMiejsce.setWindowTitle(_translate("AddMiejsce", "Dialog"))
        self.label.setText(_translate("AddMiejsce", "Dodajesz Miejsce naEvent"))
        self.label_2.setText(_translate("AddMiejsce", "Adres"))
        self.label_3.setText(_translate("AddMiejsce", "Cena"))
        self.label_4.setText(_translate("AddMiejsce", "Max osób"))
        self.pushButton.setText(_translate("AddMiejsce", "Dodaj"))

class Ui_AddSponsor(object):
    def setupUi(self, AddSponsor):
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

    def retranslateUi(self, AddSponsor):
        _translate = QtCore.QCoreApplication.translate
        AddSponsor.setWindowTitle(_translate("AddSponsor", "Dialog"))
        self.label.setText(_translate("AddSponsor", "Dodajesz sponsora"))
        self.label_2.setText(_translate("AddSponsor", "Nazwa"))
        self.pushButton.setText(_translate("AddSponsor", "Dodaj"))

class Ui_AddSponsoring(object):
    def setupUi(self, AddSponsoring):
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
        self.lineEdit_nazwa = QtWidgets.QLineEdit(AddSponsoring)
        self.lineEdit_nazwa.setGeometry(QtCore.QRect(20, 80, 113, 20))
        self.lineEdit_nazwa.setObjectName("lineEdit_nazwa")
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

        self.retranslateUi(AddSponsoring)
        QtCore.QMetaObject.connectSlotsByName(AddSponsoring)

    def retranslateUi(self, AddSponsoring):
        _translate = QtCore.QCoreApplication.translate
        AddSponsoring.setWindowTitle(_translate("AddSponsoring", "Dialog"))
        self.label.setText(_translate("AddSponsoring", "Dodajesz sponsoring"))
        self.label_2.setText(_translate("AddSponsoring", "Nazwa"))
        self.pushButton.setText(_translate("AddSponsoring", "Dodaj"))
        self.label_3.setText(_translate("AddSponsoring", "Event:"))
        self.label_4.setText(_translate("AddSponsoring", "Kwota"))

class Ui_AddTurniej(object):
    def setupUi(self, AddTurniej):
        AddTurniej.setObjectName("AddTurniej")
        AddTurniej.resize(401, 154)
        self.label = QtWidgets.QLabel(AddTurniej)
        self.label.setGeometry(QtCore.QRect(160, 10, 101, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(AddTurniej)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 101, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(AddTurniej)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 70, 71, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
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

    def retranslateUi(self, AddTurniej):
        _translate = QtCore.QCoreApplication.translate
        AddTurniej.setWindowTitle(_translate("AddTurniej", "Dialog"))
        self.label.setText(_translate("AddTurniej", "Dodajesz turniej"))
        self.label_2.setText(_translate("AddTurniej", "Nazwa"))
        self.label_3.setText(_translate("AddTurniej", "Godzina"))
        self.label_4.setText(_translate("AddTurniej", "Event:"))
        self.pushButton.setText(_translate("AddTurniej", "Dodaj"))

class Ui_DeleteTurniej(object):
    def setupUi(self, DeleteTurniej):
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

    def retranslateUi(self, DeleteTurniej):
        _translate = QtCore.QCoreApplication.translate
        DeleteTurniej.setWindowTitle(_translate("DeleteTurniej", "Dialog"))
        self.label.setText(_translate("DeleteTurniej", "Usuwasz Turniej"))
        self.pushButton.setText(_translate("DeleteTurniej", "Usuń"))
        self.label_2.setText(_translate("DeleteTurniej", "Nazwa"))
        self.label_3.setText(_translate("DeleteTurniej", "Event:"))

class Ui_AddUczestnik(object):
    def setupUi(self, AddUczestnik):
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

    def retranslateUi(self, AddUczestnik):
        _translate = QtCore.QCoreApplication.translate
        AddUczestnik.setWindowTitle(_translate("AddUczestnik", "Dialog"))
        self.label.setText(_translate("AddUczestnik", "Dodajesz uczestnika turnieju"))
        self.label_2.setText(_translate("AddUczestnik", "Imie"))
        self.label_3.setText(_translate("AddUczestnik", "Nazwisko"))
        self.label_4.setText(_translate("AddUczestnik", "Event:"))
        self.label_5.setText(_translate("AddUczestnik", "Turniej:"))
        self.pushButton.setText(_translate("AddUczestnik", "Dodaj"))

class Ui_DeleteUczestnik(object):
    def setupUi(self, DeleteUczestnik):
        DeleteUczestnik.setObjectName("DeleteUczestnik")
        DeleteUczestnik.resize(400, 137)
        self.label = QtWidgets.QLabel(DeleteUczestnik)
        self.label.setGeometry(QtCore.QRect(140, 10, 111, 20))
        self.label.setObjectName("label")
        self.lineEdit_id_uczestnika = QtWidgets.QLineEdit(DeleteUczestnik)
        self.lineEdit_id_uczestnika.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.lineEdit_id_uczestnika.setObjectName("lineEdit_id_uczestnika")
        self.label_2 = QtWidgets.QLabel(DeleteUczestnik)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 101, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(DeleteUczestnik)
        self.pushButton.setGeometry(QtCore.QRect(300, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(DeleteUczestnik)
        QtCore.QMetaObject.connectSlotsByName(DeleteUczestnik)

    def retranslateUi(self, DeleteUczestnik):
        _translate = QtCore.QCoreApplication.translate
        DeleteUczestnik.setWindowTitle(_translate("DeleteUczestnik", "Dialog"))
        self.label.setText(_translate("DeleteUczestnik", "Usuwasz uczestnika"))
        self.label_2.setText(_translate("DeleteUczestnik", "Id_uczestnika"))
        self.pushButton.setText(_translate("DeleteUczestnik", "Usuń"))

class Ui_AddWygrany(object):
    def setupUi(self, AddWygrany):
        AddWygrany.setObjectName("AddWygrany")
        AddWygrany.resize(619, 155)
        self.label = QtWidgets.QLabel(AddWygrany)
        self.label.setGeometry(QtCore.QRect(240, 10, 151, 20))
        self.label.setObjectName("label")
        self.lineEdit_id_uczestnika = QtWidgets.QLineEdit(AddWygrany)
        self.lineEdit_id_uczestnika.setGeometry(QtCore.QRect(20, 70, 113, 20))
        self.lineEdit_id_uczestnika.setObjectName("lineEdit_id_uczestnika")
        self.comboBox_event = QtWidgets.QComboBox(AddWygrany)
        self.comboBox_event.setGeometry(QtCore.QRect(150, 70, 101, 22))
        self.comboBox_event.setObjectName("comboBox_event")
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

class Ui_DeleteWygrany(object):
    def setupUi(self, DeleteWygrany):
        DeleteWygrany.setObjectName("DeleteWygrany")
        DeleteWygrany.resize(423, 155)
        self.label = QtWidgets.QLabel(DeleteWygrany)
        self.label.setGeometry(QtCore.QRect(170, 10, 151, 20))
        self.label.setObjectName("label")
        self.lineEdit_id_uczestnika = QtWidgets.QLineEdit(DeleteWygrany)
        self.lineEdit_id_uczestnika.setGeometry(QtCore.QRect(20, 70, 113, 20))
        self.lineEdit_id_uczestnika.setObjectName("lineEdit_id_uczestnika")
        self.comboBox_event = QtWidgets.QComboBox(DeleteWygrany)
        self.comboBox_event.setGeometry(QtCore.QRect(150, 70, 101, 22))
        self.comboBox_event.setObjectName("comboBox_event")
        self.comboBox_turniej = QtWidgets.QComboBox(DeleteWygrany)
        self.comboBox_turniej.setGeometry(QtCore.QRect(270, 70, 101, 22))
        self.comboBox_turniej.setObjectName("comboBox_turniej")
        self.label_2 = QtWidgets.QLabel(DeleteWygrany)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DeleteWygrany)
        self.label_3.setGeometry(QtCore.QRect(160, 50, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(DeleteWygrany)
        self.label_4.setGeometry(QtCore.QRect(280, 50, 51, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(DeleteWygrany)
        self.pushButton.setGeometry(QtCore.QRect(330, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(DeleteWygrany)
        QtCore.QMetaObject.connectSlotsByName(DeleteWygrany)

    def retranslateUi(self, DeleteWygrany):
        _translate = QtCore.QCoreApplication.translate
        DeleteWygrany.setWindowTitle(_translate("DeleteWygrany", "Dialog"))
        self.label.setText(_translate("DeleteWygrany", "Usuwasz wygranego"))
        self.label_2.setText(_translate("DeleteWygrany", "Id_uczestnika"))
        self.label_3.setText(_translate("DeleteWygrany", "Event:"))
        self.label_4.setText(_translate("DeleteWygrany", "Turniej:"))
        self.pushButton.setText(_translate("DeleteWygrany", "Usuń"))
