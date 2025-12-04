import streamlit as st
st.title("Problema Terreno")
#Entrada de dados
st.write("Digite a largura do terreno em metros:")
largura = st.number_input("Largura (m):")
st.write("Digite o comprimento do terreno em metros:")
comprimento = st.number_input("Comprimento (m):")
st.write("Digite o valor do metro quadrado em R$:")
valor_m2 = st.number_input("Valor do m²IR (R$):")
#Processamento de dados
area = largura * comprimento
preco = area * valor_m2
#Saída de dados
st.write(f"A área do terreno é {area} metros quadrados.")


