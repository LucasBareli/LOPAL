#Desafio 1

"""def conta_letras(palavra):
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    palavraChar = {}

    for caracter in palavra.lower():
        if caracter in alfabeto:
            if caracter in palavraChar:
                palavraChar[caracter] += 1
            else:
                palavraChar[caracter] = 1

    print(f"{palavraChar}")


palavra = input("Digite alguma palavra para fazer sua contagem: ")
conta_letras(palavra)"""

#Desafio 2

"""def ordena_lista(lista):
    n = len(lista)
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

numeros = []
quantidade = int(input("Quantos números você deseja inserir? "))

for _ in range(quantidade):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

lista_ordenada = ordena_lista(numeros)

print("Ordem crescente:", lista_ordenada)"""

#Desafio 3

"""def contagem_regressiva(n):
    if n > 0:
        print(n)
        contagem_regressiva(n - 1)
    else:
        print("Fim")

numero = int(input("Digite um número inteiro para a contagem regressiva: "))
contagem_regressiva(numero)"""