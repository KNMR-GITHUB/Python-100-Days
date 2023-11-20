import pandas

data = pandas.read_csv("weather_data.csv")

dict_1 = data.to_dict()

list_1 = data["temp"].to_list()

sum1 = 0
for i in list_1:
    sum1 = sum1 + i

print(f"avg: {sum1/len(list_1)}")

# or we can

print(data["temp"].mean())

# get row data

print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

# creating a dataframe from scratch dicts
my_data = {
    "names": ["Hi", "Hello", "Namaste"],
    "greetings": ["Mr. President", "There", "Adharniya Pradhan Mantri"]
}

data2 = pandas.DataFrame(my_data)

print(data2)
