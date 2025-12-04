import streamlit as st

st.title("Classificação de níveis de glicose no sangue")
st.markdown(
    """
| Nível de glicose | Classificação   |
| ---------------- | --------------- |
| 0-70 mg/dL       | Hipoglicemia    |
| 71-100           | Normal          |
| 101-140          | Pré-diabetes    |
| 141 ou mais      | Diabetes        |
"""
)

#Entrada de Dados

glicose = st.number_input("Insira o nível de glicose no sangue (mg/dL):", min_value=0)

if st.button("Classificar"):  # botão para classificar o nível de glicose
    if glicose <= 70:
        st.write("Nível de glicose classificado como: Hipoglicemia")
    elif glicose <= 100:
        st.write("Nível de glicose classificado como: Normal")
        st.balloons()
    elif glicose <= 140:
        st.write("Nível de glicose classificado como: Pré-diabetes")
    else:
        st.write("Nível de glicose classificado como: Diabetes")
