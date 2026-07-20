import pandas

data = pandas.read_csv("Central_Park_Squirrel_Census.csv")
color_list = data["Primary Fur Color"].to_dict


gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]

}

pandas.DataFrame(data_dict).to_csv("squirrel_count.csv") 
