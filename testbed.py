import folium
import webbrowser
import os

m = folium.Map([45.35, -121.6972], zoom_start=12)
m.save('map.html')
print("Map saved to map.html")

# Open in default browser
webbrowser.open('file://' + os.path.realpath('map.html'))