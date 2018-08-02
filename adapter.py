"""
    Adapter design pattern
"""

from abc import ABC, abstractmethod

class MySQL:

    def connect_to_DB(self, uri):
        print('Many steps to connect to DB...')

    def run_query(self, query):
        print('MySQL specific query')

class MongoDB:

    def create_connection(self, uri):
        print('Many steps to connect to MongoDB...')

    def query_DB(self, query):
        print('MongoDB specific query')

#---------------------------------------------

class DBAdapter(ABC):

    @abstractmethod
    def connect(self, path, username, password):
        pass

    @abstractmethod
    def query(self, text):
        pass

#--------------------------------------------

class MySQLAdapter(DBAdapter):

    def __init__(self):
        self.database = MySQL()

    def connect(self, path, username, password):
        print('Connecting to mysql')
        uri = "{}:{}".format(path, username, password)
        self.database.connect_to_DB(uri)

    def query(self, text):
        print('Running mysql query.')
        self.database.run_query(text)


class MongoAdapter(DBAdapter):

    def __init__(self):
        self.database = MongoDB()

    def connect(self, path, username, password):
        print('Connecting to mysql')
        uri = "{}:{}".format(path, username, password)
        self.database.connect_to_DB(uri)

    def query(self, text):
        print('Running mysql query.')
        self.database.run_query(text)

#-------------------------------------------------

db = MySQLAdapter()

db.connect('some path', 'user', 'password')
db.query('AMBER')


