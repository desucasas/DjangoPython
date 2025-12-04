import streamlit as st
import math as mt
#Problema Medida
TITULO = "Cálculo da área de um quadrado, triângulo e trapézio"


st.markdown(f"<h1 style='text-align: center;'>{TITULO}</h1>", unsafe_allow_html=True)
#Entrada de Dados
medidaA = st.number_input("Inserir a medida A:")
medidaB = st.number_input("Inserir a medida B:")
medidaC = st.number_input("Inserir a medida C:")
#Processamento de Dados
areaQuadrado = mt.pow(medidaA,2)
areaTriangulo = (medidaA * medidaB) / 2
areaTrapezio = ((medidaA + medidaC) * medidaB / 2)
#Saída de Dados
st.markdown("<h2 style='text-align: left;'>Resultados:</h2>", unsafe_allow_html=True)
st.write(f"A área do quadrado é: {areaQuadrado:.4f}")
st.write(f"A área do triângulo é: {areaTriangulo:.4f}")
st.write(f"A área do trapézio é: {areaTrapezio:.4f}")
