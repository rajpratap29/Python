# with open("Day 25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("Day 25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temprature = []
#     for row in data:
#         if row[1] != "temp":
#             temprature.append(int(row[1]))
#     print(temprature)

import pandas

# data = pandas.read_csv("Day 25/weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average = sum(temp_list) / len(temp_list)
# print(average)
# print(data["temp"].mean())
# print(data["temp"].max())


# Get data in Columns
# print(data["condition"])
# print(data.condition)

# Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# Creating dataframe from scratch
# data_dict = {
#     "students": ["Pundir", "Kush", "Raj"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("Day 25/new_data.csv")


data = pandas.read_csv("Day 25/2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("Day 25/squirrel_count.csv")