#AULA DE FUNÇÃO

"""def mensagem():
    print("Bem vindo")

mensagem()"""

"""def soma(a,b):
    resultado = a + b
    print(f"O resultado da soma é {resultado}")
    return resultado

valor = soma(5,3)
print(f"Valor retornado:{valor}")"""

#Exercícios

"""def saudacao():
    print("Olá, seja bem-vindo!")

saudacao()"""


"""def dobro():
    a = float(input("Digite um número : "))
    multi = a * 2
    print(f"O dobro do seu número é {multi}")
    return multi

valor = dobro()
print(f"Dobro do seu número é {valor}")"""


"""def dobro(b):
    multi = b * 2
    print(f"O dobro do seu número é {multi}")
    return multi


a = float(input("Digite um número : "))
valor = dobro(a)
print(f"Dobro do seu número é {valor}")"""

"""def maior(n1,n2):
    if n1 > n2:
        #print(f"{n1} é maior que {n2}")
        maior  = n1
    else:
        #print(f"O {n2} é maior que {n1}")
        maior = n2
    return maior

numero_1 = int(input("Digite um número : "))
numero_2 = int(input("Digite um número : "))

x = maior(numero_1,numero_2)

print(f" O maior número entre {numero_1} e {numero_2} é \n{x}.")"""

"""def media(numeros):
    soma = 0
    for i in numeros:
        soma += i
    return soma / len(numeros)

numeros = [10,20,30]

print(media(numeros))"""

"""def calcular_fatorial(numero):
    fatorial = 1
    i = 1
    while i <= numero:
        fatorial *= i
        i += 1
    return fatorial

numero = int(input("Digite um número: "))
resultado = calcular_fatorial(numero)
print(f"Fatorial de {numero} é {resultado}")"""
