import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim

# Função para geocodificar endereços usando Nominatim
def geocode_address(address):
    geolocator = Nominatim(user_agent="route_optimizer")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Função para calcular rota com OSRM (API pública, sem chave)
def calcular_rota_osrm(origem, destino):
    url = f"http://router.project-osrm.org/route/v1/driving/{origem[1]},{origem[0]};{destino[1]},{destino[0]}?overview=full&geometries=geojson"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        distancia_km = dados['routes'][0]['distance'] / 1000
        duracao_min = dados['routes'][0]['duration'] / 60
        coordenadas = dados['routes'][0]['geometry']['coordinates']
        rota = [(lat, lon) for lon, lat in coordenadas]  # Inverter para (lat, lon)
        return distancia_km, duracao_min, rota
    else:
        return None, None, None

# --- Streamlit App ---
st.set_page_config(page_title="Roteirizador Simples", layout="centered")
st.title("🚚 Roteirizador Inteligente")

with st.form("formulario"):
    origem_end = st.text_input("🏠 Endereço de Origem", "Av. Paulista, 1000, São Paulo")
    destino_end = st.text_input("🌄 Endereço de Destino", "Praça da Sé, São Paulo")
    custo_km = st.number_input("💸 Custo por km (R$)", min_value=0.0, value=2.5, step=0.1)
    submitted = st.form_submit_button("🚀 Calcular Rota Ideal")

if submitted:
    lat1, lon1 = geocode_address(origem_end)
    lat2, lon2 = geocode_address(destino_end)

    if None in (lat1, lon1, lat2, lon2):
        st.error("❌ Não foi possível localizar um dos endereços. Verifique e tente novamente.")
    else:
        with st.spinner("Calculando rota..."):
            distancia, duracao, rota = calcular_rota_osrm((lat1, lon1), (lat2, lon2))

        if rota:
            custo_total = distancia * custo_km

            st.success(f"🗺️ Distância: {distancia:.2f} km | ⏱️ Duração Estimada: {duracao:.1f} min | 💳 Custo Total: R$ {custo_total:.2f}")

            mapa = folium.Map(location=[lat1, lon1], zoom_start=13)
            folium.Marker([lat1, lon1], tooltip="Origem", icon=folium.Icon(color='green')).add_to(mapa)
            folium.Marker([lat2, lon2], tooltip="Destino", icon=folium.Icon(color='red')).add_to(mapa)
            folium.PolyLine(rota, color="blue", weight=5).add_to(mapa)

            st_folium(mapa, width=700, height=500)
        else:
            st.error("❌ Não foi possível calcular a rota.")

