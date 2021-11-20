#Atividade prática: Escreva um algoritmo em python em que o usuário escolhe se quer comprar maçãs,
#laranjas ou bananas. Deverá ser apresentado na tela um menu com as opções: 1- Maçã, 2- Laranja e 3- Banana
#Após escolhida a fruta, deve-se digitar a quantidade que se quer comprar. O algoritmo deve calcular
#o preço total a pagar do produto escolhido e mostra-lo na tela. Considere uma maçã custa R$2.30, uma laranja 3.60 e
#uma banana 1.85

print("ATIVIDADE PRÁTICA - AULA 3 - CONDIÇÕES ANINHADAS - COMPRA DE FRUTAS!")
print("_*_" *30)

#Perguntando o nome ao usuário: 
NomeDoUsuário = str(input("Olá! Por favor, nos informe seu nome: "))

#Pedindo ao usuário para escolher as opções de frutas:
print("Por favor, escolha a fruta que você deseja, {}: ".format(NomeDoUsuário))
print("1- Maçã")
print("2- Laranja")
print("3- Banana")