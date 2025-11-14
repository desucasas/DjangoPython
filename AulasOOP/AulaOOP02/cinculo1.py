from calculadora import calculadora1

#Instanciação do objeto
#Circulo = c.calculadora()

#Entrada de Dados
raio = float(input("Digite o valor do raio:"))

#Processamento de Dados
circunferencia = calculadora1.circunferencia(raio)
area = calculadora1.area(raio)

#Saída de Dados
print(f'''Circunferência: {circunferencia:.2f}
    Area: {area:2f}
    PI: {calculadora1.PI}
''')
      

