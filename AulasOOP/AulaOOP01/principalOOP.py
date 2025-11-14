import AulasOOP.AulaOOP01.trianguloOOP as tl

#Instanciar classe
trianguloX = tl.triangulo()
trianguloY = tl.triangulo()

#Entrada de Dados
print("Digite as medidas do triângulo X:")
trianguloX.a = int(input("Digite a medida de a: "))
trianguloX.b = int(input("Digite a medida de b: "))
trianguloX.c = int(input("Digite a medida de c: "))

print("Digite as medidas do triângulo Y:")
trianguloY.a = int(input("Digite a medida de a: "))
trianguloY.b = int(input("Digite a medida de b: "))
trianguloY.c = int(input("Digite a medida de c: "))

#Processamento de dados

#p = ((trianguloX.a + trianguloX.b + trianguloX.c) / 2)
#areax = (p * (p - trianguloX.a) * (p - trianguloX.b) * (p - trianguloX.c)) ** 0.5
areax = trianguloX.area()
areay = trianguloY.area()

#p = ((trianguloY.a + trianguloY.b + trianguloY.c) / 2)
#areay = (p * (p - trianguloY.a) * (p - trianguloY.b) * (p - trianguloY.c)) ** 0.5

#Condicional para verificar qual triângulo é maior

if areax > areay:
    saida = "A área do triângulo X é maior que a área do triângulo Y."
elif areay > areax:
    saida = "A área do triângulo Y é maior que a área do triângulo X."
else:
    saida = "As áreas dos triângulos são iguais."    

#Saída de Dados

print(f"A área do triângulo X é igual a {areax :.1f}")
print(f"A área do triângulo Y é igual a {areay :.1f}")
print(saida)

