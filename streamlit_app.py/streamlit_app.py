import streamlit as st
import folium
import networkx as nx
from streamlit_folium import st_folium

# ⚙️ Fuel settings
KM_PER_LITER = 8
FUEL_PRICE = 6.0
COST_PER_KM = FUEL_PRICE / KM_PER_LITER

# 🌎 Cities and coordinates
coordinates = {
    "São Paulo": (-23.5505, -46.6333),
    "Campinas": (-22.9056, -47.0608),
    "São José dos Campos": (-23.1896, -45.8841),
    "Sorocaba": (-23.5015, -47.4526),
    "Rio de Janeiro": (-22.9068, -43.1729),
    "Belo Horizonte": (-19.9167, -43.9345),
}

# 🧩 Edges with simulated distances and risks
edges = {
    ("São Paulo", "Campinas"): {"dist": 100, "theft": 0.2, "accident": 0.3, "rain": 0.1, "flood": 0.1},
    ("São Paulo", "São José dos Campos"): {"dist": 95, "theft": 0.1, "accident": 0.2, "rain": 0.3, "flood": 0.2},
    ("São Paulo", "Sorocaba"): {"dist": 90, "theft": 0.3, "accident": 0.4, "rain": 0.2, "flood": 0.1},
    ("Campinas", "Rio de Janeiro"): {"dist": 450, "theft": 0.2, "accident": 0.3, "rain": 0.2, "flood": 0.3},
    ("Campinas", "Belo Horizonte"): {"dist": 490, "theft": 0.1, "accident": 0.2, "rain": 0.1, "flood": 0.2},
    ("São José dos Campos", "Rio de Janeiro"): {"dist": 330, "theft": 0.2, "accident": 0.3, "rain": 0.3, "flood": 0.2},
    ("Sorocaba", "Belo Horizonte"): {"dist": 580, "theft": 0.4, "accident": 0.4, "rain": 0.2, "flood": 0.3},
    ("Rio de Janeiro", "Belo Horizonte"): {"dist": 440, "theft": 0.3, "accident": 0.4, "rain": 0.3, "flood": 0.3},
}

# 🚧 Build graph with risk and cost weights
def build_graph():
    G = nx.DiGraph()
    for (u, v), attr in edges.items():
        total_risk = 0.6 * attr["theft"] + 0.5 * attr["accident"] + 0.3 * attr["rain"] + 0.4 * attr["flood"]
        weight = attr["dist"] * (1 + total_risk)
        G.add_edge(u, v, weight=weight, total_risk=total_risk, distance=attr["dist"])
    return G

# 🧠 Calculate best route data
def calculate_route(G, origin, destination):
    path = nx.shortest_path(G, origin, destination, weight="weight")
    total_distance, total_risk = 0, 0
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        total_distance += G[u][v]["distance"]
        total_risk += G[u][v]["total_risk"]
    fuel_cost = total_distance * COST_PER_KM
    return path, round(total_distance, 2), round(total_risk, 2), round(fuel_cost, 2)

# 🎛️ Streamlit Interface
st.set_page_config(page_title="Optimized Best Route", layout="centered")
st.title("🛣️ Best Route with Risk and Cost")

origin = st.selectbox("Origin", coordinates.keys())
destination = st.selectbox("Destination", coordinates.keys(), index=5)

if origin == destination:
    st.warning("Please choose different cities.")
    st.stop()

# 🔍 Calculate best route
G = build_graph()
path, distance, risk, cost = calculate_route(G, origin, destination)

st.success(f"Recommended route: {' ➜ '.join(path)}")
st.markdown(f"""
- 📏 **Distance:** {distance} km  
- 💥 **Total Risk:** {risk}  
- ⛽ **Estimated Fuel Cost:** R$ {cost}
""")

# 🗺️ Map with the route
map_obj = folium.Map(location=coordinates[origin], zoom_start=6)
for i in range(len(path) - 1):
    folium.Marker(location=coordinates[path[i]], popup=path[i]).add_to(map_obj)
    folium.PolyLine(
        locations=[coordinates[path[i]], coordinates[path[i + 1]]],
        color="blue", weight=5
    ).add_to(map_obj)
folium.Marker(location=coordinates[destination], popup=destination, icon=folium.Icon(color='green')).add_to(map_obj)
st_folium(map_obj, width=700, height=500)

