import curses as crs
import sys
from lib.Game import Game
from lib.Player import Player
from typing import List
#from pyfiglet import figlet_format

def main(stdscr) -> None:
    crs.curs_set(0)
    crs.noecho()
    crs.mousemask(1)
    crs.init_pair(1, crs.COLOR_GREEN, crs.COLOR_BLACK)
    players = Player.init_players(stdscr)
    game = Game(stdscr, players)

    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(0, 0, "Players:")
    for i,p in enumerate(players):
        stdscr.addstr(i+1, 0, str(p))
    stdscr.refresh()
    game.run()

if __name__ == "__main__":
    from pytable.table import Table
    quit()
    crs.wrapper(main) 
