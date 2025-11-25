# Classe Principal
class Contribuinte:
    # 1. Herança: 
    def __init__(self, nome, renda_anual):
        self.nome = nome
        self.renda_anual = renda_anual

    # 2. Polimorfismo: 
    def calcular_imposto(self):
        return 0.0

#Classe Filha - PF (Pessoa Física)
class PessoaFisica(Contribuinte):
    # 1. Herança: 
    def __init__(self, nome, renda_anual, gastos_saude):
        super().__init__(nome, renda_anual)
        self.gastos_saude = gastos_saude 

    # 2. Polimorfismo: 
    def calcular_imposto(self):
        renda = self.renda_anual
        # Regra de Alíquota
        if renda < 20000.00:
            aliquota = 0.15 # 15%
        else:
            aliquota = 0.25 # 25%
        imposto_bruto = renda * aliquota
        
        # Abatimento
        abatimento = self.gastos_saude * 0.50
        
        imposto_final = imposto_bruto - abatimento
        
        # Garante que o imposto não seja negativo
        return max(0.0, imposto_final)

# Classe Filha - PJ (Pessoa Jurídica)
class PessoaJuridica(Contribuinte):
    # 1. Herança:
    def __init__(self, nome, renda_anual, num_funcionarios):
        super().__init__(nome, renda_anual)
        self.num_funcionarios = num_funcionarios

    # 2. Polimorfismo:
    def calcular_imposto(self):
        renda = self.renda_anual
        # Regra de Alíquota (baseada no número de funcionários)
        if self.num_funcionarios > 10:
            aliquota = 0.14 # 14%
        else:
            aliquota = 0.16 # 16%
        imposto_final = renda * aliquota
        return imposto_final

# --- LÓGICA PRINCIPAL (Exemplo de Uso) ---
def exemplo_simples_uso():
    # Cria uma lista polimórfica (aceita ambos os tipos de objetos)
    lista_contribuintes = []

    # Criação de objetos
    pf1 = PessoaFisica("Maria", 50000.00, 2000.00) 
    pj1 = PessoaJuridica("Empresa ABC", 400000.00, 25)
    
    lista_contribuintes.append(pf1)
    lista_contribuintes.append(pj1)

    print("--- Cálculo de Impostos Simplificado ---")
    
    total_arrecadado = 0.0

    # Polimorfismo: O loop chama o método calcular_imposto() correto para cada objeto
    for c in lista_contribuintes:
        imposto = c.calcular_imposto()
        total_arrecadado += imposto
        
        print(f"Contribuinte: {c.nome}")
        print(f"Imposto a pagar: R$ {imposto:.2f}\n")
        
    print(f"Total Arrecadado: R$ {total_arrecadado:.2f}")

# Rode este exemplo para ver o código em ação!
exemplo_simples_uso()