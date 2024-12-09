# Revisão Lucas Duarte Bareli

# Exercicio 6

"""qtde_lista = int(input("Digite a quantidade de números: "))

for i in range(1, qtde_lista + 1):
    numeros = int(input(f"Digite o {i}º número: "))
    quadrado = numeros * numeros
    print(f"O quadrado de {numeros} é {quadrado}")"""

# Exercicio 7

"""num1_str = input("Digite o primeiro número: ")
num2_str = input("Digite o segundo número: ")

num1 = int(num1_str)
num2 = int(num2_str)

soma = num1 + num2

print(f'A soma dos números é: {soma}')"""

# Exercicio 8

"""temperatura = float(input("Digite a temperatura em graus Celsius: "))

limite_quente = float(input("Digite o limite quente (em Celsius): "))
limite_frio = float(input("Digite o limite frio (em Celsius): "))

if temperatura >= limite_quente:
    print("Está quente")
elif temperatura <= limite_frio:
    print("Está frio")
else:
    print("Está moderado")"""

# Exercicio 10

"""try:
    import numpy

    print("Ambiente configurado corretamente!")

except ImportError:
    print("Erro: A biblioteca 'numpy' não está instalada")"""

# Exercicio 11

"""with open('arquivo.txt', 'r') as arquivo:
    numeros = [float(linha.strip()) for linha in arquivo]
    media = sum(numeros) / len(numeros)

    print(f'A média dos números é: {media}')"""

# Exercicio 12

"""contador = 0

with open('palavras.txt', 'r') as arquivo:
    for linha in arquivo:
        palavras = linha.split()
        for palavra in palavras:
            if len(palavra) > 5:
                contador += 1

print(f'O número de palavras com mais de 5 caracteres é: {contador}')"""

# Exercicio 13

"""with open('tabuadas.txt', 'w') as arquivo:
    for i in range(1, 11):
        for mult in range(1, 11):
            f.write(f"{i} x {mult} = {i * mult}\n")
        f.write("\n")

print("As tabuadas de 1 a 10 foram escritas no arquivo "tabuadas.txt"")"""

# Exercicio 14

"""import csv

dados_produtos = [
    ['Produto', 'Preço'],
    ['Produto A', 45.99],
    ['Produto B', 60.00],
    ['Produto C', 30.00],
    ['Produto D', 75.50],
    ['Produto E', 20.00],
    ['Produto F', 100.00]
]

with open('produtos.csv', 'w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f)

    escritor.writerows(dados_produtos)
    
with open('produtos.csv', newline='', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        produto = linha['Produto']
        preco = float(linha['Preço'])

        if preco > 50:
            print(f'Produto: {produto}, Preço: {preco}')"""

# Exercicio 15

"""def primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))

contagem_primos = sum(primo(num) for num in numeros)

print(f'O número de números primos na lista é: {contagem_primos}')"""

# Exercicio 16

"""primeiro_num = int(input("Digite o primeiro número: "))
segundo_num = int(input("Digite o segundo número: "))

multiplicacao = primeiro_num * segundo_num

if multiplicacao > 50:
    print(f"O número {multiplicacao} é muito grande")

else:
    print(f"O número {multiplicacao} é muito pequeno")"""

# Exercicio 17

"""senha_correta = "1234"

tentativas = 3

for tentativa in range(tentativas):
    senha = input(f"Tentativa {tentativa + 1} de {tentativas}: Digite a senha de 4 dígitos: ")

    if senha == senha_correta:
        print("Senha correta! Acesso permitido.")
        break
    else:
        print("Senha incorreta. Tente novamente.")
else:
    print("Você excedeu o número de tentativas. Acesso bloqueado.")"""

# Exercicio 18

"""num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

numeros = [num1, num2, num3]
numeros.sort()

if numeros[0] + numeros[1] > numeros[2]:
    print("Verdadeiro")
else:
    print("Falso")"""

# Exercicio 19

"""alunos = {}

for i in range(5):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

maior_nota = max(alunos, default=None, key=alunos.get)

print(f"O aluno com a maior nota é {maior_nota} com a nota {alunos[maior_nota]}")"""

# Exercicio 20

"""num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))

while num_2 != 0:
    num_1, num_2 = num_2, num_1 % num_2

print(f"O MDC é {num_1}")"""

# Exercicio 21

"""n = int(input("Digite o número de termos da sequência de Fibonacci: "))

a, b = 0, 1

print("Sequência de Fibonacci até o", n, "º termo:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b"""