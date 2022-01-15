import certifi
from pymongo import MongoClient

class MongoCRUD:
    def __init__(self):
        self._connectionString = "mongodb+srv://admin:7pbKRmqoSyVmQTpXrEtdmo7xO@cluster0.z5ix9.mongodb.net/discordDB?retryWrites=true&w=majority"
        self.client = MongoClient(self._connectionString, tlsCAFile=certifi.where())
        self.db = self.client["discordDB"]
        self.collection = self.db["questions"]

    def _createPost(self, items: dict):
        if not isinstance(items, dict):
            raise TypeError("items must be a dict")
        self.collection.insert_one(items)

    def _readPost(self, filters: dict):
        self.collection.find_one(filters)

    def _updatePost(self, filter, update):
        self.collection.update_one(filter, update)

    def _deletePost(self, collectionToDelete):
        self.collection.delete_one(collectionToDelete)

    def addOneQuestionToDB(self, question : dict):
        if not isinstance(question, dict):
            raise TypeError("question must be of type dict")
        self._createPost(question)

    def addManyQuestionsToDB(self, questions : list[dict]):
        """ Test types first so we don't add any questions if a type is incorrect, helps with not adding repeat questions"""

        if not all(isinstance(question, dict) for question in questions):
            raise TypeError("all items in questions must be of type dict")
        
        for question in questions:
            self.addOneQuestionToDB(question)



# if __name__ == "__main__":

#     mon = MongoCRUD()
#     dq = DiscordQuestion("What is your fav color?", "PerryBot")
#     mon.addOneQuestionToDB(dq.getAsDict())


#     dq2 = DiscordQuestion("What is your fav animal?", "Serval")
#     dq3 = DiscordQuestion("What is the best place in the world?", "Father CEO")

#     mon.addManyQuestionsToDB([dq2.getAsDict(), dq3.getAsDict()])
    # mon.createPost(
    #     {
    #         "questionText": "What is your fav animal",
    #         "creationDate": datetime.today().replace(microsecond=0),
    #         "user" : "PerryBot",
    #         "used": False
    #     }
    # )
    
