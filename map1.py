import folium
import pandas as pd

tipo_color = {
        "PR": "green",
        "CC": "blue",
        "MU": "purple",
        "UN": "orange",
        "HO": "red",
        "AE": "gray",
        "AV": "cadetblue"
    }
    

def getChild(tipo, latitud, longitud, lugar):
    if tipo == "PR":
        return folium.CircleMarker(location=[latitud, longitud], radius=8, popup=lugar, fill_color="lightgreen", color=tipo_color[tipo], fill_opacity=0.6, fill=True)
    elif tipo == "CC":
        return folium.Marker(location=[latitud, longitud], popup=lugar, icon=folium.Icon(color=tipo_color[tipo], icon="shopping-bag", prefix="fa"))
    elif tipo == "MU":
        return folium.Marker(location=[latitud, longitud], popup=lugar, icon=folium.Icon(color=tipo_color[tipo], icon="university", prefix="fa"))
    elif tipo == "UN":
        return folium.Marker(location=[latitud, longitud], popup=lugar, icon=folium.Icon(color=tipo_color[tipo], icon="graduation-cap", prefix="fa"))
    elif tipo == "HO":
        return folium.Marker(location=[latitud, longitud], popup=lugar, icon=folium.Icon(color=tipo_color[tipo], icon="plus-square", prefix="fa"))
    elif tipo == "AE":
        return folium.Marker(location=[latitud, longitud], popup=lugar, icon=folium.Icon(color=tipo_color[tipo], icon="plane", prefix="fa"))
    elif tipo == "AV":
        return folium.CircleMarker(location=[latitud, longitud], radius=6, popup=lugar, fill_color="lightblue", color=tipo_color[tipo], fill_opacity=0.6, fill=True)
    else:
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