from pymongo import MongoClient

# Connect to MongoDB
print("Connecting to MongoDB...")
connecturl = 'mongodb://localhost:27017/'

# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# select the 'training' database 
db = connection.training

# select the 'python' collection 
collection = db.mongodb_glossary  # You named this 'collection' variable

# create documents
doc1 = {"database": "a database contains collections"}
doc2 = {"collection": "a collection stores the documents"}
doc3 = {"document": "a document contains the data in the form of key value pairs."}

# insert documents - FIXED: Use the 'collection' variable
print("Inserting documents into collection.")
collection.insert_one(doc1)  # ✅
collection.insert_one(doc2)  # ✅
collection.insert_one(doc3)  # ✅

# query for all documents - FIXED: Use the 'collection' variable
docs = collection.find()  # ✅

print("Printing the documents in the collection.")
for document in docs:
    print(document)

# close the server connection
print("Closing the connection.")
connection.close()