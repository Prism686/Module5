import pymongo
from pymongo import MongoClient

URL="mongodb+srv://admin:admin@cluster0.ec94c0b.mongodb.net/?retryWrites=true&w=majority"
client=MongoClient(URL)
db=client.pytech
print(db.list_collection_names)
