from pymongo import MongoClient

def get_database():

    connection_string = "mongodb+srv://vivi:vivi@cluster0.5wz3u8j.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
    return client["products"]


if __name__ == "__main__":   

    get_database()





