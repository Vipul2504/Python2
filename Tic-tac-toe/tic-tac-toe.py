import random
import math

class player:
    def __init__(self, letter):
        self.letter = letter
        
    def getmoves(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def getmoves(self, letter):
        pass
    
class humanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def getmoves(self, letter):
        pass