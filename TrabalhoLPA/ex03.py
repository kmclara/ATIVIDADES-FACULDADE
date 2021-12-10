import os
from time import sleep

# FUNÇÕES ÚTEIS


def exibirDivisorVisual(caractereParaExibir):
    print("\n" + caractereParaExibir * 100 + "\n")


def exibirMenu():
    # Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')

    # Exibe o título "HOTEL DOS ANIMAIS"
    print("HOTEL DOS ANIMAIS")

    # Exibe as regras do jogo
    print("""
- O rato não pode ficar ao lado do gato.
- O cão não pode ficar ao lado do osso.
- O gato não pode ficar ao lado do cão.
- O queijo não pode ficar ao lado do rato
  """)

    # Exibe na tela uma matriz 2x4 de posições dos quartos, numerados de 1 a 8
    print("""
Especificando Posição:

-----------------
| 1 | 2 | 3 | 4 |
-----------------
| 5 | 6 | 7 | 8 |
-----------------
  """)


def exibirTituloDaFase(numeroDaFase):
    print("Bem Vindos a Fase {}!".format(numeroDaFase))


def exibirMensagemDeVitoria(numeroDaFase):
    print("\nParabéns, você venceu a Fase {}!".format(numeroDaFase))
    sleep(2)


# Exibir mensagem de fim de jogo e sair do programa
def gameOver():
    print("GAME OVER!")
    exit()


# ####################################################################################################


exibirMenu()
exibirDivisorVisual("-")

exibirTituloDaFase(1)

# Exibe as regras para a fase 1
print("""
Na Fase 1, você deve alocar o RATO e o GATO na seguinte matriz que representa os quartos:

-----------------
| * | * |   | G |
-----------------
| R |   | * | * |
-----------------
""")

# Pergunta a posição do RATO e do GATO, e salva em uma variável
posicaoRato = int(input("\nEm qual posição quer alocar o RATO? "))
posicaoGato = int(input("Em qual posição quer alocar o GATO? "))

if (posicaoRato, posicaoGato) == (6, 3):
    exibirMensagemDeVitoria(1)
else:
    gameOver()


# ####################################################################################################

exibirMenu()
exibirDivisorVisual("-")

exibirTituloDaFase(2)

# Exibe as regras para a fase 2
print("""
Na Fase 2, você deve alocar o CÃO, CÃO e o OSSO na seguinte matriz que representa os quartos:

-----------------
|   | * | * | * |
-----------------
| * | C |   |   |
-----------------
""")

# Pergunta a posição do CÃO, do CÃO e do OSSO, e salva em uma variável
posicaoCao = int(input("Em qual posição quer alocar o CÃO? "))
posicaoCao2 = int(input("Em qual posição quer alocar o outro CÃO? "))
posicaoOsso = int(input("Em qual posição quer alocar o OSSO? "))

# O osso deve ficar obrigatoriamente no quarto 1
if posicaoOsso == 1:
    exibirMensagemDeVitoria(2)
else:
    gameOver()


# ####################################################################################################

exibirMenu()
exibirDivisorVisual("-")

exibirTituloDaFase(3)

# Exibe as regras para a fase 3
print("""
Na Fase 3, você deve alocar o GATO, RATO e OSSO na seguinte matriz que representa os quartos:

-----------------
|   | * | * | * |
-----------------
|   | G |   | * |
-----------------
""")

# Pergunta a posição do GATO, do RATO e do OSSO, e salva em uma variável
posicaoGato = int(input("Em qual posição quer alocar o GATO? "))
posicaoRato = int(input("Em qual posição quer alocar o RATO? "))
posicaoOsso = int(input("Em qual posição quer alocar o OSSO? "))

# O rato deve ficar no quarto 1 e o osso no quarto 5
if (posicaoRato, posicaoOsso) == (1, 5):
    exibirMensagemDeVitoria(3)
else:
    gameOver()


# ####################################################################################################

exibirMenu()
exibirDivisorVisual("-")

exibirTituloDaFase(4)

# Exibe as regras para a fase 4
print("""
Na Fase 4, você deve alocar QUEIJO, QUEIJO e OSSO na seguinte matriz que representa os quartos:

-----------------
|   |   |   | * |
-----------------
| * | R | * | * |
-----------------
""")

# Pergunta a posição do QUEIJO, do QUEIJO e do OSSO, e salva em uma variável
posicaoQueijo = int(input("Em qual posição quer alocar o QUEIJO? "))
posicaoQueijo2 = int(input("Em qual posição quer alocar o outro QUEIJO? "))
posicaoOsso = int(input("Em qual posição quer alocar o OSSO? "))

if (posicaoQueijo, posicaoQueijo2, posicaoOsso) == (1, 3, 2):
    exibirMensagemDeVitoria(4)
else:
    gameOver()


# ####################################################################################################

# Limpa a tela
os.system("cls" if os.name == "nt" else "clear")

# Mostra mensagem de vitória
print("\nPARABENS, VOCÊ VENCEU O JOGO!")
