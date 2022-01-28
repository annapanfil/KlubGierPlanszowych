# pip install mysql.connector

import mysql.connector
import getpass
import logging
from tables import show_popup

class MyConnection():
    def __init__(self, login:str, passwd:str, host:str, db_name="KlubGierPlanszowych"):

        # login = input("nazwa użytkownika: ")
        # passwd = getpass.getpass("Hasło: ")

        passwd = "DB12345"
        self.connection = None

        try:
            self.connection = mysql.connector.connect(user=login, password=passwd, database=db_name, host = host) # default host is localhost
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                logging.error("Wrong credentials")
                show_popup("Niepoprawne dane logowania")
            else:
                show_popup("Nie można połączyć z bazą danych")
                logging.error(err)
            exit(1)


    def select(self, table: str, cols='*', condition=None):
        # cols -- list or tuple
        # condition -- string
        # eg. data = conn.select("Gry", ("nazwa", "cena"), "cena = 100")

        cursor = self.connection.cursor()
        query = f"SELECT {', '.join(cols)} FROM {table}"
        if condition: query += f" WHERE {condition}"
        logging.info(query)

        try:
            cursor.execute(query)
            data = cursor.fetchall() # fetchone(), fetchmany(n)
            headers = [col[0] for col in cursor.description]
        except mysql.connector.errors.ProgrammingError as err:
            logging.error(f"Table {table} does not exist")
            show_popup("Tabela nie istnieje lub nie ma takiej kolumny")
            data = [["Tabela nie istnieje"]]
            headers = [""]
        finally:
            cursor.close()


        return (data, headers)

    def exec_procedure(self, proc_name, args):
        logging.info(f"Execute procedure {proc_name} ({args})")

        cursor = self.connection.cursor()
        # try:
        cursor.callproc(proc_name, args=args)
        # except mysql.connector.errors.ProgrammingError as err:
        #     logging.error(err)
        # except mysql.connector.errors.DatabaseError as err:
        #     logging.error(err)


        cursor.close()
        self.connection.commit()


    def __del__(self):
        logging.debug("Closing connection...")
        if self.connection is not None:
            self.connection.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    conn = MyConnection()
    conn.insert("Gry", ["Carcassone", 200, "xyz"], ("nazwa", "cena", "wydawca"))
    conn.select("Gry", ("nazwa", "cena"))
    conn.delete("Gry", 'nazwa="Carcassone"')
    conn.select("Gry", ("nazwa", "cena"))
