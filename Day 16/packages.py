# to install packages
#
# go to file
# go to settings
# go to projects
# click on the + symbol on top
# search for your package and press install

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)
