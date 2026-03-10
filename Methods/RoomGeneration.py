import json
import os
#import Puzzles

class CreateRoom :
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.description

# checks the validity of the json file that lists all the trinkets for the puzzles
def checkJson(file):
    try:
        data = json.load(file)
    except:
        print("ERROR: PuzzleKeys.json is no longer a valid json")
    return data   

def readJson(file, mainKey):
    try:
        with open(file, 'r') as file:
            data = checkJson(file)
        return data[mainKey] # returns the initial dictionary - every other call will only require data[index]['key'] 
    except Exception as e:
        print("ERROR: file is missing?")
        print(e)
        return None

# figuring out how to scrape data from the json file!
keys = readJson("PuzzleKeys.json", "trinkets")
print(keys[0]['trinket'])
