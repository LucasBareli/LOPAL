#Ex Nome

"""nome = input("Digite o seu nome: ")

print(f"Olá,{nome}!")"""

# Ex Ano de nascimento

"""nascimento = int(input("Digite o ano do seu nascimento: "))
idade = 2024 - nascimento

if idade < 0 :
    print("Você não nasceu ainda kkk")
else:
    print(f"Você tem {idade} anos.")"""

# Ex Temperatura

"""temperatura = float(input("Digite quantos graus celsius está: "))

if temperatura < 15:
    print("Está muito frio!")
elif temperatura >= 15 and temperatura <= 30 :
    print("Temperatura agradável.")
else:
    print("Está muito quente!")"""

# Ex Problemas Iterativos

"""numeros = [2, 4, 6, 8, 10]

for numero in numeros:
    print(f'O número é: {numero}')"""

# Ex sem range

"""numero = int(input("Digite um número: "))
if numero >= 0: 
    while numero >= 1:
        print(numero)
        numero -= 1
else:
    print("Número positivo apenas")"""

# Ex notas dos alunos

"""aprovados = 0

qtde_alunos = int(input("Digite quantos alunos há na sala: "))

for aluno in range(qtde_alunos): # Cria uma repetição para perguntar dados de todos alunos
    nome = input(f"Digite o nome do {aluno + 1}° aluno: ") # Pergunta nome individualmente
    nota_1 = float(input(f"Digite a primeira nota do {nome}: ")) # Pergunta a primeira nota
    nota_2 = float(input(f"Digite a segunda nota do {nome}: ")) # Pergunta a segunda nota
    nota_3 = float(input(f"Digite a terceira nota do {nome}: ")) # Pergunta a terceira nota
    media = (nota_1 + nota_2 + nota_3) / 3
    if media >= 7 : # Verifica os aprovados
        aprovados +=1
        print(f"O aluno {nome} com a média {media} foi aprovado\n")
    else: #Verifica os reprovados
        print(f"O aluno {nome} com a média {media} foi reprovado\n")

print(f"Você teve {aprovados} alunos aprovados\n")

reprovados = qtde_alunos - aprovados

print(f"Você teve {reprovados} alunos reprovados")"""

# Ex Manipulação de Arquivo

with open("prova.txt", "w",encoding='utf-8') as arquivo:
    arquivo.write("Me da 100 Marcia ;;")

with open('prova.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

print(conteudo)