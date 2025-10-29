import folium
from folium import DivIcon

# Nur die Reiseroute darstellen: Karte mit zwei Basiskarten + Polyline + nummerierte Stationen

m = folium.Map(location=[48.5, 8.0], zoom_start=6, tiles=None)
folium.TileLayer("CartoDB positron", name="Carto Light").add_to(m)
folium.TileLayer("OpenStreetMap", name="OpenStreetMap").add_to(m)

# Reiseroute (Name, (lat, lon))
route = [
    ("Herschweiler-Petttersheim", (49.4757, 7.3504)),
    ("Straßburg", (48.584614, 7.7507127)),
    ("Basel", (47.5581077, 7.5878261)),
    ("Luzern", (47.0505452, 8.3054682)),
    ("Mailand", (45.4641943, 9.1896346)),
    ("Via San Sivino 11", (45.52819061279297, 10.547916412353516))
]

# Polyline zeichnen
line_coords = [coords for (_, coords) in route]
folium.PolyLine(locations=line_coords, color="#2b6cb0", weight=4, opacity=0.85).add_to(m)

# nummerierte Stationen als DivIcon-Marker + Tooltip/Popup
bounds = []
for i, (name, (lat, lon)) in enumerate(route, start=1):
    html = f'''
      <div style="
        display:inline-flex;
        align-items:center;
        justify-content:center;
        width:30px;
        height:30px;
        background:#2b6cb0;
        color:#fff;
        border-radius:50%;
        font-weight:700;
        box-shadow:0 1px 3px rgba(0,0,0,0.35);
        font-size:14px;
      ">{i}</div>
    '''
    icon = DivIcon(html=html)
    folium.Marker(
        location=(lat, lon),
        icon=icon,
        tooltip=f"{i}. {name}",
        popup=f"<b>{i}. {name}</b><br>Koordinaten: {lat}, {lon}"
    ).add_to(m)
    bounds.append((lat, lon))

# Ansicht so setzen, dass gesamte Route sichtbar ist
if bounds:
    m.fit_bounds(bounds, padding=(30, 30))

# Layer-Control und speichern
folium.LayerControl().add_to(m)
m.save("map_3_basiskarte.html")
print("Gespeichert: map_3_basiskarte.html")
