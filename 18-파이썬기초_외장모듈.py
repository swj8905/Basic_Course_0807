import folium

map = folium.Map(location=[37.49786869298923, 127.02763387921568],
           zoom_start=17)

map.save("./map.html")