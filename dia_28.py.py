import osmnx as ox
import networkx as nx
import folium

# Descargar el grafo de Pereira
G = ox.graph_from_place('Pereira, Colombia', network_type='drive')
# Función para calcular la ruta más corta
def calcular_ruta(G, origen, destino):
    o = ox.distance.nearest_nodes(G, origen[1], origen[0])
    d = ox.distance.nearest_nodes(G, destino[1], destino[0])
    return nx.shortest_path(G, o, d, weight='length')

# Coordenadas de origen y destino
def definir_puntos():
    return (4.8167004,-75.703461), (4.795616,-75.6891498)

origen, destino = definir_puntos()
ruta = calcular_ruta(G, origen, destino)
# Crear el mapa
m = folium.Map(location=origen, zoom_start=14)
ruta_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in ruta]
folium.PolyLine(ruta_coords, color='blue', weight=2.5).add_to(m)
folium.Marker(origen, popup='Origen', icon=folium.Icon(color='green')).add_to(m)
folium.Marker(destino, popup='Destino', icon=folium.Icon(color='red')).add_to(m)

# Guardar y mostrar mensaje
m.save('mapa_pereira.html')
print("Mapa generado y guardado como 'mapa_pereira.html'.")