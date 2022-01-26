relations = ["Sekcje_view", "Czlonkowie", "Spotkania", "Placowki_view", "Egzemplarze_view", "Gry_komputerowe", "Gry_planszowe", "Platformy_view", "Wydawcy_view", "Eventy_view", "Miejsca", "Sponsorzy_view", "Turnieje_view", "Uczestnicy_turniejow_view", "Miejsca_w_turniejach_view"]

def get_table(i, connection):
    data, headers = connection.select(relations[i])

    if data == []:
        data = [["Brak danych"]]

    for i in range(len(data)):
        data[i] = [str(val) for val in data[i]]

    return (data, headers)

def add_record(connection, i, record):
    #QUESTION: what if already exists?
    connection.insert(relations[i], record)
