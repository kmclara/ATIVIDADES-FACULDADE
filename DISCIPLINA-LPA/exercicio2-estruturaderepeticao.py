#Exercicio 2: Escreva um algoritmo que leia um valor e que imprima a quantidade de cédulas necessárias
#para pagar esse mesmo valor. Para simplificar, vamos trabalhar apenas com valores inteiros
#e com cédulas de R$100, R$50, R$10, R$20, R$5 e R$1.

print("EXERCICIO 1 - AULA PRÁTICA")
print("CAIXA ELETRÔNICO")
print("___" *30)

#Pedindo um valor ao usuário:
Valor = int(input("Digite um valor em R$: "))

while True:
    if Valor >= 100:
        #Pegar a parte inteira da divisão, para sabermos quantas cedulas de 100 cabem no valor descrito pelo usuário
        Cedulas100 = Valor // 100
        Valor -= Cedulas100 * 100
        print("Cédulas e 100: {}".format(Cedulas100))
        if not Valor:
            break
    if Valor >= 50:
        Cedulas50 = Valor // 50
        Valor -= Cedulas50 * 50
        print("Cédulas de 50: {}".format(Cedulas50))
        if not Valor:
            break
    if Valor >= 20:
        Cedulas20 = Valor // 20
        Valor -= Cedulas20 * 20
        print("Cedulas de 20: {}".format(Cedulas20))
        if not Valor:
            break
    if Valor >= 10:
        Cedulas10 = Valor // 10
        Valor -= Cedulas10 * 10
        print("Cédulas de 10: {}".format(Cedulas10))
        if not Valor:
            break
    if Valor >= 5 :
        Cedulas5 = Valor // 5
        Valor -= Cedulas5 * 5
        print("Cédulas de 5: {}".format(Cedulas5))
        if not Valor:
            break
    if Valor:
        Cedulas1 = Valor
        print("Cedulas de 1: {}".format(Cedulas1))
        break