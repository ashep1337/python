import pandas

# "Primary Fur Color"

data = pandas.read_csv("squirrel_data.csv")

print(data["Primary Fur Color"].value_counts())
