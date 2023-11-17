# # basic way to read
# with open("weather_data.csv", mode="r") as file:
#     l1 = file.read().splitlines()
#
#
# print(l1)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)

    temperature = []

    for row in data:
        print(row)
        if row[1] != "temp":
            temperature.append(int(row[1]))

    print(temperature)
