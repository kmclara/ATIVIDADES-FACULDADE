
print("ETAPAS DE ENSINO!")

#Adicionando estrutura de repetição com as variaveis para o usuário colocar nome e idade.
while True:
    nomeDaCrianca = input("Qual o nome do estudante? ")
    idadeDaCrianca = int(input("Qual a idade da criança? "))
#Adicionando condicionais para analisar as idades de acordo com o ensino.
    if idadeDaCrianca <=5:
        print("O aluno(a) {} tem {} e está na Educação Infantil.".format(nomeDaCrianca, idadeDaCrianca))
    elif idadeDaCrianca >= 6 and idadeDaCrianca <=10:
        print("O aluno(a) {} tem {} anos e está no Ensino Fundamental 1.".format(nomeDaCrianca, idadeDaCrianca))
    elif idadeDaCrianca >=11 and idadeDaCrianca <=14 :
        print("O aluno(a) {} tem {} anos e está no Ensino Fundamental 2.".format(nomeDaCrianca, idadeDaCrianca))
    elif idadeDaCrianca >=15:
        print("O aluno(a) {} tem {} anos e está no Ensino Médio.".format(nomeDaCrianca, idadeDaCrianca))
#Adicionando novamente a pergunta e especificando com a condicional se a resposta for 1, para sair. 
    escolhaDoUsuario = (input("Deseja sair? 1- SIM 2- NÃO"))
    if escolhaDoUsuario == "1":
        break

    
        
