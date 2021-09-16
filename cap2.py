#1. Faça X = 0.0 e Y = 18. Verifique o tipo de dado que o Python atribuiu
#a cada um. Faça Z = X + Y e verifique o resultado calculado e
#armazenado em Z. Verifique com qual tipo de dado foi criado o objeto
#Z.


x = 0.0
y = 18

print(type(x))
print(type(y))

z = x + y
print(z)
print(type(z))


#2. Atribua um valor qualquer a um objeto a (minúsculo). Utilize o
#comando type ou o comando print com o objeto A (maiúsculo). Relate
#o que aconteceu.


a = 2

A = 2 # so pra nao ficar corrompido

print(type(A))
# A its not defined.


#3. No IDLE, faça A = “Questão 3”, B = 25 e C = 3.9. Utilize o comando
#type para verificar qual é o tipo de dado dos objetos A, B e C.


a = "Questão 3"
b = 25
c = 3.9

print(type(a))
print(type(b))
print(type(c))


#4. Reproduza em um programa todos os casos de operações aritméticas
#do Quadro 2.1, para A = 14 e B = 5, e compare os valores obtidos por
#você com os valores esperados constantes do quadro.


a = 14
b = 5

soma = a + b
sub = a - b
multi = a * b
div = a / b
divInt = a // b
modulo = a % b
unario = - a
potencia = a ** b

print(soma)
print(sub)
print(multi)
print(div)
print(divInt)
print(modulo)
print(unario)
print(potencia)


#5. Escreva a sequência de comandos necessária para o cálculo da área de
#um triângulo de base 9 e altura 6.


base = 9
altura = 6

area = (base * altura)/2

print("A área é {0}".format(area))


#6. Refaça o exercício 5 alterando-o de modo que a base e a altura do
#triângulo sejam lidas do teclado. Considere-as números reais.


base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

area = (base*altura)/2

print("A área do trinângulo é ",area)


#7. Escreva a sequência de comandos para calcular o salário bruto de um
#profissional que ganha por hora, sabendo que ele ganha R$ 14,25/h e
#trabalhou 163 horas normais e 20 horas extras (pagam o dobro)


salarioH = 14.25
hora = 163
horaEx = 20

salarioBruto = (salarioH * hora) + ((salarioH * 2)* horaEx)
print(salarioBruto)


#8. Escreva em Python as seguintes expressões aritméticas para as
#fórmulas a seguir e teste as quatro primeiras para os valores A = 4, B
#= 5, C = 1 e a última para os valores x1 = 1, y1 = 1, x2 = 4 e y2 = 5.

#8.a    R = (A+B)/2

#8.b    X = -B+ RAÍZ QUADRADA(B**2  - 4*A*C)/(2*A)

#8.c    R = (3A + 2B)/(A+B)

#8.d    Z= 7.6*A - B**1.7

#8.e    D=RAÍZ QUADRADA ((X1-X2)**2 + (Y1-Y2)**2)

import math

a = 4
b = 5
c = 1

x1 = 1
y1= 1
x2 = 4
y2 = 5 

#8.a
r = (a+b)/2
#8.b
x = (-b + math.sqrt( (b**2) - (4*a*c))) / (2 * a)
#8.c
r2 = ((3*a) + (2*b))/ (a+b)
#8.d
z = (7.6 * a) - (b**1.7)
#8.e
d = math.sqrt( ( ( x1 - x2)**2 ) + ( (y1 - y2)**2 ) )

print("8.A = ",r)
print("8.B = ",x)
print("8.C = ",r2)
print("8.D = ",z)
print("8.E = ",d)


#9. Escreva um programa que leia do teclado as coordenadas (x1, y1) do
#ponto 1 e (x2, y2) do ponto 2. Utilizando a expressão do item 8.e,
#determine a distância entre esses dois pontos e exiba-a na tela com três
#casas decimais.


import math

x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y1: "))

d = math.sqrt( ( ( x1 - x2)**2 ) + ( (y1 - y2)**2 ) )

print("Distancia entre esses pontos é de ",round(d,3))

#10.Um vendedor ambulante vendeu os produtos indicados na tabela a
#seguir. Informe quanto ele faturou com cada produto e quanto ele
#faturou no total

# Produto                Quantidade vendida         Valor unitário R$
# Boneco   Malandrinho       17                         18,50
# Spinner Pequeno            36                         12,00
# Cubo Mágico                 7                         5,90




total = 0.0
nomeProds = [str(input("Digite o nome do Produto: "))]
qtdVendidas = [float(input("Digite a quantidade vendida: "))]
valUnis = [float(input("Digite o Preço unitário: "))]

loop = str(input("Deseja cadastrar mais produto? [Y][N]"))

while (loop == "y" or loop == "Y") : 
    nomeProds.append(str(input("Digite o nome do Produto: ")))
    qtdVendidas.append(float(input("Digite a quantidade vendida: ")))
    valUnis.append(float(input("Digite o Preço unitário: ")))
    loop = str(input("Deseja cadastrar mais produto? [Y][N]"))

for i in range(len(qtdVendidas)):
    total = total + qtdVendidas[i] * valUnis[i]
    print(qtdVendidas[i] * valUnis[i])

print(total)
