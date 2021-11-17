#Exercicio 3 - Crie uma variável de string que receba uma frase qualquer. Crie uma segunda variável, 
#agora contendo a metade da string digitada. Imprima na tela somente os dois últimos caracteres
#da segunda variável do tipo string. 

print("Começando Exercicio 3!")
print("_*_" *30)

#Criando a variável pedindo a frase aleátorio ao usuário: 
String1 = input("Informe uma frase: ")
#Vendo o tamanho dela com a função len().
TamanhoDaString1 = len(String1)

#Variavel para que peguemos a metade da frase: 
MetadeDaString1 = String1[:int(TamanhoDaString1/2)] #Colocamos o int() para que pegue a parte inteira apenas da metade da String1, pois dependendo do seu tamanho, pode vir com número com virgula. Colocamos ela dividida por 2 pois precisamos da metade dela.

#Imprimindo apenas os dois últimos caracteres da metade da string.
print(MetadeDaString1[2:])

print("Obrigada por usar nosso programa!")

