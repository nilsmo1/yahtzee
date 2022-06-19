from Rules import Rules
from rich.console import Console
from rich.table import Table
from sys import path

table = Table()
table.add_column("Rules", justify="center")
players = ["hej", "hejdå", "hejhej", "hej"]
for p in players:
    table.add_column(p, justify="center")

for r in Rules.str_reps().values():
    table.add_row(r,"","","","" )
for row in table.rows:
    print(row.__repr__())
console = Console()
console.print(table)
