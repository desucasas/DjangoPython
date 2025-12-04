import streamlit as st

#Tabuada
#Titulo da página
TITULO ="Tabuada"
st.title(TITULO)
st.set_page_config("Tabuada")
r#Entrada de dados
n = None
try:    
    n = int(st.text_input("Deseja a tabuada de qual número:"))
    for i in range(1,11):
        saida = f" {n} X {i} = {n*i}"
        st.markdown(f"""{saida}""")
except ValueError:
    if n is None:
        st.warning("Digite algum valor")
    else:
        st.error("Digite somente números inteiros")