import curses as crs
from .Scoreboard import Scoreboard
from .Dice import Dice
import curses as crs
import locale
locale.setlocale(locale.LC_ALL, 'sv_SE.utf8')

class Render:
    def __init__(self, stdscr) -> None:
        self.scr = stdscr
        self.rows, self.cols = self.scr.getmaxyx()

    def draw_dice(self, dice: Dice, row: int, col: int) -> None:
        if not(0 <= row <= self.rows and 0 <= col <= self.cols):
            return
        if dice.highlight:
            for i, p in enumerate(str(dice).split("\n")):
                self.scr.addstr(row+i, col, ''.join(p), crs.color_pair(1))
        else:
            for i, p in enumerate(str(dice).split("\n")):
                self.scr.addstr(row+i, col, ''.join(p))
        self.scr.refresh()
    
    def draw_scoreboard(self, scoreboard: Scoreboard):
        pass
