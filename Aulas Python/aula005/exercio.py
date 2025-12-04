import streamlit as st
st.title("Caixa Registradora Simples")
#Entrada de dados
valor = st.number_input("Valor unitário do produto:")
quantidade = st.number_input("Quantidade:", step=1)
pagamento = st.number_input("Valor recebido R$:")
totalcompra = valor * quantidade
troco = pagamento - totalcompra 
#Saída de dados
st.write(f"Valor unitário do produto é: {valor:.2f}")
st.write(f"Quantidade de produtos é: {quantidade}")
st.write(f"Valor da compra: {totalcompra:.2f}")
st.write(f"Valor do troco: {troco:.2f}")
