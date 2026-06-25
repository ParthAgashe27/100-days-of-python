import prettytable

table = prettytable.PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmender"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "c"

print(table)
