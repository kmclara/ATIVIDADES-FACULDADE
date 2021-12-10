import os
from random import seed, randint
from time import sleep

# Seed para gerar números aleatórios
seed(100)


def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')


def exibirMenu():
    limparTela()

    print("""
{} MENU {}

[ 1 ]> Nova Inscrição
[ 2 ]> Listar Inscrições
[ 0 ]> Encerrar
""".format('*'*10, '*'*10))


# Função de encerramento
def encerrar():
    print("\nEncerrando...")
    exit()


def novaInscricao():
    limparTela()
    print("\n{} Nova Inscrição {}\n".format('*'*10, '*'*10))
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    telefone = input("Digite seu telefone: ")
    curso = input("Digite o curso: ")

    return {
        'voucher': randint(100, 400),
        'nome': nome,
        'email': email,
        'telefone': telefone,
        'curso': curso
    }


def listarInscricoes(listaDeInscricoes):
    limparTela()
    print("\n{} Lista de Inscrições {}\n".format('*'*10, '*'*10))

    if len(listaDeInscricoes) == 0:
        print("Nenhuma inscrição cadastrada.")
        return

    for inscricao in listaDeInscricoes:
        print("Voucher: {}\nNome: {}\nEmail: {}\nTelefone: {}\nCurso: {}\n".format(
            inscricao['voucher'], inscricao['nome'], inscricao['email'], inscricao['telefone'], inscricao['curso']))
        sleep(0.5)


listaDeVouchers = []

# Loop do programa
while True:
    exibirMenu()
    op = int(input('Digite uma opção: '))

    if op == 1:
        listaDeVouchers.append(novaInscricao())
        print("\nInscrição realizada com sucesso!")

    elif op == 2:
        listarInscricoes(listaDeVouchers)

    elif op == 0:
        encerrar()
    else:
        print('\nOpção inválida!')
    input('\n\nPressione <ENTER> para continuar...')
