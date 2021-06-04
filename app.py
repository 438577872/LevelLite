from _sqlite3 import connect


# from os import mkdir
# import os
# os.dir

class LevelLite(object):
    def __init__(self, name: str):
        # path = name.split('/')

        self.__conn = connect(name)
        self.__cur = self.__conn.cursor()
        self.__cur.execute('select * from sqlite_master where type="table" and name = "leveldb"')
        table = self.__cur.fetchone()
        if not table:
            self.__cur.execute('create table leveldb('
                               'key text primary key,'
                               'val text'
                               ')')
            self.__cur.execute('CREATE INDEX index_name ON leveldb (key);')
            self.__conn.commit()

    def get(self, key):
        self.__cur.execute('select val from leveldb where key = ? limit 1', [key])
        one = self.__cur.fetchone()
        if one:
            res = one[0]
        else:
            res = None
        return res

    def put(self, key, val):
        self.__cur.execute('delete from leveldb where key = ?', [key])
        self.__cur.execute('insert into leveldb values(?,?)', [key, val])
        self.__conn.commit()
        return val

    def delete(self, key):
        self.__cur.execute('delete from leveldb where key = ?', [key])
        self.__conn.commit()

    def getInt(self, key):
        return int(self.get(key))

    def getFloat(self, key):
        return float(self.get(key))

    def getDictionary(self, key) -> dict:
        return eval(self.get(key))

# class LevelDb(object):
#     def __init__(self):
#         # from leveldb import
#         pass
#
#     def put(self):
#         pass
#
#     def get(self):
#         pass
#
#     def
