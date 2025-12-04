#-------------Lista em Python-------------#
#Indices 0          1    2   3
lista = ["Senai", True, 22, 3.5]
print(lista)
print(type(lista))
print(lista[2])
print(len(lista))
lista.insert(1, "Campeão")
lista.insert(2, "Sucasas")
print(lista)
lista.insert(3, "Sucasas")
lista.append("Sucasas")
print(lista)
print(type(lista))
print(len(lista))
for i in range(len(lista)):
    print(lista[i])

#-------Tupla-------#
#Indices    0       1    2   3
tupla = ("Senai", True, 56, 74.6)
print(type(tupla))
print(tupla)
print(type(tupla))
print(tupla[3])
print(tupla[1])
tupla.insert(1, "Campeao")
del tupla[1]


#-----Dicionário-----#

dicionario = {"nome": "Senai", "logica": False, "num1" : 2, "num2" : 1.5}
print(dicionario)
print(type(dicionario))
print(dicionario["logica"])
for chave in dicionario.keys():
    print(chave, "->", dicionario[chave])
dicionario.update({"novo": "Senai"})
dicionario.update({"novo": "Terca"})
del dicionario["logica"]


#-----Conjunto-----#
conjunto = {"Senai", False, 10, 2.69, True, 3}
print(conjunto)
print(type(conjunto))
conjunto.add(23)
conjunto.add(21)
conjunto.discard(21)
conjunto.clear()