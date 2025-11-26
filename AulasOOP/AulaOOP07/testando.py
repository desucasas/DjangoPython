#SUPER CLASSE CONTRIBUINTES

#1° Membro - Atributos
class Contribuintes:
    _nome:str
    _rendaAnual:float

#2° Membro - Propriedades
    @property #Popriedade de nome
    def nome(self) -> str:
        return self._nome
    @nome.setter
    def nome(self, nome:str) -> str:
        self._nome = nome

    @property #Propriedade de renda anual
    def rendaAnual(self) -> float:
        return self._rendaAnual    
    
#3° Membro - Construtor
    def __init__(self, nome:str, rendaAnual:float):
        self._nome = nome
        self._rendaAnual = rendaAnual
#---Fim super classe ---

#CLASSE DA CLASSE CONTRIBUINTES = PESSOA FISICA
class PessoaFisica(Contribuintes): 
#1° Membro - Atributo
    _gastosComSaude:float 

#2° Membro - Propriedades
    @property #Propriedade de gastos com saude
    def gastosComSaude(self) -> float:
        return self._gastosComSaude
    @gastosComSaude.setter
    def gastosComSaude(self, gastosComSaude:float) -> float:
        self._gastosComSaude = gastosComSaude 

#3° Membro - Construtor
    def __init__(self, nome:str, rendaAnual:float, gastosComSaude:float):
        super().__init__(nome, rendaAnual)
        self._gastosComSaude = gastosComSaude

#4° Membro - Métodos
    def calcular_imposto_pessoa_fisica(self):
        if self.rendaAnual < 20000.00:
            imposto_base = self.rendaAnual * 0.15
        else:
            imposto_base = self.rendaAnual * 0.25

        abatimento = self.gastosComSaude * 0.50
        imposto_total = imposto_base - abatimento
        return imposto_total
    
""" pessoas cuja renda foi abaixo de 20000.00 pagam 15% de imposto.
Pessoas com renda de 20000.00 em diante pagam 25% de imposto.
Se a pessoa teve gastos com saúde, 50% destes gastos são
abatidos no imposto.
Exemplo: uma pessoa cuja renda foi 50000.00 e teve 2000.00 em gastos
com saúde, o imposto fica: (50000 * 25%)  + (2000 * 50%) = 11500.00 """

#CLASSE DA CLASSE CONTRIBUINTES = PESSOA FISICA
class PessoaJuridica(Contribuintes):
#1° Membro - Atributo
    _numeroDeFuncionarios:int

#2° Membro - Propriedades
    @property #Propriedade de numero de funcionarios
    def numeroDeFuncionarios(self) -> int:
        return self._numeroDeFuncionarios
    @numeroDeFuncionarios.setter
    def numeroDeFuncionarios(self, numeroDeFuncionarios:int) -> int:
        self._numeroDeFuncionarios = numeroDeFuncionarios

#3° Membro - Construtor
    def __init__(self, nome:str, rendaAnual:float, numeroDeFuncionarios:int):
        super().__init__(nome, rendaAnual)
        self._numeroDeFuncionarios = numeroDeFuncionarios

#4° Membro - Métodos
    def calcular_imposto_pessoa_juridica(self):
        if self.numeroDeFuncionarios > 10:
            imposto = self.rendaAnual * 0.14
        else:
            imposto = self.rendaAnual * 0.16

        return imposto


""" pessoas jurídicas pagam 16% de imposto. 
Porém, se a empresa possuir mais de 10 funcionários, 
ela paga 14% de imposto.
Exemplo: uma empresa cuja renda foi 400000.00 e 
possui 25 funcionários, o imposto fica:
400000 * 14% = 56000.00 """

#FIM DAS CLASSES----------------------

#PROGRAMA PRINCIPAL
pessoaFisica1 = PessoaFisica("Ronaldo", 50000.00, 2000.00)
print(pessoaFisica1.calcular_imposto_pessoa_fisica())

pessoaJuridica1 = PessoaJuridica("Empresa SA", 400000.00, 25)
print(pessoaJuridica1.calcular_imposto_pessoa_juridica())