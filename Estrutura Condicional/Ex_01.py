#AULA DE IF/ELSE

"""idade = int(input("Digite sua idade : "))
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")"""

"""nota = float(input("Digite sua nota : "))

if nota <0 or nota >10:
    print("Nota invalida")
elif nota >=9:
    print("Nota excelente")
elif nota >=7:
    print("Nota boa")
elif nota >=5:
    print("Nota Média")
else:
    print("Nota insuficiente")"""

#Marcia-Versão

"""if nota <0 or nota >10:
    print("Nota invalida")
else:
    if nota >=9 and nota<=10:
        print("Nota excelente")
    elif nota >=7 and nota <9:
        print("Nota boa")
    elif nota >=5 and nota <9:
        print("Nota Média")
    else:
        print("Nota insuficiente")"""

"""numero = int(input("Digite um número : "))
if numero %2 == 0:
    print("Par")
else:
    print("Impar")
if numero%3 == 0:
    print("Multiplo por 3")
if numero % 5 == 0:
    print("Multiplo por 5")"""

"""idade = int(input("Digite sua idade : "))
if idade >= 60:
    print("Idoso")

elif idade <60 and idade >=18:
    print("Adulto")
elif idade <18 and idade >=13:
    print("Adolescente")
elif idade <13 and idade >=2:
    print("Criança")
else:
    print("Bebe")"""

"""temperatura = int(input("Temperatura graus celsius(1) ou fahrenheit(2) : "))
graus = float(input("Digite os graus: "))

if temperatura== 1:
        conversao = (graus * 1.8) + 32
        print(f"O valor da conversão é {conversao} celsius")

elif temperatura== 2:
        conversao = (graus -32) / 1.8
        print(f"O valor da conversão é {conversao} fahrenheit")"""

"""comprimento_1 = float(input("Digite o primeiro comprimento : "))
comprimento_2 = float(input("Digite o segundo comprimento : "))
comprimento_3 = float(input("Digite o terceiro comprimento : "))

if comprimento_1 + comprimento_2 > comprimento_3 or comprimento_1 + comprimento_3 > comprimento_2 or comprimento_2 + comprimento_3 > comprimento_1:
    print("Você possuí um triângulo")

    if comprimento_1 == comprimento_2 == comprimento_3:
        print("Equilátero")
    elif comprimento_1 == comprimento_2 or comprimento_1 == comprimento_3:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Você não possui um triângulo")"""

"""idade = int(input("Digite sua idade : "))
renda_mensal = float(input("Digite sua renda mensal : "))

if idade >= 18 and renda_mensal > 1500:
    print("Você pode pedir empréstimo")
elif idade <=18 and renda_mensal > 1000:
    print("Você pode pedir empréstimo")
else:
    print("Você não pode pedir empréstimo")"""

