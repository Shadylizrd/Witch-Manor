import json
import os

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


def test():
    try:
        with open('PuzzleKeys.json', 'r') as file:
            data = checkJson(file)
        print(data)
    except Exception as e:
        print("ERROR: file is missing?")
        print(e)
test()