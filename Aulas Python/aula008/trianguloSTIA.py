import streamlit as st
import math # Importamos a biblioteca math, caso precisemos de funções mais avançadas no futuro

def analisar_e_calcular_triangulo(a, b, c):
    # ... lógica ...
    return classificacao, perimetro

st.title("Descubra o Tipo de Triângulo e Calcule seu Perímetro!")")

# Entrada de Dados do Usuário
a = st.number_input("Comprimento do Lado A:", min_value=0)
b = st.number_input("Comprimento do Lado B:", min_value=0)
c = st.number_input("Comprimento do Lado C:", min_value=0)

#Botão para Analisar o Triângulo
if st.button("Analisar Triângulo"):
    if a <=0 or b <=0 or c <=0:
        st.error("Os comprimentos dos lados devem ser maiores que zero. Favor corrigir os valores.")
        st.stop()

mensagem_tipo, perimetro_calculado = analisar_e_calcular_triangulo(a, b, c)

# Pocessamento dos Resultados

mensagem_tipo, perimetro_calculado = analisar_e_calcular_triangulo(a, b, c)

#Resultado
    st.info(f"Classificação: **{mensagem_tipo}**")

