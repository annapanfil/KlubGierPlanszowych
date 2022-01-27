# pip install mysql.connector

import mysql.connector
import getpass
import logging

class MyConnection():
    def __init__(self, login:str, passwd:str, host:str, db_name="KlubGierPlanszowych"):

        # login = input("nazwa użytkownika: ")
        # passwd = getpass.getpass("Hasło: ")
        self.connection = None

        try:
            self.connection = mysql.connector.connect(user=login, password=passwd, database=db_name, host = host) # default host is localhost
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                logging.error("Wrong credentials")
            else:
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
            data = [["Tabela nie istnieje"]]
            headers = [""]
        finally:
            cursor.close()


        return (data, headers)


    def insert(self, table: str, values: list, cols=None):
        # values -- list  of values to insert
        # cols -- list of columns to which values refer
        # eg. connection.insert("Gry", ("Carcassone", 200, "xyz"), ("nazwa", "cena", "wydawca"))

        query = f"INSERT INTO {table}"
        if cols: query += f" ({', '.join(cols)})"

        # surround strings with ""
        for i, val in enumerate(values):
            if isinstance(val, str):
                values[i] = '"' + val + '"'
            else:
                values[i] = str(val)

        query += f""" VALUES ({', '.join(values)})"""

        logging.info(query)

        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            cursor.execute(f"select * from {table}")
            data = cursor.fetchall()
            logging.info(data)
        except mysql.connector.errors.DatabaseError as err:
            logging.error(err)
        except mysql.connector.errors.ProgrammingError as err:
            logging.error(err)
        cursor.close()
        self.connection.commit()


    def delete(self, table: str, condition: str):
        # eg. conn.select("Gry", ("nazwa", "cena"))

        query = f"DELETE FROM {table} WHERE {condition}"

        logging.info(query)

        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
        except mysql.connector.errors.ProgrammingError as err:
            logging.error(err)
        except mysql.connector.errors.DatabaseError as err:
            logging.error(err)

        cursor.close()
        self.connection.commit()

    def update(self, table: str, result: str, condition: str):
        query = f"UPDATE {table} SET {result} WHERE {condition}"

        logging.info(query)

        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
        except mysql.connector.errors.ProgrammingError as err:
            logging.error(err)
        except mysql.connector.errors.DatabaseError as err:
            logging.error(err)


        cursor.close()
        self.connection.commit()


    def exec_procedure(self, proc_name, args):
        logging.info(f"Execute procedure {proc_name} ({args})")

        cursor = self.connection.cursor()
        try:
            cursor.callproc(proc_name, args=args)
        except mysql.connector.errors.ProgrammingError as err:
            logging.error(err)
        except mysql.connector.errors.DatabaseError as err:
            logging.error(err)


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
