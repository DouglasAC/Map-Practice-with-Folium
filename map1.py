import folium
import pandas as pd

tipo_config = {
    "PR": {"type": "CircleMarker", "radius": 8, "fill_color": "lightgreen", "color": "green", "fill_opacity": 0.6, "fill": True},
    "CC": {"type": "Marker", "icon": "shopping-bag", "color": "blue"},
    "MU": {"type": "Marker", "icon": "university", "color": "purple"},
    "UN": {"type": "Marker", "icon": "graduation-cap", "color": "orange"},
    "HO": {"type": "Marker", "icon": "plus-square", "color": "red"},
    "AE": {"type": "Marker", "icon": "plane", "color": "gray"},
    "AV": {"type": "CircleMarker", "radius": 6, "fill_color": "lightblue", "color": "cadetblue", "fill_opacity": 0.6, "fill": True}
}

def getChild(tipo, latitud, longitud, lugar):
    config = tipo_config.get(tipo)
    if config:
        if config["type"] == "CircleMarker":
            return folium.CircleMarker(
                location=[latitud, longitud],
                radius=config["radius"],
                popup=lugar,
                fill_color=config["fill_color"],
                color=config["color"],
                fill_opacity=config["fill_opacity"],
                fill=config["fill"]
            )
        elif config["type"] == "Marker":
            return folium.Marker(
                location=[latitud, longitud],
                popup=lugar,
                icon=folium.Icon(color=config["color"], icon=config["icon"], prefix="fa")
            )
    return folium.Marker(location=[latitud, longitud], popup=lugar, icon=folium.Icon(color="black", icon="question", prefix="fa"))

data = pd.read_csv("Lugares.txt")

map = folium.Map(location=[14.586521217402636, -90.52169884971288], zoom_start=15, title="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for row in data.itertuples(index=False):
    lugar, latitud, longitud, tipo = row.NOMBRE, row.LAT, row.LOG, str(row.TIPO).strip()
    child = getChild(tipo, latitud, longitud, lugar)
    fg.add_child(child)

map.add_child(fg)
map.save("Map1.html")