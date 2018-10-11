import sqlite3


class Sqlite(object):
    def __init__(self):
        self.db = sqlite3.connect(':memory:')
        self.cursor = self.db.cursor()


    def create_table(self, table_name, columns):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS %s
            (%s)
        ''' % (table_name, ','.join(columns)))
        self.db.commit()
    
    def insert_rows(self, table_name, columns, rows):
        self.cursor.executemany('''
            INSERT INTO %s (%s)
            VALUES 
            (%s);
        ''' % (table_name, ','.join(columns), ('?,' * len(columns)).strip(',')), rows)
        self.db.commit()
    
    def execute(self, query):
        return self.cursor.execute(query)