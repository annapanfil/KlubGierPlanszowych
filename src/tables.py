import datetime
from PyQt5.QtWidgets import QMessageBox

relations = ["Sekcje_view", "Czlonkowie", "Spotkania", "Placowki_view", "Egzemplarze_view", 
            "Gry_komputerowe", "Gry_planszowe", "Platformy_view", "Wydawcy_view", 
            "Eventy_view", "Miejsca", "Sponsorzy_view", "Turnieje_view", 
            "Uczestnicy_turniejow_view", "Miejsca_w_turniejach_view", "Gry", "Sponsorowanie", 
            "Gry_uzywanie", "Czlonkowie_w_sekcjach"]

def get_table(i, connection):
    data, headers = connection.select(relations[i])

    if data == []:
        data = [["Brak danych"]]

    for i in range(len(data)):
        data[i] = [str(val) for val in data[i]]

    return (data, headers)


def add_record(connection, i:int , record: list):
    #QUESTION: what if already exists?
    connection.insert(relations[i], record)


def get_names(connection, i: int, colname: str):
    data, _ = connection.select(relations[i], [colname])
    if data != []:
        data = data[0]
    return data


def remove_record(connection, i: int, condition: str):
    connection.delete(relations[i], condition)


def update_record(connection, i: int, new: str, condition: str):
    connection.update(relations[i], new, condition)



def show_popup(text):
    msg = QMessageBox()
    msg.setWindowTitle("Wrong input")
    msg.setText(text)
    msg.setIcon(QMessageBox.Critical)
    x = msg.exec_()

def validate_number(promised_number):
    #TODO: przecinki
    if promised_number.isdigit():
        return promised_number
    else:
        show_popup(f"Niepoprawna liczba: '{promised_number}'")
        return None

def validate_date(promised_date):
    try:
        datetime.datetime.strptime(promised_date, '%Y-%m-%d')
        return promised_date
    except ValueError:
        show_popup("Niepoprawny format daty, spodziewany format to RRRR-MM-DD")
        return None

def validate_hour(promised_hour):
    #TODO
    return promised_hour

def validate_text(promised_text):
    #TODO: not sql injection
    return promised_text
