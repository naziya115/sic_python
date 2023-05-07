import folium
import pandas as pd
import json


df = pd.read_csv('csvs/current-covid-patients-hospital.csv')
df = df.groupby('Entity')
marker_map = folium.Map(location=[35.762887375145795, 84.08313219586536], zoom_start=2, tiles='openstreetmap')
geo_path = "csvs/countries-lat-long.json"
json_data = json.load(open(geo_path))
# temp = []
# for country in df.Entity:
#     for key in json_data:
#         value = json_data[key]
#         if country[0] in value:
#             print(country)
#         print(country[0], value[count]['country'])
#         if value[count]['country'] == country[0]:
#             temp.append([value[count]['country'], value[count]['latitude'], value[count]['longitude']])
# print(temp)
#
# temp = []
# count = 0
# for key, group in df:
#     print(key)
#     print(group.tail(1)['Daily hospital occupancy'].values[0])
#     folium.Marker(location=[-27, 133],
#                   popup=f"{key}  {group.tail(1)['Daily hospital occupancy'].values[0]}",
#                   icon=folium.Icon(Icon='cloud'),
#                   ).add_to(marker_map)
#     # count += 1
# marker_map.save("index.html")

