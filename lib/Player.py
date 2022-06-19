from __future__ import annotations
from typing import Dict, List
from .Rules import Rules
from .Dice import Dice
import curses as crs

class Player:
    def __init__(self, name: str="p1") -> None:
        self.name = name
        self.fields = {rule.name : 0 for rule in Rules}
        self.saved = []
    
    def set_field(self, rule: int, value): 
        if rule in self.fields: self.fields[rule] = value

    @property
    def score(self) -> int:
        return sum(v for v in self.fields.values())
    
    def __str__(self):
        return f"{self.name}\t Score: {self.score}"

    def set_saved(self, *dice: Dice) -> None:
        dice = list(dice)
        for die in dice: self.saved.append(die)

    @staticmethod
    def init_players(stdscr) -> List[Player]:
        crs.echo()
        stdscr.addstr(0,0,"How many players?")
        n = int(stdscr.getstr(1,0))
        players = []
        for t in range(n):
            stdscr.clear()
            stdscr.addstr(0,0, f"Name of player {t+1}:")
            name = stdscr.getstr(1,0).decode("utf-8")
            players.append(Player(name))
            stdscr.refresh()
        return players
            
