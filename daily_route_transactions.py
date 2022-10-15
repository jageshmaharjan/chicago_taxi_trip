from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def day_parser(day):
    return day.split(" ")[0]

df = pd.read_csv('/Users/jagesh.maharjan//Downloads/jupyter_notebook/DA/Taxi_Trips_-_2021.csv')
df.dropna(subset=["Pickup Centroid Location",
                  "Dropoff Centroid  Location",
                  "Trip Start Timestamp",
                  "Trip End Timestamp"],
          how="any",
          inplace=True)

# df = df[:50000]
print(df.head())

min_long = min(df["Pickup Centroid Longitude"].min(), df["Dropoff Centroid Longitude"].min())
max_long = max(df["Pickup Centroid Longitude"].max(), df["Dropoff Centroid Longitude"].max())
min_lat = min(df["Pickup Centroid Latitude"].min(), df["Dropoff Centroid Latitude"].min())
max_lat = max(df["Pickup Centroid Latitude"].max(), df["Dropoff Centroid Latitude"].max())

Map_Dim = (min_long, max_long, min_lat, max_lat)

x1_all = list(df["Pickup Centroid Longitude"])
y1_all = list(df["Pickup Centroid Latitude"])
x2_all = list(df["Dropoff Centroid Longitude"])
y2_all = list(df["Dropoff Centroid Latitude"])
x1, x2, y1, y2 = [], [], [], []
m = 0
city_map = plt.imread('/Users/jagesh.maharjan/Downloads/jupyter_notebook/DA/map.png')
df_date_ = list(map(lambda x: day_parser(x), df["Trip Start Timestamp"]))
df_day_count_ = dict(Counter(df_date_))
df_day_count_ ={k: v for k, v in sorted(df_day_count_.items(), key=lambda x: x[0])}

for k, v in df_day_count_.items():
    for i in range(m, m+v):
        plt.clf()
        x1.append(x1_all[i])
        x2.append(x2_all[i])
        y1.append(y1_all[i])
        y2.append(y2_all[i])
        m += 1

        if len(x1) == v: # % 5 == 0:
            plt.figure(figsize=(12, 8))
            plt.xlim(Map_Dim[0], Map_Dim[1])
            plt.ylim(Map_Dim[2], Map_Dim[3])
            plt.imshow(city_map, zorder=0, extent=Map_Dim, aspect='equal')
            plt.plot([x1, x2], [y1, y2], 'ro--', linewidth=1.5)
            plt.legend(k)
            plt.title("Daily Route Transaction in Chicago")
            plt.pause(0.00001)
            x1, x2, y1, y2 = [], [], [], []


plt.show()


# check for the most bussiest long-lat
# avg. ride hourly
# price hourly

