import certifi
from pymongo import MongoClient

# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(
    "mongodb+srv://admin:7pbKRmqoSyVmQTpXrEtdmo7xO@cluster0.z5ix9.mongodb.net/discordDB?retryWrites=true&w=majority",
    tlsCAFile=certifi.where()
)
dbAdmin = client.admin
print("################")
db = client["discordDB"]
collection = db["questions"]


# newPost = {"question": "What is your fav colour?"}

# collection.insert_one(newPost)

# Issue the serverStatus command and print the results
# serverStatusResult = db.command("serverStatus")

# pprint(serverStatusResult)


results = collection.find({"question": "What is your fav colour?"})

for result in results:
    print(result)
