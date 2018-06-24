import sqlite3


class DataBase:
    def __init__(self):
        self.db = sqlite3.connect("Data.db")
        self.c = self.db.cursor()

    def query(self, column, table, query, where):
        return self.c.execute("SELECT " + column + " FROM " + table + " WHERE " + query, where)

    def query_spell(self, query_rows, query_values):
        return self.query("*", "spells", query_rows, query_values)


data = DataBase()
rows = data.query_spell("material != ? AND  components != ? ", ("n/a", 'S'))
