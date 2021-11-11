#Desenvolver um algoritmo que solicite ao usuário dois números inteiros. Imprima a soma destes dois números
#na tela!

#Solicitando ao usuário dois números:
print("Para saber a soma de pai e filho, responda as questões abaixo, e aguarde o resultado!")

IdadeFilho = int(input("Digite a idade do filho: "))
IdadePai = int(input("Digite a idade do pai: "))

#Realizando a soma das idades: 
SomaDasIdades = (IdadeFilho+IdadePai)

#Resultado do programa:
print("Olá! As idades informadas foram: Filho - {}, Pai - {}.".format(IdadeFilho, IdadePai))
print("A soma de ambas foi de {}! Obrigada por usar nosso programa!".format(SomaDasIdades))