import datetime
from PyQt5.QtWidgets import QMessageBox

relations = ["Sekcje_view", "Czlonkowie", "Spotkanie_view", "Placowki_view",
            "Egzemplarz_view", "Gry_komputerowe_view", "Gry_planszowe_view",
            "Platformy_view", "Wydawcy_view",
            "Event_view", "Miejsca", "Sponsorzy_view", "Turnieje_view",
            "Uczestnicy_turniejow_view", "Miejsce_w_turnieju_view", "Gry", "Sponsorowanie", "Gry_uzywanie", "Czlonkowie_w_sekcjach"]

basic_relations = ["Sekcje", "Czlonkowie", "Spotkania", "Placowki", "Egzemplarz", "Gry_komputerowe", "Gry_planszowe", "Platformy", "Wydawcy", "Eventy", "Miejsca", "Sponsorzy", "Turnieje", "Uczestnicy_turniejow", "Miejsce_w_turnieju", "Gry", "Sponsorowanie", "Gry_uzywanie", "Czlonkowie_w_sekcjach"]

def get_table(i, connection):
    data, headers = connection.select(relations[i])

    if data == []:
        data = [["Brak danych"]]

    for i in range(len(data)):
        data[i] = [str(val) for val in data[i]]

    return (data, headers)


def add_record(connection, i:int , record: list):
    #QUESTION: what if already exists?
    proc_name = basic_relations[i] + "_add"
    connection.exec_procedure(proc_name, record)
    # connection.insert(relations[i], record)


def get_names(connection, i: int, colname: str):
    data, _ = connection.select(relations[i], [colname])
    if data != []:
        data = [d[0] for d in data]
    return data


def remove_record(connection, i: int, condition: str):
    proc_name = basic_relations[i] + "_delete"
    connection.exec_procedure(proc_name, record)
    # connection.delete(relations[i], condition)


def update_record(connection, i: int, new: str, condition: str):
    # connection.update(relations[i], new, condition)
    proc_name = basic_relations[i] + "_update"
    connection.exec_procedure(proc_name, record)



def show_popup(text):
    msg = QMessageBox()
    msg.setWindowTitle("Wrong input")
    msg.setText(text)
    msg.setIcon(QMessageBox.Critical)
    x = msg.exec_()

def validate_number(promised_number):
    #TODO: przecinki
    if promised_number.isdigit() or promised_number == "":
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
