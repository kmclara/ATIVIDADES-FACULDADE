#Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma 
#pessoa. Se a pessoa tiver menos de 3 anos de idade, o ingressa será gratuito, se tiver
#entre 3 e 12 anos, o ingresso custará R$15, se tiver mais de 12 anos, custará R$ 30
#Primeiro:
#Escreva um laço em que vocẽ pergunte a idade dos usuários, e então, informe-lhes o preço
#dos ingressos do cinema.
#Segundo: 
#Encerre o laço usando um break quando o usuário digitar sair.
#Terceiro:
#Após encerrar o laço, apresente na tela o total de pessoas que compraram ingressos, o total de dinheiro
#arrecadado e a média de idade das pessoas. 

print("_________"*30)

TotalPessoas = 0
TotalDinheiro = 0

#Adicionando pergunta de idade ao usuário dentro de um laço de repetição: 
while True:
    IdadeDoUsuário = input("Nos infome sua idade: ")
    if IdadeDoUsuário == "sair":
        break
    IdadeDoUsuário = int(IdadeDoUsuário)
    TotalPessoas += 1
    if IdadeDoUsuário < 3:
        Ingresso = 0
    elif IdadeDoUsuário > 12:
        Ingresso = 30
    else:
        Ingresso = 15
    TotalDinheiro += Ingresso

MediaIdadePessoas = TotalDinheiro / TotalPessoas

print("Total de Pessoas: {}".format(TotalPessoas))
print("Total Arrecadado: {}".format(TotalDinheiro))
print("Total Média Arrecadada: {}".format(MediaIdadePessoas))