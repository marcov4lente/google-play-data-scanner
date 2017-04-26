import sqlite3

class DBAdapter:

    def __init__(self):
        self.connection = sqlite3.connect('data.db')
        self.cursor = self.connection.cursor()
        query = 'CREATE TABLE IF NOT EXISTS top_apps (id INTEGER PRIMARY KEY, name TEXT, developer TEXT, rank INTEGER, url TEXT, created TEXT DEFAULT current_timestamp);'
        self.cursor.execute(query)

    def insert(self, table_name, data):
        field_count = len(data)

        query = ' INSERT INTO '+table_name+' ( '

        i = 1
        for index, value in data.items():
            query += index
            if(i < field_count):
                query += ', '
            i = i + 1

        query += ' ) VALUES ( '

        i = 1
        for index, value in data.items():
            query += '?'
            if(i < field_count):
                query += ', '
            i = i + 1

        query += ' ) '

        params = []

        for index, value in data.items():
            params.append(value)

        self.cursor.execute(query, params)
	self.connection.commit()
