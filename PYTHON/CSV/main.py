# import csv

# with open("weather_data.csv") as weather_data:
#     DATA = csv.reader(weather_data)
#     temperatures = []
#     for row in DATA:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

DATA = pandas.read_csv("weather_data.csv")
TEMP_LIST = DATA["temp"].to_list()

TEMP_AVERAGE = DATA["temp"].mean()
TEMP_HIGHEST = DATA["temp"].max()

print(TEMP_AVERAGE)
print(TEMP_HIGHEST)
print(DATA[DATA.temp == TEMP_HIGHEST])