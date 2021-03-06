#Atividade 1 - Expressões Algébricas 

print("Exercicios de prática sobre a Aula 2 de Lógica de Programação e Algoritmos.")

#A - O somátorio dos 5 primeiros números inteiros positivos. 
print("Os 5 primeiros números inteiros positivos são: 1, 2, 3, 4 e 5.")
print("Somatório dos números: ")

SomaDosNúmeros = (1 + 2 + 3 + 4 + 5)
print("A soma dos 5 primeiros números inteiros positivos foi de {}.".format(SomaDosNúmeros))

print("_*_" *30)

#B - A media entre 23, 19 e 31.
print("Para se fazer a média entre números, é necessário somar todos e dividir pela quantidade de números.")
print("Nesta atividade, os números para se descobrir a média são: 23, 19 e 31.")

MédiaDosNúmeros = (23+19+31)/3
print("A média dos números 23, 19 e 31 é igual á {:.2f}!".format(MédiaDosNúmeros))

print("Vale lembrar que, neste caso, podemos lembrar da ordem de - preferencia - do Python. Onde, primeiro se resolve o que está nos parenteses, e logo depois, os demais nas sequencias especificadas pelo python.")

print("_*_" *30)

#C - Quantas vezes o número 73 cabe no numero 403.
print("Para sabermos isso, basta dividirmos 403 por 73, e pegar a parte inteira dessa divisão.")
print("Para realizarmos está operação, temos nos operadores matemáticos, um operador especifico para isto, o: // - divisão inteira!")
print("A divisão inteira irá nos retornar justamente aquilo que precisamos, o valor inteiro da divisão.")

DivisãoInteira = (403//73)
print("O número 73 cabe {} vezes no número 403!".format(DivisãoInteira))

print("_*_" *30)

#D - A sobra quando 403 é dividido por 73.
print("Pra calcularmos a sobra de uma divisão, usamos o operador matemático denominado MOD - %.")
print("O mod irá nos retornar o resto da divisão, ou seja, a sobra do mesmo.")

SobraDaDivisão = (403%73)
print("A sobra da divisão entre 403 e 73 é {}!".format(SobraDaDivisão))

print("_*_" *30)

#E - 2 elevado á décima potência. 
print("Para calcular a potência de um número, basta colocarmos dois **, que nos operadores matemáticos do Python, significa potência.")
print("Nesta atividade, será dois elevado á 10.")

CálculoDaPotência = (2**10)
print("O cálculo da potênciação é igual á {}!".format(CálculoDaPotência))

print("_*_" *30)

#F - O resultado absoluto da diferença entre 54 e 57.
print("Para acharmos o valor absoluto, usaremos uma função denominada abs(). Essa função nos retornará o valor absoluto da operação.")
print("Na diferença entre 54 e 57, irá dar -3, mas usando a função abs(), irá dar 3, o valor absoluto.")

CálculoDoValorAbsoluto = abs(54-57)
print("A diferença entre 54 e 57 é igual a -3. Porém, no seu valor absoluto, é igual á {}!".format(CálculoDoValorAbsoluto))

print("_*_" *30)

#G - O menor valor entre 34, 29 e 31.
print("Para encontrarmos o menor valor, usamos uma função chamada min(). Está função nós retorna o menor valor em um apanhado de opções.")
print("Usaremos a função min() para os seguintes números: 34, 29 e 31!")

EncontrandoOMenorValor = min(34, 29, 31)
print("O menor valor entre 34, 29 e 31 é {}!".format(EncontrandoOMenorValor))

print("_*_" *30)