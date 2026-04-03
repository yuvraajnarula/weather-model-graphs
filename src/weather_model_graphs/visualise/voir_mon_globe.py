import networkx as nx
import numpy as np
import weather_model_graphs as wmg
from weather_model_graphs.visualise.plot_3d import render_with_plotly

# 1. Coordonnées de test (en degrés)
coords = np.array([
    [6.12, 1.22],   # Lomé
    [48.85, 2.35],  # Paris
    [40.71, -74.00] # New York
])

# 2. Création du graphe
# On réduit mesh_node_distance à 10 pour que ça tienne dans les coordonnées
graph = wmg.create.create_all_graph_components(
    coords=coords,
    m2m_connectivity="flat",
    g2m_connectivity="nearest_neighbour",
    m2g_connectivity="nearest_neighbour",
    m2m_connectivity_kwargs=dict(mesh_node_distance=10) # <--- VALEUR RÉDUITE ICI
)

# 3. On lance la visualisation
print("Génération du globe 3D...")
render_with_plotly(
    graph, 
    layout="concentric", 
    add_coastlines=True, 
    show=True
)