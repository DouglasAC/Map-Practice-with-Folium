import folium

map = folium.Map(location=[14.586521217402636, -90.52169884971288], zoom_start=25, title="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[14.586521217402636, -90.52169884971288], popup="Paiz, Américas", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")