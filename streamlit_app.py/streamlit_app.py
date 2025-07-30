import streamlit as st
import folium
import networkx as nx
from streamlit_folium import st_folium

# ⚙️ Configurações de combustível
CONSUMO_KM_POR_LITRO = 8
PRECO_COMBUSTIVEL = 6.0
CUSTO_POR_KM = PRECO_COMBUSTIVEL / CONSUMO_KM_POR_LITRO

# 🌎 Cidades e coordenadas
coordinates = {
    "São Paulo": (-23.5505, -46.6333),
    "Campinas": (-22.9056, -47.0608),
    "São José dos Campos": (-23.1896, -45.8841),
    "Sorocaba": (-23.5015, -47.4526),
    "Rio de Janeiro": (-22.9068, -43.1729),
    "Belo Horizonte": (-19.9167, -43.9345),
}

# 🧩 Arestas com distâncias e riscos simulados
edges = {
    ("São Paulo", "Campinas"): {"dist": 100, "roubo": 0.2, "acidente": 0.3, "chuva": 0.1, "enchente": 0.1},
    ("São Paulo", "São José dos Campos"): {"dist": 95, "roubo": 0.1, "acidente": 0.2, "chuva": 0.3, "enchente": 0.2},
    ("São Paulo", "Sorocaba"): {"dist": 90, "roubo": 0.3, "acidente": 0.4, "chuva": 0.2, "enchente": 0.1},
    ("Campinas", "Rio de Janeiro"): {"dist": 450, "roubo": 0.2, "acidente": 0.3, "chuva": 0.2, "enchente": 0.3},
    ("Campinas", "Belo Horizonte"): {"dist": 490, "roubo": 0.1, "acidente": 0.2, "chuva": 0.1, "enchente": 0.2},
    ("São José dos Campos", "Rio de Janeiro"): {"dist": 330, "roubo": 0.2, "acidente": 0.3, "chuva": 0.3, "enchente": 0.2},
    ("Sorocaba", "Belo Horizonte"): {"dist": 580, "roubo": 0.4, "acidente": 0.4, "chuva": 0.2, "enchente": 0.3},
    ("Rio de Janeiro", "Belo Horizonte"): {"dist": 440, "roubo": 0.3, "acidente": 0.4, "chuva": 0.3, "enchente": 0.3},
}

# 🚧 Constrói o grafo com pesos de risco e custo
def build_graph():
    G = nx.DiGraph()
    for (u, v), attr in edges.items():
        risco = 0.6 * attr["roubo"] + 0.5 * attr["acidente"] + 0.3 * attr["chuva"] + 0.4 * attr["enchente"]
        peso = attr["dist"] * (1 + risco)
        G.add_edge(u, v, weight=peso, risco_total=risco, distancia=attr["dist"])
    return G

# 🧠 Calcula dados da melhor rota
def calcular_rota(G, origem, destino):
    caminho = nx.shortest_path(G, origem, destino, weight="weight")
    dist_total, risco_total = 0, 0
    for i in range(len(caminho) - 1):
        u, v = caminho[i], caminho[i + 1]
        dist_total += G[u][v]["distancia"]
        risco_total += G[u][v]["risco_total"]
    custo_comb = dist_total * CUSTO_POR_KM
    return caminho, round(dist_total, 2), round(risco_total, 2), round(custo_comb, 2)

# 🎛️ Streamlit Interface
st.set_page_config(page_title="Melhor Rota Otimizada", layout="centered")
st.title("🛣️ Melhor Rota com Risco e Custo")

origem = st.selectbox("Origem", coordinates.keys())
destino = st.selectbox("Destino", coordinates.keys(), index=5)

if origem == destino:
    st.warning("Escolha cidades diferentes.")
    st.stop()

# 🔍 Cálculo da melhor rota
G = build_graph()
caminho, dist, risco, custo = calcular_rota(G, origem, destino)

st.success(f"Rota recomendada: {' ➜ '.join(caminho)}")
st.markdown(f"""
- 📏 **Distância:** {dist} km  
- 💥 **Risco Total:** {risco}  
- ⛽ **Custo Estimado com Combustível:** R$ {custo}
""")

# 🗺️ Mapa com a rota
mapa = folium.Map(location=coordinates[origem], zoom_start=6)
for i in range(len(caminho) - 1):
    folium.Marker(location=coordinates[caminho[i]], popup=caminho[i]).add_to(mapa)
    folium.PolyLine(
        locations=[coordinates[caminho[i]], coordinates[caminho[i + 1]]],
        color="blue", weight=5
    ).add_to(mapa)
folium.Marker(location=coordinates[destino], popup=destino, icon=folium.Icon(color='green')).add_to(mapa)
st_folium(mapa, width=700, height=500)
