# Projeto 14: Sistema Inteligente de Rotas

# 🚛 Roteirizador Inteligente para Entregas Seguras e Econômicas

## Descrição do Projeto

Esta aplicação web é um roteirizador inteligente que calcula a **melhor rota de entrega** considerando simultaneamente fatores de risco logístico (roubo de carga, acidentes, chuvas e enchentes) e o custo com combustível. Utilizando um grafo ponderado, o sistema encontra a rota que minimiza o risco total e o custo financeiro, garantindo entregas mais seguras e econômicas.

Construída com Python, Streamlit e NetworkX, a aplicação oferece uma interface simples para seleção de cidades de origem e destino, exibindo o trajeto otimizado em um mapa interativo.

---

## Problema de Negócio

Uma transportadora enfrenta desafios para equilibrar **segurança das cargas** e **custos operacionais**. Rotas mais curtas podem passar por regiões com alto risco de roubos ou desastres naturais, enquanto rotas mais seguras podem ser muito mais longas, elevando custos com combustível e tempo.

Esta aplicação endereça essa dificuldade ao:

- Quantificar e combinar múltiplos riscos em uma única métrica ponderada;
- Incorporar o custo de combustível baseado na distância;
- Gerar rotas que minimizam simultaneamente riscos e custos;
- Facilitar a tomada de decisão para planejamento logístico mais seguro e eficiente.

---

## Impactos Financeiros

Ao considerar riscos e custos de forma integrada, a aplicação possibilita:

- **Redução significativa de perdas financeiras** relacionadas a roubos e acidentes;
- **Otimização do consumo de combustível**, reduzindo despesas operacionais;
- **Aumento da confiabilidade e pontualidade das entregas**, melhorando a satisfação do cliente e reputação da empresa;
- **Tomada de decisão baseada em dados**, mitigando riscos desnecessários e economizando recursos.

---

## Tecnologias Utilizadas

- **Python** para lógica de roteirização e análise de dados;
- **NetworkX** para modelagem do problema como um grafo e cálculo das rotas ótimas;
- **Streamlit** para criação da interface web simples e interativa;
- **Folium** para visualização do mapa das rotas.

---

## Como usar

1. Acesse a a aplicação em https://projeto-14--sistema-inteligente-de-rotas-sosjp3gywohesw24qm6yd.streamlit.app/ e elecione a cidade de origem e destino na interface web;
2. O sistema calcula automaticamente a rota com menor risco ponderado e custo;
3. Veja o caminho recomendado, distância total, risco estimado e custo com combustível;
4. Visualize o trajeto no mapa interativo.
   <img width="839" height="888" alt="image" src="https://github.com/user-attachments/assets/61e52fcc-ef33-4b51-b9eb-884008824b56" />


---

## Próximos passos

- Integração com dados reais de riscos e trânsito;
- Adição de variáveis dinâmicas, como condições climáticas em tempo real;
- Expansão para mais cidades e rotas complexas;
- Inclusão de opções personalizadas para diferentes perfis de risco.

---

