from datetime import datetime
import certifi
from pymongo import MongoClient


class MongoCRUD:
    def __init__(self):
        self._connectionString = "mongodb+srv://admin:7pbKRmqoSyVmQTpXrEtdmo7xO@cluster0.z5ix9.mongodb.net/discordDB?retryWrites=true&w=majority"
        self.client = MongoClient(self._connectionString, tlsCAFile=certifi.where())
        self.db = self.client["discordDB"]
        self.collection = self.db["questions"]

    def _createPost(self, items: dict):
        self.collection.insert_one(items)

    def _readPost(self, filters: dict):
        self.collection.find_one(filters)

    def _updatePost(self, filter, update):
        self.collection.update_one(filter, update)

    def _deletePost(self, collectionToDelete):
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
    
