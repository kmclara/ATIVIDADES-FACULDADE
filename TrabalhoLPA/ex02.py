# Pega o nome do usuário
nome = input("Digite um nome: ")

# Converte o nome para maiúsculo
nomeEmMaiusculo = nome.upper()


# Substitui as vogais do nome pelos códigos
# A = @, E = &, I = !, O = #, U = *
nomeCodificado = nomeEmMaiusculo.replace(
    "A", "@").replace("E", "&").replace("I", "!").replace("O", "#").replace("U", "*")

# Imprime o nome codificado
print(nomeCodificado)
