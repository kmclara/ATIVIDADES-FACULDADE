for i in range (5, 10, 2):
    print(i)

for i in range (10, 0, -2):
    print(i)

#Algoritmo que calcula a media dos números pares de 1 a 100

#Atribuindo valores nas variaveis com 0:
soma = 0
quantidade = 0
#Utilizaando laço de repetição for
for i in range (1, 101):
    #Verificando se ele é par, se ele for, faço a somatória mais a contagem de quantidade: 
    if i % 2 ==0:
        soma += i
        quantidade += 1
#Cálculando a média: 
media = soma/quantidade
print("A média de números pares entre 1 e 100 é de {}".format(media))
