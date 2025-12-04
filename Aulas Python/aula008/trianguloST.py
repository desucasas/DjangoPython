import streamlit as st
def triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

st.title(" Verifica o tipo de triângulo com base nos lados fornecidos")
st.markdown("Insira o comprimento dos três lados para análise.")


a=float(st.number_input("Digite o valor do lado a", min_value=0))
b=float(st.number_input("Digite o valor do lado b", min_value=0))
c=float(st.number_input("Digite o valor do lado c", min_value=0))

#Entrada de Dados
if st.button("Verificar tipo de triângulo"):
    st.write(triangulo(a, b, c))
#Condições de existência do triângulo
    if not triangulo(a, b, c):
        st.error("Os valores fornecidos não formam um triângulo válido. ❌")
        st.stop()
#Classificação por lados
    if a == b == c:
        return "É um triângulo Equilátero."
    elif a == b or b == c or a == c:
        return "É um triângulo Isósceles."
    else:
        return "É um triângulo Escaleno."
   
#Cálculo do perímetro
    perimetro = a + b + c
    st.success(f"É um triângulo válido! ✅ Perímetro: **{perimetro:.2f}**")

    

