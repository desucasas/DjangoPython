# Atributos privados da classe
class contaBancaria:
    __numero:int
    __titular:str
    __saldo:float

#Propriedades para acessar os membros da classe
@property
def numero(self) -> int:
    return self.__numero
@numero.setter
def numero(self, numero) -> int:
    self.__numero = numero

@property
def titular(self) -> str:
    return self.__titular
@titular.setter
def titular(self, titular) -> str:
    self.__titular = titular

@property
def saldo(self, saldo) -> float:
    self.__saldo = saldo

#Construtores
def __init__(self, num:int = 0, titular:str = "", saldo:float = 0.0):
    self.numero = num
    self.titular = titular
    self.saldo = saldo

#Métodos
def depositar(self, quantia):
    self.__saldo = self.__saldo + quantia

def sacar (self, quantia):
    self.__saldo = self.__saldo - quantia

def mostrarDados(self):
    print("Número da conta: ", self.__numero)
    print("Titular da conta: ", self.__titular)
    print("Saldo da conta: R$ %.2f" % self.__saldo)


# ---------------- FIM DA CLASSE ------------------ #


#Progrma Principal

#Entrada de dados
numero = int(input("Digite o numero da conta: "))
titular = str(input("Digite o nome do titular: "))
adriano = str(input("Deseja fazer um deposito inicial? (s/n)"))

if adriano == 's':
    saldo = float(input("Digite o saldo inicial: "))
    conta = contaBancaria(numero, titular, saldo)
else:
    conta = contaBancaria(numero, titular, 0.0)

#-------------- Saida de Dados -----------------#
#Deposito
quantia = float(input("Digite a quantia a ser depositada: R$ "))
conta.depositar(quantia)
print("Dados da conta atualizados: ")
conta.mostrarDados()

#Saque
quantia = float(input("Digite a quantia a ser sacada: R$ "))
conta.sacar(quantia)
print("Dados da conta atualizados: ")
conta.mostrarDados()