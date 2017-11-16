import os
from py_schweizer_mongodb_operator.mongodb_operator import *

if __name__ == '__main__':
    db_operator = MongoDbOperator('my_db')
    db_operator.get_mongodb_client()
    db_operator.collection_drop(["", ""])
