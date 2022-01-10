from datetime import datetime
import certifi
from pymongo import MongoClient


class MongoCRUD:
    def __init__(self):
        self._connectionString = "mongodb+srv://admin:7pbKRmqoSyVmQTpXrEtdmo7xO@cluster0.z5ix9.mongodb.net/discordDB?retryWrites=true&w=majority"
        self.client = MongoClient(self._connectionString, tlsCAFile=certifi.where())
        self.db = self.client["discordDB"]
        self.collection = self.db["questions"]

    def createPost(self, items: dict):
        self.collection.insert_one(items)

    def readPost(self, filters: dict):
        self.collection.find_one(filters)

    def updatePost(self, filter, update):
        self.collection.update_one(filter, update)

    def deletePost(self, collectionToDelete):
        self.collection.delete_one(collectionToDelete)


if __name__ == "__main__":

    mon = MongoCRUD()
    # mon.createPost(
    #     {
    #         "questionText": "What is your fav animal",
    #         "creationDate": datetime.today().replace(microsecond=0),
    #         "user" : "PerryBot",
    #         "used": False
    #     }
    # )
    
