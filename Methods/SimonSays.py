COLOURS=["RED", "BLUE", "GREEN", "YELLOW"]
class SimonSays(Puzzles):
    
    def __init__(self,difficulty):
        
        self.__answer=[]
        self._difficulty=difficulty
        
        for i in range(difficulty):
            #makes a list of random colours the length of the difficulty
            self.__answer.append(COLOURS[i])
            
            
    def sequence(self, difficulty,currentDifficulty):
        currentDifficulty+=1
        
        if difficulty==currentDifficulty:
            #returns true if the game has been won
            return True
        else:
            pattern(difficulty, currentDifficulty)
    
    

        
        