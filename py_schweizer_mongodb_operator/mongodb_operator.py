from pymongo import MongoClient

__all__ = ['MongoDbOperator']


class MongoDbOperator:
    """
        Get a MongoDbOperator instance by 'operator=MongoDbOperator('db_name',arg1="",arg2="",..,..,..,..)',
        Then, get the
    """

    def __init__(self, db_name, db_url="127.0.0.1", db_port=27017, db_username="username",
                 db_password="password",
                 db_if_auth=True, db_auth_dbname="admin"):
        print "Default args are db_name"
        self.db_name = db_name
        self.db_url = db_url
        self.db_port = db_port
        self.db_username = db_username
        self.db_password = db_password
        self.db_if_auth = db_if_auth
        self.db_auth_dbname = db_auth_dbname
        self.db = None

    def get_mongodb_client(self):
        db_client = MongoClient(self.db_url, self.db_port)
        if self.db_if_auth:
            db_client[self.db_auth_dbname].authenticate(self.db_username, self.db_password, mechanism='SCRAM-SHA-1')
        self.db = db_client[self.db_name]

    def collection_drop(self, list_reserve):
        """
        Drop all Collections besides the collections in 'list_reserve'
        """
        if self.db is not None:
            collection_names = self.db.collection_names()
            for collection in collection_names:
                if collection not in list_reserve:
                    self.db.drop_collection(collection)
                    print "Droped collection names:%s" % collection
        else:
            print "Db client for %s db not initialized yet!" % self.db_name

    def collection_create(self, list_targets):
        if self.db is not None:
            for collection in list_targets:
                self.db[collection].insert({})
                print "Created collection names:%s" % collection
        else:
            print "Db client for %s db not initialized yet!" % self.db_name

