#AULA DE FOR

"""frutas = ["maça","banana","laranja"]
for fruta in frutas:
    print(fruta)"""

"""mensagem = "Helow world"
for caractere in mensagem:
    print(caractere)"""

"""cores = ("vermelho", "verde", "azul", "amarelo")
for cor in cores:
    print(f"Cor: {cor}")"""

"""pessoa = {
    "nome":"Ana",
    "idade":30,
    "profissao":"engenheira"
}
for chave, valor in pessoa.items():
    print(f"{chave}:{valor}")"""

"""animais = {"gato","cachorro","elefante",'girafa'}
for animal in animais:
    print("Animal:",animal)"""

"""for i in range(0,11,2):
    print(i)"""

"""nome_arquivo = "T:/1DS_TB13/LOPAL/LOPAL-Aula6-EstRepetição-Arquivo.txt"
with open(nome_arquivo,"r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())"""

"""for i in range(0,11,2):
    print(i)"""

"""cores = ["vermelho", "azul", "verde", "amarelo"]
for cor in cores:
    print(f"Cor: {cor}")"""

"""resultado = 0
for i in range(1,101):
    resultado += i
print(resultado)"""

"""numero = int(input("Digite um número:"))

for i in range(0,11):
    print(f"{numero} X {i} = {numero*i}")"""

"""qtde_lista = int(input("Digite até onde a lista vai : "))
lista = []
for i in range(1, qtde_lista+1):
    n = int(input(f"Digite o {i} item da lista : "))
    lista.append(n)
media = sum(lista) / qtde_lista
print(f"Sua média é {media}")"""