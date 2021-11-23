#VARIÁVEL, DADOS E SEUS TIPOS. 

#Dado é qualquer coisa que podemos manipular em nosso programa. 
#Variável é um conjunto de endereços que estão na memória, conjunto que possui dados. 

#Atribuição: Na atribuição é quando criamos uma variável e atribuimos ela um valor com o símbolo de "="
#Quando atribuimos uma valor á variável, colocamos aquele valor na memória. 

#Exemplo:

NotaDaDisciplina = 10.0
Disciplina = "Lógica de Programação e Algoritmos"

#Lê-se: A variável "NotaDaDisciplina" recebe o dado 10.0.
#Lê-se: A variável "Disciplina" recebe o dado "Lógica de Programação e Algoritmos"

print(NotaDaDisciplina, Disciplina)

#Regras de Variáveis

print("Regra 1: Não comece uma variável com números! O Python não irá reconhecer!")

#3abc = #Não reconhece! Irá dar erro!

print("Viu? Não reconhece! Mas podemos usar números no meio da variável!")

Variável1 = "Agora essa deu!"

print(Variável1)

print("Regra 2: Inicie um variável com letra ou sublina (_)! ")

DiaDaSemana = "Começando com letras"
_DiaDaSemana = "Começando com sublinha"

print("As variáveis {} e {} deram certo!".format(DiaDaSemana, _DiaDaSemana))

print("Regra 3: Números, letras e sublinhas podem ser colocadas á vontade no meio da variável!")

DiaDaSemana2 = "Variável com número no meio"
Dia_Da_Semana_ = "Variável com sublinha no meio"

print(Dia_Da_Semana_, DiaDaSemana2)
print("Podemos ver que deu certo!")

print("Observação: Não podemos usar exclamção, interrogação, números, espaço, & e nada no incio das nossas variáveis!")
print("Apenas letras e sublinha são permitidas para colocar no inicio das nossas variaveis!")

#Exemplo ERRADO de variável iniciada com exclamação:
#!Nota = 10.0
#Isso está ERRADO! Irá dar erro assim como deu quando colocamos número no inicio da nosso variável!

print("Regra 4: A linguagem Python permite o uso de acentuação, porém, não é recomendado!")
print("Apenas o Python3 permite a acentuação. Demais linguagens de programação não aceitam acentuação.")
print("Por uma questão de costuma e boa prática, não se é recomendado.")

PreçoDoFeijão = "Não se recomenda, mas pode!"
print(PreçoDoFeijão)

PrecoDoFeijao = "Se é recomendado."
print(PrecoDoFeijao)