from PyMongoDriver import get_database
import pprint

dbProducts = get_database()

collection = dbProducts["products"]

doc1 = {"title": "New book"}
searchParameter = {"title" : ["New book", "Old book"]}

query_docs = collection.find(doc1)
print("Searching for sample target document before delete: ")
for item in query_docs:
   print(item)


"""
cursor = accounts_collection.find(documents_to_find)

num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()
print("# of documents found: " + str(num_docs))
"""