
print("ETAPAS DE ENSINO!")

while True:
    NomeDaCriança = str(input("Qual o nome do estudante? "))
    IdadeDaCriança = int(input("Qual a idade da criança? "))

    if IdadeDaCriança <=5:
        print("O aluno(a) {} tem {} e está na Educação Infantil.".format(NomeDaCriança, IdadeDaCriança))
    elif IdadeDaCriança >= 6 and IdadeDaCriança <=10:
        print("O aluno(a) {} tem {} anos e está no Ensino Fundamental 1.".format(NomeDaCriança, IdadeDaCriança))
    elif IdadeDaCriança >=11 and IdadeDaCriança <=14 :
        print("O aluno(a) {} tem {} anos e está no Ensino Fundamental 2.".format(NomeDaCriança, IdadeDaCriança))
    elif IdadeDaCriança >=15:
        print("O aluno(a) {} tem {} anos e está no Ensino Médio.".format(NomeDaCriança, IdadeDaCriança))

    EscolhaDoUsuário = (input("Deseja sair? 1- SIM 2- NÃO"))
    if EscolhaDoUsuário == "1":
        break

    
        