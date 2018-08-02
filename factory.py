"""
    Example of a factory design pattern.
    Can be a class or a method.
"""

from .adapter import MySQLAdapter, MongoAdapter

def get_DB(type='mysql'):
    """
        Documentation

        Parameters
        --------------
        type: 'mysql', 'mongodb

        Returns
        --------------
        db: database adapter class (DBAdapter)

    """

    if type == 'mysql':
        # import MySQL
        return MySQLAdapter()

    elif type == 'mongodb':
        # import MongoDB

        # read config file, pass parameters...
        # could be complicated
        return MongoAdapter()





