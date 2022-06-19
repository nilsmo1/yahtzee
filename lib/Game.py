from .Player import Player
from typing import List
from .Dice import Dice
from .Render import Render
from .Rules import Rules
from .Scoreboard import Scoreboard
import curses as crs
from random import randint

class Game:
    def __init__(self, stdscr, players: List[Player]) -> None:
        self.players = players
        self.dice = Dice.init()
        self.scr = stdscr
        self.scr_y, self.scr_x = stdscr.getmaxyx()
        self.render = Render(stdscr)
        self.max_turns = len(Rules)*len(players)
        self.scoreboard = Scoreboard(self.players)

    def render_dice(self) -> None:
        self.scr.refresh()
        for i,die in enumerate(self.dice):
            self.render.draw_dice(die, randint(5, self.scr_y-6), randint(2, self.scr_x-10))

    def run(self) -> None:
        self.scr.addstr(3, 0, "press enter to roll dice")
        self.scr.getch()
        turn = 0
        while turn < self.max_turns:
            player = self.players[turn % len(self.players)]
            self.scr.addstr(4, 0, str(player))
            for _ in range(3):
                rolls = [die.roll() for die in self.dice[len(player.saved):]]
                self.scr.clear()
                self.scr.addstr(0,0, str(turn))
                self.render.draw_scoreboard(self.scoreboard)
                self.render_dice()
                #for d in self.dice:
                #   d.set_highlight(0)
                #TODO: clear displayed
                #TODO: display dice
                #TODO: get mouse to click on dice
                #TODO: highlight chosen dice
                #value = chosen value
                #for d in self.dice:
                #   if d.value = value: d.set_highlight(1)
                #TODO: add chosen dice to saved
                
                key = self.scr.getch()
                if key == crs.KEY_EXIT:
                    #TODO: evaluate dice
                    #TODO: add score to player
                    break
            turn +=1
