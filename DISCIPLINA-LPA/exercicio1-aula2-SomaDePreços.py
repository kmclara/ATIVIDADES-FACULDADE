#Exercício1: Desenvolver um algoritmo que solicite ao usuário o preço de um produto e um percentual
#de desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto.

print("Começando o exercício 1!")
print("_*_" *30)

#Perguntando ao usuário o preço do produto e seu percentual de desconto: 
PrecoDoProduto = float(input("Qual o preço do produto escolhido? "))
PercentualDeDescontoDoProduto = float(input("Qual o percentual de desconto do produto? "))

#Calculando o percentual de desconto do produto: 
CalculoPercentualEPrecoProduto = PrecoDoProduto * (PercentualDeDescontoDoProduto / 100)
#Calculando o preço final do produto:
CalculoPrecoFinalDoProduto = PrecoDoProduto - CalculoPercentualEPrecoProduto 

#Resultado para ao usuário: 
print("O desconto do produto é de {}%! E o preço final do produto é de R${}!".format(CalculoPercentualEPrecoProduto, CalculoPrecoFinalDoProduto))
