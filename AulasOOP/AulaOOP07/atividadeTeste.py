from abc import ABC, abstractmethod

#Super Classe

class Contribuinte(ABC):
    __nome: str
    __renda_anual: float

#Construtor
    def __init__(self, nome:str, renda_anual: float):
        self._nome = nome
        self._renda_anual = renda_anual

#Método
@abstractmethod
def calcular_imposto(self) -> float:
    # Não tem código aqui, pois a regra é diferente para PF e PJ!
    pass

#Propriedade - Nome
@property
def nome(self):
    return self._nome

#Propriedade - Renda Anual
@property
def renda_anual(self):
    return self._renda_anual

@renda_anual_setter
def renda_anual(self, nova_renda):
    if renda_anual >= 0:
        self._renda_anual = nova_renda
    else:
        print("Erro de validação: A renda anual não pode ser negativa!")

#--- FIM CLASSE PRINCIPAL ---#

#-CLASSE FILHA - PF (PESSOA FÍSICA)

class PessoaFisica(Contribuinte):

#Construtor
def __init__(self, nome:str, renda_anual:float, gastos_saude:float):
    super().__init__(nome, renda_anual)
#Atributo   
    self.gastos_saude = gastos_saude
#Implementação
    def calcular_imposto(self) -> float:
        renda = self.renda_anual
#Definições
    if renda < 20000.00:
        aliquota = 0.15 #15%
    else:
        aliquota = 0.25
    imposto_bruto = renda * aliquota

    
    
