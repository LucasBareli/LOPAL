#Lucas Duarte Bareli Ds-13

#Exercícios 22/10 - Função

#Exercício-1

"""def imc(peso,altura,imc):
    imc = peso / (altura ** 2)

    return imc

peso = float(input("Digite seu peso : "))
altura = float(input("Digite sua altura : "))
imc = imc(peso,altura,imc)
print(f"Seu IMC é : {imc:.2f}")"""

#Exercício-2

"""def maior_n(n):
    maior = 0
    for i in range(n):
        numero = int(input(f"Digite o {i+1}º número: "))
        if maior == 0 or numero > maior:
            maior = numero
    return maior

n = int(input("Quantos números você deseja digitar? "))
resultado = maior_n(n)

print(f"O maior número digitado é: {resultado}")"""

#Exercício-3

"""def par_ou_impar(numero):
    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")

numero = int(input("Digite um número : "))
par_ou_impar(numero)"""

#Exercício-4

"""def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    for letras in palavra:
        if letras in vogais:
            contador += 1
    return contador

palavra = str(input("Digite uma palavra: "))

print(f"A palavra tem {contar_vogais(palavra)} vogais")"""

#Exercício-5

"""def contagem_regressiva(numero):
    for i in range(numero, 0 - 1, -1):
        print(i)

numero = int(input("Digite um número : "))
contagem_regressiva(numero)"""
