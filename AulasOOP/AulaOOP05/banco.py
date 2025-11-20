class ContaPessoaFisica:
    # 1º Membro - Atributos Privados
    __numeroDaConta: int
    __titular: str
    __saldo: float

    # 2º Membro - Propriedades
    # Propriedade do numero da conta

    @property
    def _numeroDaConta(self) -> int:
        return self.__numeroDaConta
    @_numeroDaConta.setter
    def _numeroDaConta(self, numero:int) ->int :
        self._numeroDaConta = numero
    
    #Propriedade Titular
    @property
    def _titular(self) -> str:
        return self.__titular
    @_titular.setter
    def _titular(self, nome:str) -> str:
        self.__titular = nome

    #Propriedade Saldo
    @property
    def _saldo(self) -> float:
        return self.__saldo
    @_saldo.setter
    def _saldo(self, saldo: float) -> float:
        self.__saldo = saldo


    #3° Membro - Construtor
    def __init__(self, numeroDaConta:int, titular:str, saldo:float):
        self._numeroDaConta = numeroDaConta
        self._titular = titular
        self._saldo = saldo
   
    #4° Membro - Métodos
    def depositar(self, deposito:float) -> float:
        self._saldo += deposito
    def saque(self, saque:float) -> float:
        self._saldo -= saque
        

    #---Fim super classe---

class ContaPessoaJuridica(ContaPessoaFisica):#Sub classe da classe Conta Pessoa Fisica
    #1° Membro - Atributos
    __limite:float

    #2° Membro - Propriedades
    @property
    def _limite(self) -> float:
        return self.__limite
    @_limite.setter
    def _limite(self, limite) -> float:
        self.__limite = limite

    #3° Membro - Construtor
    def __init__(self, numeroDaConta, titular, saldo, limite):
        super().__init__(numeroDaConta, titular, saldo)
        self._limite = limite
   
    #4° Membro - Métodos
    def limiteDisponivel(self) -> float:
        return self._limite
    #----Fim sub classe----

class ContaPoupanca(ContaPessoaFisica):
    #1º Membro - Atributos
    __taxaDeJuros = 0.05

    #2º Membro - Propriedades
    @property
    def __taxaDeJuros(self) -> float:
        return self.__taxaDeJuros
    
    #3º Membro - Construtor
    def __init__(self, numeroDaConta, titular, saldo):
        super().__init__(numeroDaConta, titular, saldo)

    #4º Membro - Métodos
    def limiteDisponivel(self) -> float:
        return self._limite
    
    def saque(self, saqui:float) -> float: #Sobrescrita do método saque
        self._saldo -= saque
        return self._saldo
    
    def atualizarSaldo(self) -> float:
        self._saldo += self._saldo * self.__taxaDeJuros
        return self._saldo
    
# ---------------Fim classes------------- #

#Programa principal

conta1 = ContaPessoaFisica(123456, "Clodoaldo", 1000)
conta2 = ContaPessoaJuridica(654321, "Adriano", 500, 100)
conta3 = ContaPoupanca(789, "Vitor", -100)


#Saida de Dados 1

print(f'''
      
)