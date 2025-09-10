# Project 14: Smart Routing System

🚛 **Intelligent Route Planner for Safe and Cost-Effective Deliveries**

---

## Project Overview

This web application is an intelligent route planner that calculates the **optimal delivery route** by simultaneously considering logistics risks (cargo theft, accidents, rain, and floods) and fuel costs. Using a weighted graph, the system identifies the route that minimizes both total risk and financial expense, ensuring safer and more cost-efficient deliveries.

Built with **Python**, **Streamlit**, and **NetworkX**, the app provides a user-friendly interface for selecting origin and destination cities, displaying the optimized route on an interactive map.

---

## Business Challenge

Logistics companies often struggle to balance **cargo safety** and **operational costs**. Shorter routes may pass through high-risk areas for theft or natural disasters, while safer routes can be much longer, increasing fuel and time expenses.

This application addresses these challenges by:

- Quantifying and combining multiple risk factors into a single weighted metric  
- Incorporating fuel costs based on distance  
- Generating routes that minimize both risk and expense  
- Supporting smarter decision-making for safer, more efficient logistics planning  

---

## Financial Benefits

By integrating risk and cost considerations, the system helps:

- **Significantly reduce financial losses** due to theft or accidents  
- **Optimize fuel consumption**, lowering operational costs  
- **Increase delivery reliability and punctuality**, enhancing customer satisfaction and company reputation  
- **Enable data-driven decisions**, mitigating unnecessary risks and saving resources  

---

## Technologies Used

- **Python** for routing logic and data analysis  
- **NetworkX** to model the problem as a graph and compute optimal routes  
- **Streamlit** for a simple, interactive web interface  
- **Folium** for route map visualization  

---

## How to Use

1. Access the app at: [Smart Routing System](https://projeto-14--sistema-inteligente-de-rotas-sosjp3gywohesw24qm6yd.streamlit.app/)  
2. Select your origin and destination cities  
3. The system automatically calculates the route with the lowest weighted risk and cost  
4. View the recommended path, total distance, estimated risk, and fuel cost  
5. Explore the route on the interactive map  

<img width="839" height="888" alt="Smart Routing Map" src="https://github.com/user-attachments/assets/61e52fcc-ef33-4b51-b9eb-884008824b56" />

---

## Next Steps

- Integrate real-time risk and traffic data  
- Add dynamic variables, such as live weather conditions  
- Expand coverage to more cities and complex routes  
- Include customizable options for different risk profiles  

---
