
from datetime import date, datetime
from typing import Type


class DiscordQuestion:
    """[Class to help form questions to be added to the DB. Simply create a new instance for each question. 
    Fields can be updated after creation]

    """

    def __init__(self, questionText : str, user : str, creationDate : datetime = datetime.now(), used: bool = False):
        """

        Args:
            questionText (str): The question to be asked
            user (str): The user who added the question
            creationDate (datetime, optional): The date and time the question was added. Defaults to datetime.now().
            used (bool, optional): Flag for if the question has already been asked. Defaults to False.
        """
        self.setQuestionText(questionText)
        self.setUser(user)
        self.setCreationDate(creationDate)
        self.setUsed(used)
    
    def setQuestionText(self, questionText : str) -> str:
        if not isinstance(questionText, str):
            raise TypeError("questionText must be a string")
        self._questionText = questionText

    def getQuestionText(self) -> str:
        return self._questionText

    def setUser(self, user) -> None:
        if not isinstance(user, str):
            raise TypeError("user must be a string")
        self._user = user

    def getUser(self) -> str:
        return self._user

    def setCreationDate(self, creationDate: datetime) -> None:
        if not isinstance(creationDate, datetime):
            raise TypeError("creationDate must be a datetime")
        self._creationDate = creationDate

    def getCreationDate(self) -> datetime:
        return self._creationDate

    def setUsed(self, used: bool) -> None:
        if not isinstance(used, bool):
            raise TypeError("used must be a bool")
        self._used = used
    
    def getUsed(self) -> bool:
        return self._used


    def __str__(self):
     return f"Discord Question - questionText:{self.getQuestionText()}, user:{self.getUser()}, creationDate:{self.getCreationDate()}, used: {self.getUsed}"

    def getAsDict(self) -> dict:
        """Returns a dictionary representation of the question

        Returns:
            dict: The dict representation of the question
        """
        dictToReturn : dict = {
            "questionText" : self.getQuestionText(),
            "user" : self.getUser(),
            "creationDate" : self.getCreationDate(),
            "used" : self.getUsed()
        }
        return dictToReturn
