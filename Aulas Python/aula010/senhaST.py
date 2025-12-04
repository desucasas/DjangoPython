import streamlit as st
#Problema senha fixa
st.title("Sistema de Login Simples")
#Declaração de constantes
USUARIO = "clodoaldo"
SENHA = "senha123"
#Entrada de dados
usuario_entrada = st.text_input("Nome do usuário:")
senha_entrada = st.text_input("Senha", type="password")
#Estrutura de controle em loop
botao = st.button("Logar")
#Tentativas de acesso
MAXIMO_TENTATIVAS = 3
if 'tentativas' not in st.session_state:
    st.session_state.tentativas = 0
if botao is True:
    if st.session_state.tentativas >= MAXIMO_TENTATIVAS:
        st.error("Máximo de tentativas atingido. Acesso bloqueado.")
    else:
        #Usar o WHile para controlar as tentativas
        while st.session_state.tentativas < MAXIMO_TENTATIVAS:
            if usuario_entrada == USUARIO and senha_entrada == SENHA:
                st.success("Login bem sucedido!")
                st.session_state.tentativas = 0
                break
            else:
                st.session_state.tentativas += 1
                st.warning(f"Credenciais inválidas. Tentativa {st.session_state.tentativas} de {MAXIMO_TENTATIVAS}")
                break
    
