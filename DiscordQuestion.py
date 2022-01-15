
from datetime import date, datetime
from typing import Type


class DiscordQuestion:

    def __init__(self, questionText : str, user : str, creationDate : datetime = datetime.now(), used: bool = False):
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
        dictToReturn : dict = {
            "questionText" : self.getQuestionText(),
            "user" : self.getUser(),
            "creationDate" : self.getCreationDate(),
            "used" : self.getUsed()
        }
        return dictToReturn
