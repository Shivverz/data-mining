import urllib.parse
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Encode username and password
username = urllib.parse.quote_plus("0henrique0")
password = urllib.parse.quote_plus("adminadmin")

# MongoDB Atlas connection URI
uri = f"mongodb+srv://{username}:{password}@datamining.ywf7foj.mongodb.net/?retryWrites=true&w=majority&appName=DataMining"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


db = client.sportmonks
collection = db.fixtures

# Selecionando todos os documentos na coleção
all_documents = collection.find()

# Iterando sobre os documentos e imprimindo-os


for jogo in all_documents:
####intro
#    data_hora_split = jogo['starting_at'].split()
#    dia = data_hora_split[0]
#    horas = data_hora_split[1]
#    if jogo['result_info']:
#        txt = "The game betwen " + jogo['participants'][0]['name'] + " and " + jogo['participants'][1]['name'] + " of the season "+ jogo['season']['name'] +" took place in " + dia + " and started at " + horas +" and the " + jogo['result_info'] +"\n"
#        with open(f"intro.txt", 'a', encoding='utf-8') as arquivo:
#            arquivo.write(txt)

####referees
#    if len(jogo['referees']) > 0:
#        txt = f'The game {jogo["name"]} of the season {jogo["season"]["name"]} was refereed by '
#        for i in range(len(jogo['referees'])-1):
#            txt+= jogo['referees'][i]['referee']['name']+ ", "
#        if len(jogo['referees'])>1:
#            txt = txt[:-2]
#            txt+= " and "
#        txt+= jogo['referees'][0]['referee']['name'] + '.\n'
#        with open(f"referees.txt", 'a', encoding='utf-8') as arquivo:
#            arquivo.write(txt)

###events
    if len(jogo['events']) != 0:
        txt = f'The game {jogo["name"]} of the season {jogo["season"]["name"]} had the following events:\n'
        for i in range(len(jogo['events'])):
            equipa = jogo["events"][i]["participant_id"]
            if equipa != None:
                if len(jogo['participants'])==2:
                    if jogo['participants'][0]['id']==equipa:
                        equipa = jogo['participants'][0]['name']
                    else:
                        equipa = jogo['participants'][1]['name']
       
            if type(equipa) is float or equipa == None:
                equipa = 'unknown'
            if jogo["events"][i]["type"]["name"] == 'Substitution':
                txt+= f'\t{jogo["events"][i]["minute"]} min: There was a substitution for team {equipa}. Player {jogo["events"][i]["related_player_name"]} came in, and player {jogo["events"][i]["player_name"]} went out.\n'
            elif jogo["events"][i]["type"]["name"] == 'Goal':
                if jogo["events"][i]["player_name"] == None:
                    txt+= f'\t{jogo["events"][i]["minute"]} min: {equipa} scored a goal.\n'
                else:
                    txt+= f'\t{jogo["events"][i]["minute"]} min: {jogo["events"][i]["player_name"]} scored a goal for team {equipa}.\n'
            elif jogo["events"][i]["type"]["name"] == 'Own Goal':
                if jogo["events"][i]["player_name"] == None:
                    txt+= f'\t{jogo["events"][i]["minute"]} min: {equipa} scored an own goal.\n'
                else:
                    txt+= f'\t{jogo["events"][i]["minute"]} min: {jogo["events"][i]["player_name"]} scored an own goal for team {equipa}.\n'
            elif jogo["events"][i]["type"]["name"] == 'Corner':
                if jogo["events"][i]["player_name"] == None:
                    txt+= f'\t{jogo["events"][i]["minute"]} min: {equipa} took a corner kick.\n'
                else:
                    txt+= f'\t{jogo["events"][i]["minute"]} min: {jogo["events"][i]["player_name"]} took a corner kick for team {equipa}.\n'
            elif jogo["events"][i]["type"]["name"] == 'Yellowcard' or jogo["events"][i]["type"]["name"] == 'Yellow/Red card' or jogo["events"][i]["type"]["name"] == 'Redcard':
                if jogo["events"][i]["player_name"] == None:
                    txt+= f'\t{jogo["events"][i]["minute"]} min: The {equipa} received {jogo["events"][i]["type"]["name"]}.\n'
                else:
                    txt+= f'\t{jogo["events"][i]["minute"]} min: The player {jogo["events"][i]["player_name"]} from team {equipa} received {jogo["events"][i]["type"]["name"]}.\n'
            elif jogo["events"][i]["type"]["name"] == 'Penalty':
                if jogo["events"][i]["player_name"] == None:
                    txt+= f'\t{jogo["events"][i]["minute"]} min: {equipa} scored a penalty.\n'
                else:
                    txt+= f'\t{jogo["events"][i]["minute"]} min: {jogo["events"][i]["player_name"]} scored a penalty for team {equipa}.\n'
            elif jogo["events"][i]["type"]["name"] == 'Missed Penalty':
                if jogo["events"][i]["player_name"] == None:
                    txt+= f'\t{jogo["events"][i]["minute"]} min: The {equipa} misses a penalty.\n'
                else:
                    txt+= f'\t{jogo["events"][i]["minute"]} min: {jogo["events"][i]["player_name"]} missed a penalty for team {equipa}.\n'
            elif (jogo["events"][i]["type"]["name"] == 'VAR' or jogo["events"][i]["type"]["name"] == 'VAR_CARD'):
                if jogo["events"][i]["addition"] != None:
                    txt+= f'\t{jogo["events"][i]["minute"]} min: Var decision "{jogo["events"][i]["addition"]}"({jogo["events"][i]["player_name"]}).\n'
            else:
                print({jogo["events"][i]["type"]["name"]})
                print(jogo["events"][i])        
        with open(f"events.txt", 'a', encoding='utf-8') as arquivo:
            arquivo.write(txt)

###statistics
############ainda tenho de formatar os statistics 
    if len(jogo['statistics']) != 0:
        txt = f'The game {jogo["name"]} of the season {jogo["season"]["name"]} had the following statistics:\n'
        for i in range(len(jogo['statistics'])):
            equipa = jogo["statistics"][i]["participant_id"]
            if len(jogo['participants'])==2:
                if jogo['participants'][0]['id']==equipa:
                    equipa = jogo['participants'][0]['name']
                else:
                    equipa = jogo['participants'][1]['name']
            txt+= f'\t{equipa} have {jogo["statistics"][i]["data"]["value"]} {jogo["statistics"][i]["type"]["name"]}\n'
        with open(f"statistics.txt", 'a', encoding='utf-8') as arquivo:
            arquivo.write(txt)

####formations  
#    if len(jogo['formations']) == 2:
#        txt= f'In the game {jogo["name"]} of the season {jogo["season"]["name"]} '
#        txt+= f'the {jogo["formations"][0]["location"]} team was {jogo["formations"][0]["participant"]["name"]} and played in a {jogo["formations"][0]["formation"]} formation '
#        txt+= f'and the {jogo["formations"][1]["location"]} team was {jogo["formations"][1]["participant"]["name"]} and played in a {jogo["formations"][1]["formation"]} formation.\n'
#        with open(f"formations.txt", 'a', encoding='utf-8') as arquivo:
#            arquivo.write(txt)
