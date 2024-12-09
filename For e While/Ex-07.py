#Aula do Lindomar

#Exercício 1

"""print("Olá mundo!")"""

#Exercício 2

"""num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
soma = num_1 + num_2

print(f"Resultado da soma é {soma}")"""

#Exercício 3

"""num = int(input("Digite um número: "))
if num % 2 == 0:
    print(f"O numero {num} é par")
else:
    print(f"O número {num} é ímpar")"""

# Exercício 4

"""num_1 = float(input("Digite o primeiro número : "))
num_2 = float(input("Digite o segundo número : "))
operacao = str(input("Você deseja +, -, / ou * :"))

if operacao == "+":
    resultado = num_1 + num_2
    print(resultado)
elif operacao == "-":
    resultado = num_1 - num_2
    print(resultado)
elif operacao == "/":
    resultado = num_1 / num_2
    print(resultado)
elif operacao == "*":
    resultado = num_1 * num_2
    print(resultado)
else:
    print("Operação inválida")"""

# Exercício 5

"""for i in range(10,0,-1):
    print(i)"""

# Exercício 6

"""numero = int(input("Digite um número : "))
fatorial = 1
i = 1
while i <= numero :
    fatorial*= i
    i +=1
print(f"O fatorial de {numero} é {fatorial}")"""

#Exercício 7

"""palavra = str(input("Digite uma palavra: "))
if palavra[::-1] == palavra:
    print(f"A palavra {palavra} é políndroma")
else:
    print(f"A palavra {palavra} não é polindroma")"""

#Exercício 8

"""numero_n = int(input("Digite até onde vai a sequência de Fibonacci : "))
primeiro_numero = 0
segundo_numero = 1

for i in range(0, numero_n + 1):
    soma = primeiro_numero + segundo_numero
    segundo_numero, primeiro_numero = soma, segundo_numero
    print(soma)"""

#Exercício 9

"""palavra = str(input("Digite uma palavra: "))
vogais = "aeiouAEIOU"
contador = 0

for letras in palavra:
    if letras in vogais:
        contador += 1

print(f"A palavra tem {contador} vogais")"""

#Exercício 10

"""numero = int(input("Digite um número : "))

for i in range(0,11):
    multiplicacao = numero * i
    print(f"{numero} X {i} = {multiplicacao}")"""