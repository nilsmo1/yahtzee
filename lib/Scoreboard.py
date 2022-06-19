from typing import List
from .ScoreboardRep import SCOREBOARD
from .Player import Player

class Scoreboard:
    def __init__(self, players: List[Player]) -> None:
        self.players = players

    def display(self) -> None:
        pass
        
