import folium
import requests
from folium import GeoJson

# 1) Welt-GeoJSON ONLINE laden (kein lokaler Download nötig)
url = "https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson"
resp = requests.get(url)
resp.raise_for_status()
geojson_data = resp.json()

# 2) Menge der besuchten Länder – Namen müssen zum GeoJSON passen
#    In dieser Datei heißt das Namensfeld i. d. R. 'name'.
visited = {
    "Germany",
    "France",
    "Switzerland",
    "Italy"
}

# 3) Karte anlegen
m = folium.Map(location=[20, 0], zoom_start=2, tiles="OpenStreetMap")
folium.TileLayer("CartoDB positron", name="Carto Light").add_to(m)

# 4) Styling-Funktionen
def style_fn(feature):
    props = feature.get("properties", {})
    country = props.get("ADMIN") or props.get("name") or ""
    if country in visited:
        return {"fillColor": "#22c55e", "color": "#065f46", "weight": 1, "fillOpacity": 0.6}
    return {"fillColor": "#94a3b8", "color": "#334155", "weight": 0.5, "fillOpacity": 0.15}

def highlight_fn(_):
    return {"fillOpacity": 0.8, "weight": 2, "color": "#0ea5e9"}

# 5) GeoJSON zur Karte hinzufügen
GeoJson(
    data=geojson_data,
    name="World",
    style_function=style_fn,
    highlight_function=highlight_fn,
    tooltip=folium.features.GeoJsonTooltip(
        # Diese Datei nutzt 'name' → falls nötig auf ["ADMIN"] ändern
        fields=["name"],
        aliases=["Land:"],
        sticky=True
    )
).add_to(m)

folium.LayerControl(collapsed=False).add_to(m)

# Karte speichern
m.save("map_4_basiskarte.html")
print("Gespeichert: map_4_basiskarte.html")