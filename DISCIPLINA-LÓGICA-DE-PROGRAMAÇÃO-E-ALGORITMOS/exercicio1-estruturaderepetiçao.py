#EXERCICIO 1: Realize a sequência de print com for e while.
#A: Inteiros de 3 até 12, incluso o 12.
#B: Inteiros de 0 até 9, excluindo 9, com passo de 2.

print("ATIVIDADES DE LAÇOS DE REPETIÇÃO!")
print("_*_" *30)

print("EXERCICIO 1. LETRA A:")

print("ESTRUTURA FOR: ")

for numeros in range (3, 13, 1):
    print(numeros)

print("ESTRUTURA WHILE: ")
#Atribuindo 3 na variavel x
x = 3
#Enquanto x for menor ou igual a 12, faça:
while (x <= 12):
    print(x)
    #Implementando 1 no x, toda vez que ele executa o print, ele soma 1 no x lá em cima, sucessivamente até ar 12.
    x += 1

print("EXERCICIO 1. LETRA B: ")

print("ESTRUTURA FOR: ")

for number in range (0, 9, 2):
    print(number)

print("ESTRUTURA WHILE: ")

y = 0
while (y <= 8):
    print(y)
    y += 2

print("_*_" *30)

print("RESOLUÇÃO DE PROBLEMAS!")
#Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: 
#adição, subtração, multiplicação, divisão e sair. Exiba na tela o resultado da operação desejada.
#Repita até que a opção saída seja escolhida. 

print("CALCULADORA.")
print("ESCOLHA UMA OPÇÃO PARA REALIZAR A OPERAÇÃO DESEJADA: ")
print("1 - ADIÇÃO (+)")
print("2 - SUBTRAÇÃO (-)")
print("3 - MULTIPLICAÇÃO (*)")
print("4 - DIVISÃO (/)")
print("CASO QUEIRA ENCERRAR O PROGRAMA, POR FAVOR, DIGITE: SAIR.")
print("_*_" *30)