from pymongo import MongoClient

class OidsRepository:
    def __init__(self, mongo_config):
        self._client = MongoClient(host=mongo_config['host'], port=mongo_config['port'])
        self._oids = self._client[mongo_config['database']][mongo_config['collection']]

    def contains_oid(self, oid):
        return self._oids.find({'oid': oid}).count()

    def add_oid(self, oid):
        self._oids.insert_one({'oid': oid})

    def delete_oid(self, oid):
        self._oids.delete_many({'oid': oid})

    def clear(self):
        self._oids.remove()

