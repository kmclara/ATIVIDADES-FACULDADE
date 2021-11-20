#Atividade prática: Escreva um algoritmo em python em que o usuário escolhe se quer comprar maçãs,
#laranjas ou bananas. Deverá ser apresentado na tela um menu com as opções: 1- Maçã, 2- Laranja e 3- Banana
#Após escolhida a fruta, deve-se digitar a quantidade que se quer comprar. O algoritmo deve calcular
#o preço total a pagar do produto escolhido e mostra-lo na tela. Considere uma maçã custa R$2.30, uma laranja 3.60 e
#uma banana 1.85

print("ATIVIDADE PRÁTICA - AULA 3 - CONDIÇÕES ANINHADAS - COMPRA DE FRUTAS!")
print("_*_" *30)

#Pedindo ao usuário para escolher as opções de frutas:
print("Por favor, escolha a fruta que você deseja: ")
print("1- Maçã")
print("2- Laranja")
print("3- Banana")

#Perguntando qual foi a sua escolha:
EscolhaDeFrutas = int(input("Qual foi a sua escolha? 1, 2 ou 3? Nós informe, por favor: "))

#Perguntando a quantidade de frutas que ele escolheu:
QuantidadeDeFrutasEscolhida = int(input("Qual a quantidade de fruta escolhida? Digite por favor: "))

#Cálculo das frutas e suas quantidades:
CálculoMaçã = (QuantidadeDeFrutasEscolhida * 2.30)
CálculoLaranja = (QuantidadeDeFrutasEscolhida * 3.60)
CálculoBanana = (QuantidadeDeFrutasEscolhida * 1.85)

#Condições:
if EscolhaDeFrutas == 1:
    print("Você escolheu a fruta 1: Maçã. A quantidade escolhida foi de {} e o preço final será de {}!".format(QuantidadeDeFrutasEscolhida, CálculoMaçã))
else:
    if EscolhaDeFrutas == 2:
        print("Você escolheu a fruta 2: Laranja. A quantidade escolhida foi de {} e o seu preço final de {}!".format(QuantidadeDeFrutasEscolhida, CálculoLaranja))
    if EscolhaDeFrutas == 3:
        print("Você escolheu a fruta 3- Banana. A quantidade escolhida foi de {} e o preço final é de {}! ".format(QuantidadeDeFrutasEscolhida, CálculoBanana))