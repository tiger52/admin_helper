#!/usr/bin/env python

from pymongo import MongoClient
import random


class MongoDB(object):
    def __init__(self):
        #self.mongo_host = "127.0.0.1"
        #self.mongo_host = "k21-dev-dmetrics.dev.oll.tv"
        self.mongo_host = "k21-dm-mg1.prod.oll.tv"
        #self.mongo_host = "g50-dm-mg1.prod.oll.tv"
        self.mongo_port = 27017
        self.mongo_db = ["admin", "testbase"]
        self.mongo_user = "admin"
        self.mongo_password = "mongo4DS"
        #self.mongo_user = None
        #self.mongo_password = None
        self.__conn = None
        self.__dbnames = None
        self.__metrics = []


    def connect(self):
        if self.__conn is None:
            try:
                self.__conn = MongoClient(host=self.mongo_host, port=self.mongo_port)
		print "Connected successfully!!!"
            except Exception as e:
                print 'Error in MongoDB connection: %s' % str(e)
    def close(self):
        if self.__conn is not None:
            self.__conn.close()
    # Get a list of DB names
    def getDBNames(self):
        if self.__conn is None:
            self.connect()
        db = self.__conn[self.mongo_db[0]]
        if self.mongo_user and self.mongo_password:
            db.authenticate(self.mongo_user, self.mongo_password)
        master = db.command('isMaster')['ismaster']
	print "isMaster: {}".format(master)
        dict = {}
        dict['key'] = 'mongodb.ismaster'
        DBList = []
        if master:
            dict['value'] = 1
            DBNames = self.__conn.database_names()
            self.__dbnames = DBNames
        else:
            dict['value'] = 0
	    DBNames = ""
        self.__metrics.append(dict)
        print "DBList: {}\nmetrics: {}\nnames: {}\n".format(DBList, self.__metrics, DBNames)

    def getTestQuery(self):
        if self.__conn is None:
            self.connect()
	    print "connect to db"
        db = self.__conn[self.mongo_db[0]]
        if self.mongo_user and self.mongo_password:
            print "authorizing..."
            authecho = db.authenticate(self.mongo_user, self.mongo_password)
	    print "authorized: {}".format(authecho)
#        db2 = self.__conn[self.mongo_db[1]]
#	collections = db2.collection_names()
#	print "collection: {}".format(collections)
#	result = db2.qwerty
#	result.insert([ {"qwe":"newone", "asd": random.randrange(1000)} ])
#	for result in result.find():
#	    print result
#	#print "result: {}".format(result.find())

if __name__ == '__main__':
    MongoDB = MongoDB()
    #MongoDB.getDBNames()
    MongoDB.getTestQuery()
    print "some: {}".format(MongoDB.getDBNames())
    MongoDB.close()

