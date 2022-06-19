from .Rules import Rules

SCOREBOARD = lambda players : """
    {} {} {}
{1}
{2}
{3}
{4}
{5}
{6}
{7}
{8}
{9}
{10}
{11}
{12}
{13}
""".format(*Rules, *list(map(str, players)))
