import folium

# Grundkarte erstellen (Zentrum Europa, Zoomstufe 4)
m = folium.Map(location=[50, 10], zoom_start=4, tiles="OpenStreetMap")

# Optional: weitere Basiskarten hinzufügen
folium.TileLayer("CartoDB positron", name="Carto Light").add_to(m)

# Karte speichern
m.save("map_1_basiskarte.html")
print("Gespeichert: map_1_basiskarte.html")