# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         temp = row[1]
#         if temp != "temp":
#             temperatures.append(int(temp))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # avg = sum(temp_list) / len(temp_list)
# avg = data["temp"].mean()
# print(avg)
#
# maxi = data.temp.max()
# print(maxi)
#
# print(data[data.day == "Monday"])
# print(data[data.temp == maxi])
# monday = data[data.day == "Monday"]
# print((monday.temp * 1.8) + 32)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_fur_color = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_fur_color = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_fur_color = len(data[data["Primary Fur Color"] == "Black"])
print(grey_fur_color)
print(cinnamon_fur_color)
print(black_fur_color)

data_dict = {
   "FurColor": ["grey", "black", "red"],
   "Count": [grey_fur_color, black_fur_color, cinnamon_fur_color]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count")
