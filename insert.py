from PyMongoDriver import get_database

dbProducts = get_database()

collection = dbProducts["products"]


new_books = [
   {
      "title" : "New book",
      "price" : 6.99,
      "year" : 2020
   },
   {
      "title" : "Old book",
      "price" : 34.59
   }
]



result = collection.insert_many(new_books)
inserted_docs_id = result.inserted_ids
print("total of inserted documents" + str(len(inserted_docs_id)))
print(f"id of inserted docs: {inserted_docs_id}")




