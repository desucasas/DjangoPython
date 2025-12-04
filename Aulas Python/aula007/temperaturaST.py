import streamlit as st

def Celsius_Fahrenheit(t):
    return (t * 1.8) + 32

def Celsius_Kelvin(t):
    return t + 273.15

def F_Celsius(t):
    return (t - 32) * 5/9

def F_Kelvin(t):
    return F_Celsius(t) + 273.15

def K_Celsius(t):
    return t - 273.15

def K_Fahrenheit(t):
    return Celsius_Fahrenheit(K_Celsius(t))

def K_Kelvin(t):
    return t

#Problema Temperatura
st.sidebar.title("Conversor de Temperatura")
st.title("Conversor de Temperatura")
st.sidebar.markdown("Converte a temperatura entre Celsius, Fahrenheit e Kelvin")
celsius_selecionado = st.sidebar.checkbox("Celsius", key="temp_celsius")
fahrenheit_selecionado = st.sidebar.checkbox("Fahrenheit", key="temp_fahrenheit")
kelvin_selecionado = st.sidebar.checkbox("Kelvin", key="temp_kelvin")

#Entrada de dados
temp = st.number_input("Valor da Temperatura", format="%.2f", step=1.0)

#Processamento de dados
if st.button("Converter", icon="🌡"):
    if celsius_selecionado:
        st.write(f"{temp}°C em Fahrenheit: {Celsius_Fahrenheit(temp):.2f}°F")
        st.write(f"{temp}°C em Kelvin: {Celsius_Kelvin(temp)}K")
    elif fahrenheit_selecionado:
        st.write(f"{temp}°F em Celsius: {F_Celsius(temp):.2f}°C")
        st.write(f"{temp}°F em Kelvin: {F_Kelvin(temp):.2f}K")
    elif kelvin_selecionado:
        st.write(f"{temp}K em Celsius: {K_Kelvin(temp):.2f}°C")
        st.write(f"{temp}K em Fahrenheit: °F")
    else:
        st.warning("Selecione pelo menos uma unidade para conversão.")    
# Melhor jogo de Termo e desenvolvido por um aluno SENAI              
# Entra no https://muskiguess.onrender.com/