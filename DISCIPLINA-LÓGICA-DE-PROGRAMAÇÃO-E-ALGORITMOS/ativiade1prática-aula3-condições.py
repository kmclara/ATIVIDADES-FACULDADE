#Atividade prática 1: Desenvolva um programa que lê dois valores numéricos
#inteiros e compara se o primeio é maior do que o segundo, utilizando uma 
#condicional simples. Caso seja (resultado verdadeiro), ele imprime na tela
#a mensagem informando que o primeiro valor digitado é maior do que o segundo.

print("ATIVIDADE 1 - ATIVIDADE PRÁTICA - AULA 3 - CONDIÇÃO SIMPLES")
print("_*_" *30)

#Pedindo ao usuário dois valores inteiros númericos: 
ValorInteiroNumero1 = int(input("Digite o primeiro valor númerico inteiro: "))
ValorInteiroNumerico2 = int(input("Digite o segundo valor númerico inteiro: "))

#Comparando se o primeiro valor é maior que o segundo valor usando uma condicional simples: 
if ValorInteiroNumero1 > ValorInteiroNumerico2: 
    print("O número {} é maior que o número {}!".format(ValorInteiroNumero1, ValorInteiroNumerico2))

print("_*_" *30)

#Atividade prática 2: Desenvolva um programa que lê um valor inteiro e descobre
#se ele é par ou impar. 

print("ATIVIDADE 2 - ATIVIDADE PRÁTICA - AULA 3 - CONDIÇÃO COMPOSTA")
print("_*_" *30)

#Pedindo um valor inteiro ao usuário:
ValorInteiro = int(input("Digite um valor inteiro: "))

#Condições: 
if (ValorInteiro%2) == 0: #Para saber se um número é par, basta dividir por 2 e se o resto for 0, é impar, por isso usamos a operação matematica % (resto da divisão), e falamos que ela é igual (representado por ==) á 0.
    print("O valor {} é par!".format(ValorInteiro))
else:
    print("O valor {} é impar!".format(ValorInteiro))
