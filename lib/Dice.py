from __future__ import annotations 
from random import randint
from typing import Optional, List
import curses as crs
from .DiceReps import ONE, TWO, THREE, FOUR, FIVE, SIX
from random import randint

class Dice:
    def __init__(self, sides: int=6, *, value: Optional[int]=None, highlight: int=0) -> None:
        self.sides = sides
        self.value = value
        self.highlight = highlight
        self.strs = [ONE, TWO, THREE, FOUR, FIVE, SIX]

    def roll(self) -> None:
        self.value = randint(1, self.sides)
        return self.value

    def __eq__(self, other: Dice): 
        if isinstance(other, int):
            return self.value == other
        elif isinstance(other, Dice):
            return self.value == other.value

    def reset(self) -> None: self.value = None 
    def __str__(self) -> str: return self.strs[self.value-1]
    #def __str__(self) -> str: return self.strs

    @staticmethod
    def init(n: int=5, *, sides: int=6, values: Optional[List[int]]=None) -> List[Dice]:
        if values is None: return [Dice(sides, highlight=randint(0,1)) for i in range(n)]
        return [Dice(sides, v) for v in values]

    def set_highlight(self, highlight: int) -> None:
        self.highlight = highlight
