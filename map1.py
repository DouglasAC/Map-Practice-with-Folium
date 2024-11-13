import folium
import pandas as pd

data = pd.read_csv("Lugares.txt")

map = folium.Map(location=[14.586521217402636, -90.52169884971288], zoom_start=15, title="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for row in data.itertuples(index=False):
    lugar, latitud, longitud = row.NOMBRE, row.LAT, row.LOG
    fg.add_child(folium.Marker(location=[latitud, longitud], popup=lugar, icon=folium.Icon(color="blue")))

fg.add_child(folium.Marker(location=[14.586521217402636, -90.52169884971288], popup="Paiz, Américas", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")