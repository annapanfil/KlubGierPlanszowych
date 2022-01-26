import datetime

relations = ["Sekcje_view", "Czlonkowie", "Spotkania", "Placowki_view", "Egzemplarze_view", "Gry_komputerowe", "Gry_planszowe", "Platformy_view", "Wydawcy_view", "Eventy_view", "Miejsca", "Sponsorzy_view", "Turnieje_view", "Uczestnicy_turniejow_view", "Miejsca_w_turniejach_view", "Gry", "Sponsorowanie"]

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


def validate_number(promised_number):
    if promised_number.isdigit():
        return promised_number
    else:
        #TODO: popup
        return None

def validate_date(promised_date):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        parsed_date = promised_date
        return parsed_date
    except ValueError:
        #TODO: popup
        print("Incorrect data format, should be YYYY-MM-DD")
        return None

def validate_text(promised_text):
    #TODO: not sql injection
    return promised_text
