import json
import os

#

#  KeyDescriptions.json fields:
# 'trinket', 'trinketDescription', 'puzzleDescription', 'solvedDescription', 'correctTrinket', 'wrongTrinket'

# checks the validity of the json file that lists all the trinkets for the puzzles
def checkJson(file):
    try:
        data = json.load(file)
    except:
        print(f"ERROR: {file} is no longer a valid json")
        return None
    return data   

def readJson(json, mainKey):
    try:
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'gameData/', json)
        with open(filename, 'r') as file:
            data = checkJson(file)[mainKey]
            # I store the data in the json file as an array so this'll make it easier to access data straight away
            # Returns the initial dictionary - every other call will only require data[index]['key']
            return data
        
    except Exception as e:
        print("ERROR: file is missing?")
        print(e)
        return None

#reminder on how to call the different values by the keys and array locations:
#keys = readJson('KeyDescriptions.json', 'trinkets')
#print(keys['trinkets'][0]['trinket']) --> 'Cracked Key'
#print(keys['trinkets'][1]['trinket']) --> 'Crystal Orb'

#simon = readJson('SimonDescriptions.json', 'SimonRoomDescriptions')[0]
#print(simon['puzzleDescription'])