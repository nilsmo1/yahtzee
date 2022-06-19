from typing import List
from .Dice import Dice
from .Rules import Rules
from collections import Counter

class CalcRules:
    @staticmethod
    def upper_section(dice: List[Dice], choice: int) -> int:
        return sum(d.value for d in dice if d.value == choice)
    
    @staticmethod
    def lower_section(self, dice: List[Dice], choice: int, value: int) -> int:
        counter = Counter(d.value for d in dice)
        if choice < Rules.THREEOFAKIND: return -1
        
        if choice == Rules.THREEOFAKIND: 
            if counter[value] >= 3: return 3*value

        elif choice == Rules.FOUROFAKIND:
            if counter[value] >= 4: return 4*value

        elif choice == Rules.FULLHOUSE:
            if len(counter) == 2:
                return 25

        elif choice == Rules.SMALLSTRAIGHT:
            for c in (1, 2, 3):
                if all(k in counter for 
                       k in (c, c+1, c+2, c+3)):
                    return 30

        elif choice == Rules.LARGESTRAIGHT:
            for c in (1, 2):
                if all(k in counter for 
                       k in (c, c+1, c+2, c+3)):
                    return 40

        elif choice == Rules.YAHTZEE:
            if len(counter) == 1:
                return 50

        elif choice == Rules.CHANCE:
            return sum(k*i for k,i in counter.items())

        if choice in Rules: return 0
        raise ValueError(f"{choice} is not a valid choice!")
        
