#Desafio 1

"""palavra = input("Escolha uma palavra: ").lower()
letras_adivinhadas = []
tentativas = 6

while tentativas > 0:
    print("Tentativas restantes:", tentativas)

    for letra in palavra:
        if letra in letras_adivinhadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

    palpite = input("Adivinhe uma letra: ").lower()

    if palpite in letras_adivinhadas:
        print("Você já adivinhou essa letra. Tente outra.")
        continue

    letras_adivinhadas.append(palpite)

    if palpite not in palavra:
        tentativas -= 1
        print("Letra incorreta!")

    acertou = True
    for letra in palavra:
        if letra not in letras_adivinhadas:
            acertou = False
            break

    if acertou:
        print(f"Parabéns! Você adivinhou a palavra:{palavra}")
        break
else:
    print(f"Você perdeu! A palavra era:{palavra}")"""

#Desafio 2

"""num_inicial = int(input("Número inicial de coelhos: "))
taxa_reproducao = float(input("Taxa de reprodução (em porcentagem): ")) / 100
taxa_mortalidade = float(input("Taxa de mortalidade (em porcentagem): ")) / 100
num_geracoes = int(input("Número de gerações: "))

populacao = num_inicial

for geracao in range(num_geracoes):
    novos_coelhos = populacao * taxa_reproducao
    coelhos_mortos = populacao * taxa_mortalidade

    populacao = populacao + novos_coelhos - coelhos_mortos

    print(f"Geração {geracao + 1}: {int(populacao)} coelhos")

print(f"\nPopulação final após {num_geracoes} gerações: {int(populacao)} coelhos")"""