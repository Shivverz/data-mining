import urllib.parse
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Encode username and password
username = urllib.parse.quote_plus("jbtescudeiro")
password = urllib.parse.quote_plus("SportingB16b")

# MongoDB Atlas connection URI
uri = f"mongodb+srv://{username}:{password}@datamining.ywf7foj.mongodb.net/?retryWrites=true&w=majority&appName=DataMining"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


db = client.sportmonks
collection = db.standings

# Selecionando todos os documentos na coleção
all_documents = collection.find()

# Iterando sobre os documentos e imprimindo-os




participants_by_season = {}

# Iterando sobre os documentos e organizando por temporada
for document in all_documents:
    season_name = document["season"]["name"]
    participant_name = document["participant"]["name"]
    participant_points = document["points"]
    if season_name not in participants_by_season:
        participants_by_season[season_name] = []
    participants_by_season[season_name].append((participant_name, int(participant_points)))

# Ordenando a lista de participantes pelo segundo elemento da tupla (os pontos)
for season, participants in participants_by_season.items():
    participants_by_season[season] = sorted(participants, key=lambda x: x[1], reverse=True)

sorted_seasons = sorted(participants_by_season.keys())

numbers = [
    "champion",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
    "thirteenth",
    "fourteenth",
    "fifteenth",
    "sixteenth",
    "penultimate",
    "last"
]

with open("Files/standings.txt", "w") as file:

    for season in sorted_seasons:
        participants = participants_by_season[season]
        print(f"Season: {season}")
        print("Participants:")
        pos=0
        for participant in participants:
            print(f"Name: {participant[0]}, Points: {participant[1]}")
            file.write(f"In Season {season} {participant[0]} was {numbers[pos]} with {participant[1]} points.\n")
            pos+=1
        print("\n")




# Fechando a conexão com o MongoDB Atlas
client.close()


