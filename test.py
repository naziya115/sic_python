import pandas as pd
import matplotlib.pyplot as plt
import folium
import json

# latest available data about the current number of patients hospitalized
# in different countries due to covid
df = pd.read_csv('csvs/current-covid-patients-hospital.csv')
df = df.groupby('Entity')
marker_map = folium.Map(location=[35.762887375145795, 84.08313219586536], zoom_start=2, tiles='openstreetmap')
# json with latitude and longitude of all countries
geo_path = "csvs/countries-lat-long.json"
json_data = json.load(open(geo_path))
geo_data = pd.DataFrame(columns=['country', 'latitude', 'longitude'])
for country in df.Entity:
    temp = [[tag['country'], tag['latitude'], tag['longitude']] for tag in json_data['ref_country_codes'] if country[0] in tag['country']]
    if len(temp) > 0:
        geo_data.loc[len(geo_data)] = temp[0]
for key, group in df:
    if len(geo_data[geo_data.country == key]) > 0:
        folium.Marker(location=[geo_data[geo_data.country == key].latitude.values[0],
                                geo_data[geo_data.country == key].longitude.values[0]],
                      popup=f"{key}  hospital occupancy: "
                            f"{group.tail(1)['Daily hospital occupancy'].values[0]}",
                      icon=folium.Icon(Icon='cloud'),
                      ).add_to(marker_map)
marker_map.save("index.html")
