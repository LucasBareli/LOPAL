#Lucas Duarte Bareli Ds-13

#Exercícios 17/09 IF/ELSE

#Exercício-1

"""ano = int(input("Digite o ano desejado :"))
if ano%4 == 0:
    print(f"O ano {ano} é bissexto")
elif ano%400 == 0 and ano%100 ==0:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")"""

#Exercício-2

"""peso = float(input("Digite seu peso : "))
altura = float(input("Digite sua altura : "))
imc = peso/(altura**2)

if imc >0 and imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print("Obesidade")
elif imc >= 35 and imc <= 39.9:
    print("Obesidade mórbida")
elif imc >= 40:
    print("Obesidade mórbida grave")"""

#Exercício-3

"""qt_produtos = int(input("Digite a quantidade de produtos comprados : "))
valor_unt = float(input("Digite o valor de cada unidade : "))

if qt_produtos >=100:
    valor_inicial = qt_produtos*valor_unt
    desconto_unt = (valor_inicial * 10/100) / qt_produtos
    desconto = valor_inicial * 10/100
    valor_final = (qt_produtos*valor_unt) - desconto
else:
    desconto = (qt_produtos * valor_unt) * 5/100
    valor_final = (qt_produtos * valor_unt) - desconto
    print(valor_final)

print(f"Você solicitou {qt_produtos} produtos, com o valor inicial de {valor_inicial}.")
print(f"Com isso, você obteve um desconto de {desconto_unt} por produto, totalizando seu valor final com desconto de {valor_final}")"""

#Exercício-4

"""idade = int(input("Digite sua idade :"))
if idade >= 18:
    print("Você é obrigado a votar")
elif idade >=16 and idade<18:
    print("Seu voto é facultativo")
else:
    print("Você não pode votar")"""

#Exercício-5

"""pessoa_1 = int(input("Digite sua idade :"))
pessoa_2 = int(input("Digite sua idade :"))
pessoa_3 = int(input("Digite sua idade :"))

maior_idade = max(pessoa_1, pessoa_2, pessoa_3)
menor_idade = min(pessoa_1, pessoa_2, pessoa_3)

print(f"A maior idade entre as pessoas é: {maior_idade}")
print(f"A menor idade entre as pessoas é: {menor_idade}")"""

#Exercício-6

"""horas = int(input("Digite a hora desejada : "))
minutos = int(input("Digite o minuto desejado : "))
segundos = int(input("Digite o segundo desejado : "))

if horas <= 24 and horas >= 0 and minutos >=0 and minutos<= 60 and segundos >=0 and segundos <= 60:
    print("Hora está de acordo")
else:
    print("Hora invalida")"""

#Exercício-7

"""nota = float(input("Digite sua nota : "))

if nota >= 9 and nota <=10:
    print("Nota A")
elif nota >= 7 and nota<9:
    print("Nota B")
elif nota >= 5 and nota < 7:
    print("Nota C")
elif nota >= 3 and nota < 5:
    print("Nota D")
elif nota >=0 and nota <3:
    print("Nota E")"""

#Exercício-8

"""lado_1 = float(input("Digite o primeiro comprimento : "))
lado_2 = float(input("Digite o segundo comprimento : "))
lado_3 = float(input("Digite o terceiro comprimento : "))
lado_4 = float(input("Digite o quarto comprimento : "))

if lado_1 == lado_2 == lado_3 == lado_4:
    print("Você possui um quadrado")
elif lado_1 == lado_2 != lado_3 == lado_4 or lado_1 == lado_3 != lado_2 == lado_4 or lado_1 == lado_4 != lado_2 == lado_3:
    print("Você possuí um retângulo")
else:
    print("Você não possui nenhum dos dois")"""

#Exercício-9

"""primeiro_numero = float(input("DIgite o primeiro número : "))
segundo_numero = float(input("DIgite o segundo número : "))
operacao = str(input("Digite a operação desejada : (+, -, * ou /) : "))

if operacao == "+":
    resultado = primeiro_numero + segundo_numero
    print(f"Resultado da soma é {resultado}")
elif operacao == "-":
    resultado = primeiro_numero - segundo_numero
    print(f"Resultado da subtração é {resultado}")
elif operacao == "*":
    resultado = primeiro_numero * segundo_numero
    print(f"Resultado da multiplicação é {resultado}")
elif operacao == "/":
    resultado = primeiro_numero / segundo_numero
    print(f"Resultado da divisão é {resultado}")"""

#Exercício-10

"""nota_1 = float(input("Digite a primeira nota : "))
nota_2 = float(input("Digite a segunda nota : "))
nota_3 = float(input("Digite a terceira nota : "))
descarte = min(nota_1, nota_2, nota_3)
media = (nota_1 + nota_2 + nota_3 - descarte) / 3

print(f"A média calculada de sua média sem a sua menor nota é de : {media}")"""

#Desafio

"""import random
computador = random.randint(0, 11)
jogador = int(input("Advinhe o número que eu pensei: "))

if jogador == computador:
    print("Você acertou")
elif jogador > computador:
    print(f"O valor é abaixo de {jogador}")
    jogador = int(input("Segunda tentativa : "))
    if jogador == computador:
        print("Você acertou")
    else:
        print(f"Você errou \n o seu chute foi: {jogador}, porém o certo era: {computador}")
elif jogador < computador:
    print(f"O valor é acima de {jogador}")
    jogador = int(input("Segunda tentativa: "))
    if jogador == computador:
        print("Você acertou")
    else:
        print(f"Você errou \n o seu chute foi: {jogador}, porém o certo era: {computador}")"""
