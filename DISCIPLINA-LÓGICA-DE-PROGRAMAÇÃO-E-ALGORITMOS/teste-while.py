from typing import Text


x = 1
while (x <= 5):
    print(x)
    x=x+1

#x = 0 
#while(x <= 99):
  #  print(x)
   # x=x+1

soma = 0
contagem = 1 
while (contagem <= 5):
  x = float(input("Digite o nota {}: ".format(contagem)))
  soma +=x #Equivale a soma = x+1
  contagem +=1 #Equivale a contagem = x+1
print("Somatório é {}".format(soma))

Valor = int(input("Digite um valor maior que 0: "))
while (Valor <=0):
  Valor = int(input("Digite um valor maior que 0: "))
print("O valor digitado foi {}. Encerrando programa...".format(Valor))

#Com String
#Situando o usuário: 
print("Digite uma mensagem que irei repetir para você!")
print("Para encerrar, escreva: sair.")
#Adicionando texto para interação:
Texto = input(" ")
#Equanto o texto digitado pelo usuario for diferente da palavra "sair" o programa deve repetir o input de texto
while (Texto != "sair."):
  print(Texto)
  Texto = input(" ")
#Quando o usuário escrever a palvra sair, o programa se encerrará
print("Encerrando programa... ")

print("Digite uma mensagem que irei repetir com você!")
print("Para sair, digite: sair")
#Percebe-se que ao invés de uma condição lógica, apenas usamos um booleano, neste caso, o nosso programa ficaria em um loop infinito, mas usando break, fazerá com que ele pare assim que acharmos necessário.
while True:
  Texto= input(" ")
  print(Texto)
  if Texto == "sair":
    break
print("Encerrando o programa....") 