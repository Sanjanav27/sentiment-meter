from pymongo import MongoClient
import pymongo
client=MongoClient('mongodb+srv://sanju:<password>@cluster0.wllvz.mongodb.net/<dbname>?retryWrites=true&w=majority')
db=client.get_database("sentiment_meter")
records=db.words
