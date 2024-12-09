#Aula de Orientação a Objetos

#Exemplo 1

"""class Cachorro:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        return ("AUAU")

    def idade_humana(self):
        return self.idade * 7

meu_cachorro = Cachorro("Rex",3)

meu_cachorro.latir()

print(f"O nome do  meu cachorro é {meu_cachorro.nome}, ele tem {meu_cachorro.idade} anos e {meu_cachorro.idade_humana()} anos humanos. Ele faz {meu_cachorro.latir()}")"""

#Exemplo 2

"""class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tinta = 100
    def escrever(self):
        if self.tinta > 0:
            print(f"Escrevendo com a cante {self.cor}")
            self.tinta -= 10
        else:
            print("Caneta cabo fi")
    def recarregar(self):
        print("Recarregando a caneta...")
        self.tinta = 100

    def verificar_tinta(self):
        return f"Tinta restante:{self.tinta}%\n"

minha_caneta = Caneta("azul")
for i in range(0,9):
    minha_caneta.escrever()
    print(minha_caneta.verificar_tinta())

minha_caneta.recarregar()"""

#Exemplo 3

"""class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def nome(self):
        return self.nome()
    def latir(self):
        print("AU AU!")

class CachorroPolicial(Cachorro):
    def procurar_drogas(self):
        print("Procurando intorpecentes...")

def fazer_latir(nome_cachorro):
    nome_cachorro.latir()

rex = CachorroPolicial("Rex", 5)
rex.latir()
rex.procurar_drogas()

fazer_latir(rex)"""

#Exemplo 4

"""class Circulo:
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return PI * self.raio ** 2

raio = float(input("Digite o raio do círculo: "))
PI = 3.1416
circulo = Circulo(raio)

print(f"O valor da área desse círculo é: {circulo.area()}")"""

#Exemplo 5

"""class Retangulo:
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura
    def perimetro(self):
        return 2 * (largura + altura)
        
altura = float(input("Digite a altura do retângulo: "))
largura = float(input("Digite a largura do retângulo: "))
retangulo = Retangulo(altura, largura)

print(f"O perimetro do seu retângulo é: {retangulo.perimetro()}")"""

#Exemplo 6

"""class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"{self.nome}\n{self.idade} anos")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
pessoa = Pessoa(nome, idade)
pessoa.apresentar() """

#Exemplo 7

"""class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def resumo(self):
        print(f"Titulo: {self.titulo}\nAutor: {self.autor}")

titulo = input("Digite o titulo do livro: ")
autor = input("Digite o autor do livro: ")
livro = Livro(titulo,autor)
livro.resumo()"""