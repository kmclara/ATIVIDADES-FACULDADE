#Atividade Prática: Escreva um algoritmo que lê um nome e uma idade. Caso o nome digitado seja Vinicius,
#escreva isso na tela. Caso o usuário digite qualquer outro nome, verifique sua idade. Se for menor que 18
#anos, informe que é de menor. Se for maior que 100 anos, informe que está pessoa possivelmente
#não existe.

print("ATIVIDADE PRÁTICA - AULA 3 - CONDICIONAIS DE MÚLTIPLA ESCOLHA - ELIF")
print("_*_" *30)

#Perguntando o nome do usuário:
NomeDoUsuario = str(input("Digite seu nome: "))

#Perguntando ao usuário a sua idade:
IdadeDoUsuario = int(input("Por favor, nos informe a sua idade: "))

#Condições/Condicionais:
if NomeDoUsuario == "Vinicius":
    print("Olá Vinicius! Muito prazer em te conhecer!")
elif IdadeDoUsuario < 18:
    print("Olá {}. Aparentemente você não é o Vinicius e possui menos de 18 anos.".format(NomeDoUsuario))
elif IdadeDoUsuario >= 100:
    print("Bom, {}, acho que você não existe!".format(NomeDoUsuario))
else:
    print("Ok {}, você é maior de idade, porém não é o Vinicius!".format(NomeDoUsuario))
    

