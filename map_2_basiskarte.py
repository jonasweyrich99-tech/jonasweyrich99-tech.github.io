import folium
from folium import Popup, Icon

# Grundkarte: ohne voreingestellte Tiles, damit wir beide Layers selbst hinzufügen
m = folium.Map(location=[40, 45], zoom_start=3, tiles=None)

# zwei Basiskarten hinzufügen (werden im Layer-Control sichtbar)
folium.TileLayer("CartoDB positron", name="Carto Light").add_to(m)
folium.TileLayer("OpenStreetMap", name="OpenStreetMap").add_to(m)

# später: Marker hinzufügen ...
punkte = [
    {
      "title": "Hochschule Mainz",
      "coords": [49.9892, 8.2383],
      "color": "blue",
      "icon": "university",
      "popup": "<b>Hochschule Mainz</b><br>Lucy-Hillebrand-Str. 2<br>55128 Mainz<br>Tel: 06131 6280"
    },
    {
      "title": "Mainz — Stadtzentrum",
      "coords": [49.9920, 8.2470],
      "color": "green",
      "icon": "info-circle",
      "popup": "<b>Mainz – Stadtzentrum</b><br>Kurze Info zum Ort"
    },
    {
      "title": "Wiesbaden",
      "coords": [50.0782, 8.2398],
      "color": "red",
      "icon": "star",
      "popup": "<b>Wiesbaden</b><br>Kurze Info zum Ort"
    },
    {
      "title": "Zuhause",
      "coords": [49.4757, 7.3504],
      "color": "red",
      "icon": "star",
      "popup": "<b>Zuhause</b><br>Kurze Info zum Ort"
    }
]

bounds = []

# Marker hinzufügen
for p in punkte:
    marker = folium.Marker(
        location=p["coords"],
        popup=Popup(p["popup"], max_width=300),
        icon=Icon(color=p["color"], icon=p["icon"], prefix='fa')  # prefix 'fa' nutzt FontAwesome icons
    )
    marker.add_to(m)
    bounds.append(p["coords"])

# Karte so skalieren, dass alle Marker sichtbar sind
if bounds:
    m.fit_bounds(bounds, padding=(30, 30))

# Layer-Control hinzufügen (ermöglicht Umschalten zwischen Carto Light und OpenStreetMap)
folium.LayerControl().add_to(m)

# Karte speichern
m.save("map_2_basiskarte.html")
print("Gespeichert: map_2_basiskarte.html")
