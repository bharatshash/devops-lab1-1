import os

from pymongo import MongoClient

# MONGO_URI  = "mongodb://user:password@mongo:27017/?directConnection=true"


MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo-studentdb-service/student_db")
client = MongoClient(MONGO_URI)


# client = MongoClient(MONGO_URI)
# client = MongoClient('localhost', 27017)
db = client['student_service']

if 'students' not in db.list_collection_names():
    db.create_collection('students')

students_collection = db['students']
