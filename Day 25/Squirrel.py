import pandas as pd

data_01 = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231120.csv")

fur = data_01["Primary Fur Color"].to_list()

b_count = 0
c_count = 0
g_count = 0

for i in fur:
    if i == "Black":
        b_count += 1
    elif i == "Cinnamon":
        c_count += 1
    else:
        g_count += 1

new_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [g_count, c_count, b_count]
}

new_df = pd.DataFrame(new_dict)

print(new_df)

