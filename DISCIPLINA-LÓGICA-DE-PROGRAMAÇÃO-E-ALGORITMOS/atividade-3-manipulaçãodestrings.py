#Manipulação Avançada de Strings - Exemplos. 

print("Alguns exemplos de manipulação de strings e explicações.")
print("_*_" *30)

#Concatenação de Strings:
print("Na concatenação de strings, fazemos a junção ou soma de duas strings.")
print("Se usa o sinal de + para realizar a concatenação!")
print("Exemplo: ")

String1 = "Lógica de Programação "
String2 = String1 + "e Algoritmos"
print("A concatenação se resultará em: {}".format(String2))

print("_*_" *30)

#Repetindo Strings na Concatenação:
print("Exemplo: ")
String3 = "A" + "-" *10 + "B"
print(String3)

print("A repetição ocorreu com o traço, com o auxilio da multiplicação - *30 -.")
print("Pode-se usar isso para qualquer repetição de string, com qualquer numeração que você deseja que se multiplique!")

print("_*_" *30)

#Composição:
print("A composição serve para juntarmos diferentes variáveis e strings.")
print("Exemplo: ")

NotaDoAluno = 8.5
ResultadoParaOAluno = "Sua nota é %f na disciplina de Lógica de Programação e Algoritmos!" %NotaDoAluno
print(ResultadoParaOAluno)

print("O sinal de %f serve para que coloquemos o valor da variavel que desejarmos ali.")
print("E o % no final da frase, para que indiquemos que variavel queremos que fique no lugar de %f.")
print("Este comando se assemelha muito com o .format(), só que mais antigo.")

print("_*_" *30)

#Composição com várias variáveis:
print("Exemplo: ")

NotaDoEstudante = 8.5
Disciplina = "Algoritmos"
Resultado = "A nota foi de %.2f na disciplina de %s!" %(NotaDoEstudante, Disciplina)
print(Resultado)