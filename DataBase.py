# -*- coding: utf-8 -*-
import sqlite3


class DataBase:
    def __init__(self):
        self.db = sqlite3.connect("Data.db")
        self.c = self.db.cursor()

    def query(self, column, table, query, where):
        #print self.c.execute("SELECT * FROM spells WHERE classes LIKE ? and level=? ", ("%Wizard%",6 ))
        self.c.execute("SELECT " + column + " FROM " + table + " WHERE " + query, where)
        rows = self.c.fetchall()
        return rows

    def query_spell(self, query_rows, query_values):
        return self.query("*", "spells", query_rows, query_values)

    # Since the file has been encoded differently to what was expected the ' is stored as â€™ which this changes
    def replace_odd_values(self, where):
        self.c.execute('''UPDATE spells SET ''' + where + '''= replace( ''' + where + ''', "â€™", "\'")''')
        self.db.commit()

    def replace_handle(self):
        self.replace_odd_values("desc")
        self.replace_odd_values("higher_level")
        self.replace_odd_values("name")
        self.replace_odd_values("material")

