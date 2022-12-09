import sys
import pandas as pd
import folium
from folium.plugins import HeatMap

# generates a map with markers for each data point
def marker_map(map, df):
    for i, df in df.iterrows():
        coord = [df['latitude'], df['longitude']]
        folium.Marker(coord).add_to(map)
    map.save('index.html')

# generates a heat map with given data points
def heat_map(map, df):
    heatData = []
    for i, df in df.iterrows():
        heatData.append([df['latitude'], df['longitude']])
    HeatMap(heatData).add_to(map)
    map.save('index.html')
        

def main(mapData):
    df = pd.read_csv(mapData, names=['latitude', 'longitude', 'amenity', 'city'])
    map = folium.Map(location=[49.19, -122.7], tiles="OpenStreetMap", zoom_start=11)
    
    marker_map(map, df)


if __name__ == '__main__':
    mapData = sys.argv[1]
    main(mapData)