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

print("Podemos observar que depois de cada percentual, foi colocado letras diferentes, isso porque há uma separação!")
print("A separação é: ")
print("%d e %i: Números inteiros.")
print("%f: Números de ponto flutuante.")
print("%s: Strings.")

print("_*_" *30)

#Definindo casas decimais: 
print("Para que não fique mais casas depois a virgula, podemos formatar para que fique quantas casas quisermos depois da virgula.")
print("No jeito de formatação com %, usamos da seguinte forma: ")

NotaDoUniveristario = 8.5
Matéria = "Lógica"
Resultado = "A nota foi de %.2f na disciplina de %s." %(NotaDoUniveristario, Matéria)
print(Resultado)

print("A formatação/definição foi feita na seguinte parte - .2 - no %f.")

print("Agora, se formos fazer isso com o .format(): ")

NotaDoUsuário = 17.5
NomeDoUsuário = "João"
ResultadoParaOUsuário = "A nota de {} foi {:.2f}!".format(NomeDoUsuário, NotaDoUsuário)

print(ResultadoParaOUsuário)

print("Aqui colocamos a formatação das casas decimais dentro das chaves.")

print("_*_" *30)

#Fatiamento
print("Podemos recordar/fatiar um pedaço da string.")

String4 = "Lógica de Programação e Algoritmos"
print(String4[0:6])

print("Obs: Sempre se conta um a menos. Então se você quiser fatiar uma string que vai do 0 ao 5, como foi o caso acima, sempre deve colocar um a mais.")
print("Então, ao invés de ficar [0:5] irá ficar [0:6].")
