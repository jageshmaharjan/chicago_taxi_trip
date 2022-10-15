import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.animation as animation


df = pd.read_csv('/Users/jagesh.maharjan/Downloads/jupyter_notebook/DA/Taxi_Trips_-_2021.csv')

df.dropna(subset=["Pickup Centroid Location",
                  "Dropoff Centroid  Location",
                  "Trip Start Timestamp",
                  "Trip End Timestamp"],
          how="any",
          inplace=True)

min_long = min(df["Pickup Centroid Longitude"].min(), df["Dropoff Centroid Longitude"].min())
max_long = max(df["Pickup Centroid Longitude"].max(), df["Dropoff Centroid Longitude"].max())
min_lat = min(df["Pickup Centroid Latitude"].min(), df["Dropoff Centroid Latitude"].min())
max_lat = max(df["Pickup Centroid Latitude"].max(), df["Dropoff Centroid Latitude"].max())

Map_Dim = ((min_long, max_long, min_lat, max_lat))

city_map = plt.imread('/Users/jagesh.maharjan/Downloads/jupyter_notebook/DA/map.png')

fig, ax = plt.subplots(figsize = (15,20))

# source_point = [-87.85, 41.50]
# destination_point = [-87.75, 41.95]  #[df["Pickup Centroid Longitude"], df["Dropoff Centroid Latitude"]]
ax.scatter(df["Pickup Centroid Longitude"], df["Pickup Centroid Latitude"],
           zorder=1, alpha= 0.2, c='b', s=10)

# ax.plot(source_point,destination_point, 'k-')

ax.set_title('Chicago City Map')
ax.set_xlim(Map_Dim[0],Map_Dim[1])
ax.set_ylim(Map_Dim[2],Map_Dim[3])
ax.imshow(city_map, zorder=0, extent = Map_Dim, aspect= 'equal')


# def ride_simulate(df):
#     # x = long
#     # y = lat
#     ax.clear()
#     # ax.plot(x, y)
#     ax.set_title('Chicago City Map')
#     ax.set_xlim(Map_Dim[0], Map_Dim[1])
#     ax.set_ylim(Map_Dim[2], Map_Dim[3])
#     ax.imshow(city_map, zorder=0, extent=Map_Dim, aspect='equal')
#     ax.scatter(df["Pickup Centroid Longitude"], df["Pickup Centroid Latitude"],
#                zorder=1, alpha=0.2, c='b', s=10)


# ani = animation.FuncAnimation(
#         fig, ride_simulate,
#         interval=500, repeat=False #blit=True, save_count=50
#         )

# plt.show()