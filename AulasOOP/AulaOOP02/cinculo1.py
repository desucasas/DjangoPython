import calculadora as c

#Instanciação do objeto
circulo = c.calculadora()

#Entrada de Dados
raio = float(input("Digite o valor do raio:"))

#Processamento de Dados
circunferencia = circulo.circunferencia(raio)
area = circulo.area(raio)

#Saída de Dados
print(f'''Circunferência: {circunferencia:.2f}
    Area: {area:2f}
    PI: {circulo.PI}
''')
      

