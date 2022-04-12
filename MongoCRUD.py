from DiscordQuestion import DiscordQuestion
from datetime import datetime
import certifi
from pymongo import MongoClient


class NoNewPriorityQuestionAvailableException(Exception):
    pass

class NoNewNonPriorityQuestionAvailableException(Exception):
    pass

class NoNewQuestionAvailableException(Exception):
    pass

class MongoCRUD:
    def __init__(self):
        self._connectionString = ""
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

    def addManyQuestionsToDB(self, questions : list):
        """ Test types first so we don't add any questions if a type is incorrect, helps with not adding repeat questions"""

        if not all(isinstance(question, dict) for question in questions):
            raise TypeError("all items in questions must be of type dict")
        
        for question in questions:
            self.addOneQuestionToDB(question)
            

    def getNextPriorityOneQuestion(self) -> dict:
        """[summary]

        Raises:
            NoNewPriorityQuestionAvailableException: No new priority questions are available in the DB

        Returns:
            dict: The earlist new priority question
        """
        
        priorityFindQuery = {'priority' : {'$eq' : 1}, 'used' : {'$eq' : False}}
        
        docCount = self.collection.count_documents(priorityFindQuery)
        if docCount == 0:
            raise NoNewPriorityQuestionAvailableException("No new priority questions are available!")
            
        cursor = self.collection.find(priorityFindQuery).sort('creationDate' , -1).limit(1)
        
        for doc in cursor:
            return doc
        
    def getNextNonPriorityQuestion(self):
        findQuery = {'priority' : {'$eq' : 0}, 'used' : {'$eq' : False}}
        docCount = self.collection.count_documents(findQuery)
        
        if docCount == 0:
            raise NoNewNonPriorityQuestionAvailableException("No new non-priority questions are available!")
        
        cursor = self.collection.find(findQuery).sort('creationDate' , 1).limit(1)
        
        for doc in cursor:
            return doc
        
        
            
            
    def getNextQuestion(self) -> dict:
        """Return the next question to be asked. If a priority 1 question(s) exists then the earlist priority 1 question will be returned.
        Else the latest non-priority 1 question will be returned.

        Returns:
            dict: The entry of the DB that matches the criteria of the description above
        """
        
        try:
            newPriorityQuestion = self.getNextPriorityOneQuestion()
            return newPriorityQuestion
        except NoNewPriorityQuestionAvailableException:
            try:
                newNonPriorityQuestion = self.getNextNonPriorityQuestion()
                return newNonPriorityQuestion
            except NoNewNonPriorityQuestionAvailableException:
                raise NoNewQuestionAvailableException("There are no new questions available!")         
            
        
        



# if __name__ == "__main__":
#     mon = MongoCRUD()
#     # dq = DiscordQuestion("What is your frog?", "Frogge", priority=0)
#     # mon.addOneQuestionToDB(dq.getAsDict())
#     # a = mon.getNextPriorityOneQuestion()
#     # a = mon.getNextNonPriorityQuestion()
#     # a = mon.getNextQuestion()
#     # print(a)

#     dq2 = DiscordQuestion("What is your fav animal?", "Serval")
#     dq3 = DiscordQuestion("What is the best place in the world?", "Father CEO")

#     mon.addManyQuestionsToDB([dq2.getAsDict(), dq3.getAsDict()])
#     mon._createPost(
#         {
#             "questionText": "What is your fav animal",
#             "creationDate": datetime.today().replace(microsecond=0),
#             "user" : "PerryBot",
#             "used": False
#         }
#     )
    
