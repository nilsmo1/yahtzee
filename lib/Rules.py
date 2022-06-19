from enum import Enum, auto
from typing import Dict

class Rules(Enum):
    ACES = auto() 
    TWOS = auto()
    THREES = auto()
    FOURS = auto()
    FIVES = auto()
    SIXES = auto()
    THREEOFAKIND = auto()
    FOUROFAKIND = auto()
    FULLHOUSE = auto()
    SMALLSTRAIGHT = auto()
    LARGESTRAIGHT = auto()
    YAHTZEE = auto()
    CHANCE = auto()
    
    @staticmethod
    def str_reps() -> Dict[str, int]:
        reps = {rule.name : str(rule.name).capitalize() for rule in list(Rules)[:6]}
        reps[Rules.THREEOFAKIND] = "Three of a kind"
        reps[Rules.FOUROFAKIND] = "Four of a kind"
        reps[Rules.FULLHOUSE] = "Full house"
        reps[Rules.SMALLSTRAIGHT] = "Small straight"
        reps[Rules.LARGESTRAIGHT] = "Large straight"
        reps[Rules.YAHTZEE] = "Yahtzee"
        reps[Rules.CHANCE] = "Chance"
        return reps
