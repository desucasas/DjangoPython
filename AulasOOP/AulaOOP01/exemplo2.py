#Importar o modulo
import AulasOOP.AulaOOP01.produtoOOP as p

#Instanciar o objeto
p1 = p.Produto()

#Entrada de Dados
print("Digite os dados do produto")
p1.nome = input("\tNome: ")
p1.preco = float(input("\tPreco: R$"))
p1.saldo = int(input("\tQuantidade: "))

#Saída de dados 1
#print("Dados do Produto")
#print(f"\tNome do Produto: {p1.nome}")
#print(f"\tValor de Compra: R$ {p1.preco}")
#print(f"\tQuantidade em Estoque: {p1.saldo}")
#print(f"Valor Total em Estoque: R$ {p1.valorTotalEmEstoque():.2f}")

print(p1.dadosDoProduto())

#Adicionar Produtos
q = int(input("Digite a quantidade de produto a ser adicionado ao estoque:"))
p1.adicionarProdutos(q)

#Saída de Dados - 2
print("--Dados atualizados--")
print(p1.dadosDoProduto())

#Remover Produtos

q= int(input("Digite o número de produtos a ser removido ao estoque:"))
p1.removerProdutos(q)

#Saída de Dados 3

print("--Dados Atualizados--")
print(p1.dadosDoProduto())