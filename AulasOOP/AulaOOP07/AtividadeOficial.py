from abc import ABC, abstractmethod

#Super Classe
class Contribuinte(ABC):
    __nome:str
    __renda_anual:float

@property
    def __init__(self, nome:str, renda_anual:float):
        self._nome = nome
        self._renda_anual = renda_anual

#Método Abstrato
@abstractmethod
def calcular_imposto(self) -> float:
    pass

#Propriedades para Nome
@property
def nome(self):
    return self._nome

nome.setter
def nome(self, novo_nome):
    self._nome = novo_nome

#Propriedades para Renda Anual
@property
def renda_anual(self):
    return self._renda_anual

@renda_anual.setter
def renda_anual(self, nova_renda):
    if nova_renda >=0
        self._renda_anual = nova_renda
    else:
        print("Erro: A renda anual não pode ser um valor negativo.")