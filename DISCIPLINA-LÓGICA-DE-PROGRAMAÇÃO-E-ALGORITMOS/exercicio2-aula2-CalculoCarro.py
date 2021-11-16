#Exercício2: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
#pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço
#a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.

print("Começando exercício 2!")
print("_*_" *30)

#Perguntando ao usuário a quantidade de km percorridos e quantos dias ele possui o carro alugado: 
QuantidadeDeKmPercorridos = float(input("Quantos KM foram percorridos? "))
QuantidadeDeDiasAlugados = float(input("Quantos dias o carro está sendo alugado? "))

#Cálculo do preço de Km's rodados: 
CalculoKmsRodados = (QuantidadeDeKmPercorridos * 0,15)