#1. Escreva um programa que apresente na tela a frase: "Meu primeiro programa!

print("Meu primeiro programa!!!")

#2. Escreva um programa que solicite ao usuário um número inteiro e ao final apresente na tela
#o número informado pelo usuário do programa

num = input("Digite um número inteiro \n")
print(num)

#3. Escreva um programa que solicite ao usuário um número inteiro e ao final apresente na tela
#o número informado da seguinte forma: "Foi informado o valor: X"

num = input("Digite um número inteiro \n")

print("Foi informado o valor: {}".format(num))

#4. Escreva um programa que solicite ao usuário dois números inteiros e ao final apresente na
#tela os dois números informados da seguinte forma: "Voce informou os numeros X e Y"


num1 = input("Digite o primeiro valor")
num2 = input("Digite o segundo valor")

print("Você informou os números {0} e {1}".format(num1,num2))


#5. Escreva um programa que solicite ao usuário um número real e ao final apresente na tela o
#número informado formatado com duas casas decimais da seguinte forma: "Voce informou
#o numero X.YY"


num1 = float(input("Digite um valor real para X: "))

print("Voce informou o numero {0} ".format(round(num1,2)))


#6. Escreva um programa que solicite ao usuário a temperatura em graus Celsius e ao final
#apresente a temperatura correspondente em graus Farenheit. F = Celsius * 1.8 + 32


grauC = float(input("Digite quantos Graus deseja converter para Farenheit: "))

f = (grauC * 1.8) + 32

print("{0}C é equivalente a {1}F".format(grauC,f))


#7. Escreva um programa que solicite ao usuário um número inteiro e um número real e ao final
#apresente na tela os dois números informados formatando com duas casas decimais
#somente o número real da seguinte forma: "Voce informou os numeros N e X.YY"


num1 = int(input("Digite um valor inteiro: "))
num2 = float(input("Digite um valor real: "))

print("O valor informado {0} e {1:.2f}".format(num1,num2))


#8. Escreva um programa que solicite ao usuário a primeira letra de seu nome e ao final
#apresente na tela a letra informada pelo usuário da seguinte forma: "Voce digitou w"


letra = str(input("Digite a primeira letra do seu nome: "))

print("Vocẽ digitou: {0}".format(letra))


#9. Escreva um programa que solicite ao usuário o nome de sua cor preferida e ao final
#apresente na tela a cor informada pelo usuário da seguinte forma: "Voce gosta da cor AAA"


cor = str(input("Digite sua cor preferida: "))

print("Sua cor favorita é {0}".format(cor))


#10. Escreva um programa que solicite ao usuário o nome de uma verdura e uma fruta de sua
#preferencia e ao final apresente na tela as informações digitadas pelo usuário da seguinte
#forma: "Voce gosta de AAAAAAA e BBBBBBB"


fruta = str(input("Digite sua fruta favorita: "))
verdura = str(input("Digite sua verdura favorita: "))

print("Você gosta da fruta: {0} e da verdura: {1} ".format(fruta,verdura))


#11. Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela o
#numero informado e na linha de baixo o dobro deste número da seguinte forma:
#Numero -> X
#Dobro deste numero -> Y


num = float(input("Digite um número real: "))
dobro = num *2
print("Número -> {0} \nDobro do número -> {1}".format(num,dobro))


#12. Reescrever o programa anterior apresentando o quadrado e o cubo do número informado


num = float(input("Digite um número real: "))
quadrado = num ** 2
cubo = num ** 3
print("Número -> {0} \nQuadrado do número -> {1} \nCubo do número ->{2}".format(num,quadrado,cubo))


#13. Escreva um programa que solicite ao usuário dois números inteiros e ao final apresente na
#tela a soma dos dois números informados da seguinte forma: "O numeros N e X somados
#correspondem a Y"


num1 = int(input("Digite o primeiro valor inteiro: "))
num2 = int(input("Digite o segundo valor inteiro: "))

soma = num1 + num2
print("O numeros {0} e {1} somados correspondem a {2}".format(num1,num2,soma))


#14. Escreva um programa que solicite ao usuário dois números reais e ao final apresente na
#tela o produto dos dois números informados da seguinte forma: "O produto dos numeros N
#e X corresponde a Y"


num1 = float(input("Digite o primeiro valor real: "))
num2 = float(input("Digite o segundo valor real: "))

multiplicacao = num1 * num2
print("O numeros {0} e {1} multiplicados correspondem a {2}".format(num1,num2,multiplicacao))


#15. Refazer o programa 14 realizando as quatro operações aritméticas básicas


num1 = float(input("Digite o primeiro valor : "))
num2 = float(input("Digite o segundo valor : "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1/num2

print(" {0} + {1} = {2} \n {0} - {1} = {3} \n {0} * {1} = {4} \n {0} / {1} = {5}".format(num1,num2,soma,subtracao,multiplicacao,divisao))


#16. Escreva um programa que solicite o valor fixo do salário de um vendedor, o total vendido
#no mês e o percentual de comissão do vendedor. Ao final apresentar o salário bruto.


salario = float(input("Digite seu salário fixo: "))
vendas = int(input("Digite o número de vendas no mês: "))
percentualComissao = float(input("Digite o percentual de comissão: "))

salarioBruto = salario + (percentualComissao * vendas)

print("O sálario bruto foi de R${0:.2f}".format(salarioBruto))
