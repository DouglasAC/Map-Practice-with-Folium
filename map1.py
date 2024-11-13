import folium

map = folium.Map(location=[14.547, -90.527], zoom_start=25, title="Stamen Terrain")


map.save("Map1.html")