import sqlite3


class DataBase:
    def __init__(self, **kwargs):
        self.dbs = kwargs.get('db')
        self.table = kwargs.get('table')
        self.rows = kwargs.get('rows')
        self.values = kwargs.get('values')
        if self.dbs:
            self.db = sqlite3.connect(f'{self.dbs}')
        else:
            self.db = sqlite3.connect('dbs/db.db')
        self.connect = self.db.cursor()

    def add(self):
        self.connect.execute(f"INSERT INTO {self.table}({self.rows}) VALUES({self.values})")
        self.db.commit()

    def get(self):
        if self.rows:
            self.connect.execute(f"SELECT {self.rows} FROM {self.table}")
            data = self.connect.fetchall()
        else:
            self.connect.execute(f"SELECT * FROM {self.table}")
            data = self.connect.fetchall()
        return data

    def search(self):
        if self.rows:
            self.connect.execute(f"SELECT {self.rows} FROM {self.table} WHERE {self.values}")
            data = self.connect.fetchall()
        else:
            self.connect.execute(f"SELECT * FROM {self.table} WHERE {self.values}")
            data = self.connect.fetchall()
        return data

    def replace(self):
        self.connect.execute(f"REPLACE INTO {self.table}({self.rows}) VALUES({self.values})")
        self.db.commit()

    def update(self, search=None):
        if search:
            self.connect.execute(f"UPDATE {self.table} SET '{self.rows}'='{self.values}' WHERE {search[0]}={search[1]}")
        else:
            self.connect.execute(f"UPDATE {self.table} SET '{self.rows}'='{self.values}'")
        self.db.commit()

    def delete(self):
        self.connect.execute(f"DELETE FROM {self.table} WHERE {self.rows}={self.values}")
        self.db.commit()
