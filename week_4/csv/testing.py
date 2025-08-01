# with open("weather_data.csv") as data:
#    weather_data = data.readlines()
#    print(weather_data)


# with open("weather_data.csv") as data:
#    weather_data = csv.reader(data)
#    temps = []
#    for row in weather_data:
#        if row[1] != "temp":
#            temps.append(int(row[1]))
#    print(temps)

# import pandas

# data = pandas.read_csv("weather_data.csv")

# print(data.temp.max())
# max = data.temp.max()
# print(max)
# print(data[data.temp == max])

# monday = data[data.day == "Monday"]
# print(monday.temp * (9 / 5) + 32)
