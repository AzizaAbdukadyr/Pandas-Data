

# with open("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# sum_temp = sum(temp_list)
# print(sum_temp)
# avg_temp = sum_temp/len(temp_list)
# print(avg_temp)

print(data["temp"].mean())
print(data["temp"].max())

print("---"*10)
# Get Data in Columns
print(data["condition"])
print(data.condition)


print("---"*10)
# Get data in Row
print(data[data.day == "Monday"])


print("---"*10)
# Get max temp in row
print(data[data.temp == data.temp.max()])

print("---"*10)
# Get Monday temp
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp*1.8 + 32
print(monday_temp_F)

print("---"*10)
# Create a dataframe from scratch
data_dict_2 = {
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}
data_2 = pandas.DataFrame(data_dict_2)
print(data_2)
data_2.to_csv("new_data2.csv")