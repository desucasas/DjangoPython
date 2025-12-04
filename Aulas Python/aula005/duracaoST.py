import streamlit as st
#Problema Duração de tempo
TITULO = "Calculadora e duração de tempo"
st.set_page_config(page_title=TITULO)
st.title(TITULO)
#Entrada de Dados
tempo = st.number_input("Digite o tempo em segundos:", min_value=0, step=1, help="Insira a duração total em segundos para converter em horas, minutos e segundos.")
#Processamento de Dados
horas = tempo // 3600 #Cálculo das horas
minutos = (tempo % 3600) // 60 #Cálculo dos minutos
segundos = tempo % 60 #Cálculo dos segundos
#Saída de Dados
st.write(f"{horas} horas, {minutos} minutos e {segundos} segundos")