#Lucas Duarte Bareli Ds-13

#Exercícios 05/11 ORIENTAÇÃO A OBJETOS

#Exercício-1

"""class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (base * altura)/2

base = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do triângulo: "))
triangulo = Triangulo(base, altura)

print(f"A area do seu triângulo é: {triangulo.area()}")"""

#Exercício-2

"""class Carro:
    def __init__(self, modelo, ano, quilometragem):
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem
        
    def detalhes(self):
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Quilometragem: {self.quilometragem} km")

modelo = input("Digite o modelo do carro: ")
ano = int(input("Digite o ano do carro: "))
quilometragem = int(input("Digite a quilometragem do carro: "))

carro = Carro(modelo, ano, quilometragem)
carro.detalhes() """

#Exercício-3

"""class Animal:
    def __init__(self, especie, som):
        self.especie = especie
        self.som = som

    def emitir_som(self):
        print(f"O {self.especie} faz: {self.som}")

especie = input("Digite a espécie do animal: ")
som = input("Digite o som que o animal faz: ")

animal = Animal(especie, som)
animal.emitir_som()"""

#Exercício-4

"""class Aluno:
    def __init__(self, nome, bimestre):
        self.nome = nome
        self.bimestre = bimestre
        self.notas = []

    def media(self):
        soma_notas = 0
        for i in range(self.bimestre):
            nota = float(input(f"Digite sua nota no {i + 1}° bimestre: "))
            self.notas.append(nota)
            soma_notas += nota
        return soma_notas / self.bimestre

nome = input("Digite seu nome: ")
bimestre = int(input("Digite quantos bimestres: "))

aluno = Aluno(nome, bimestre)

print(f"Sua média durante os {bimestre} bimestres foi de: {aluno.media():.2f}")"""

#Exercício-5

"""class TransacaoBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.historico_transacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico_transacoes.append(f"Depósito de R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso")
        else:
            print("Valor de depósito inválido. O valor deve ser maior que zero")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                self.historico_transacoes.append(f"Saque de R${valor:.2f}")
                print(f"Saque de R${valor:.2f} realizado com sucesso")
            else:
                print("Saldo insuficiente para o saque")
        else:
            print("Valor de saque inválido. O valor deve ser maior que zero")

    def extrato(self):
        print("\nExtrato Bancário: ")
        if self.historico_transacoes:
            for transacao in self.historico_transacoes:
                print(transacao)
        else:
            print("Nenhuma transação realizada")
        print(f"Saldo atual: R${self.saldo:.2f}")

def menu():
    print("\nMenu:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver Extrato")
    print("4. Sair")
    opcao = input("Escolha uma opção (1/2/3/4): ")
    return opcao

def banco():
    conta = TransacaoBancaria()

    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input("Digite o valor do depósito: R$"))
            conta.depositar(valor)

        elif opcao == '2':
            valor = float(input("Digite o valor do saque: R$"))
            conta.sacar(valor)

        elif opcao == '3':
            conta.extrato()

        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente")

banco()"""

#Exercício-6

"""class GerenciadorFinanceiro:
    class Conta:
        def __init__(self, saldo, tipo_conta):
            self.saldo = saldo
            self.historico_transacoes = []
            self.tipo_conta = tipo_conta

        def adicionar_transacao(self, tipo, valor):
            self.historico_transacoes.append((tipo, valor))

    def __init__(self):
        self.contas = {}

    def criar_conta(self, id_conta, tipo_conta):
        if id_conta in self.contas:
            print(f"Conta com ID {id_conta} já existe")
        else:
            if tipo_conta not in ['Poupança', 'Corrente']:
                print(f"Tipo de conta {tipo_conta} inválido")
            else:
                nova_conta = self.Conta(saldo=0.0, tipo_conta=tipo_conta)
                self.contas[id_conta] = nova_conta
                print(f"Conta {id_conta} do tipo {tipo_conta} criada com sucesso")

    def depositar(self, id_conta, valor):
        if id_conta not in self.contas:
            print(f"Conta {id_conta} não encontrada")
        elif valor <= 0:
            print("Valor de depósito deve ser positivo")
        else:
            conta = self.contas[id_conta]
            conta.saldo += valor
            conta.adicionar_transacao('Depósito', valor)
            print(f"Depósito de R${valor:.2f} realizado na conta {id_conta}. Saldo atual: R${conta.saldo:.2f}")

    def sacar(self, id_conta, valor):
        if id_conta not in self.contas:
            print(f"Conta {id_conta} não encontrada")
        elif valor <= 0:
            print("Valor de saque deve ser positivo")
        else:
            conta = self.contas[id_conta]
            if valor > conta.saldo:
                print(f"Saldo insuficiente na conta {id_conta} para o saque de R${valor:.2f}")
            else:
                conta.saldo -= valor
                conta.adicionar_transacao('Saque', valor)
                print(f"Saque de R${valor:.2f} realizado na conta {id_conta}. Saldo atual: R${conta.saldo:.2f}")

    def transferir(self, id_origem, id_destino, valor):
        if id_origem not in self.contas:
            print(f"Conta de origem {id_origem} não encontrada")
        elif id_destino not in self.contas:
            print(f"Conta de destino {id_destino} não encontrada")
        elif valor <= 0:
            print("Valor de transferência deve ser positivo")
        else:
            conta_origem = self.contas[id_origem]
            conta_destino = self.contas[id_destino]

            if valor > conta_origem.saldo:
                print(f"Saldo insuficiente na conta {id_origem} para a transferência de R${valor:.2f}")
            else:
                conta_origem.saldo -= valor
                conta_destino.saldo += valor
                conta_origem.adicionar_transacao('Transferência para ' + id_destino, valor)
                conta_destino.adicionar_transacao('Transferência de ' + id_origem, valor)
                print(f"Transferência de R${valor:.2f} realizada de {id_origem} para {id_destino}")

    def consultar_extrato(self, id_conta):
        if id_conta not in self.contas:
            print(f"Conta {id_conta} não encontrada")
        else:
            conta = self.contas[id_conta]
            print(f"\nExtrato da conta {id_conta}:")
            print(f"Tipo de conta: {conta.tipo_conta}")
            print(f"Saldo: R${conta.saldo:.2f}")
            print("Histórico de Transações: ")
            for transacao in conta.historico_transacoes:
                tipo, valor = transacao
                print(f"- {tipo}: R${valor:.2f}")

    def calcular_juros(self, id_conta, taxa_juros=0.02):
        if id_conta not in self.contas:
            print(f"Conta {id_conta} não encontrada")
        else:
            conta = self.contas[id_conta]
            if conta.tipo_conta == 'Poupança':
                juros = conta.saldo * taxa_juros
                conta.saldo += juros
                conta.adicionar_transacao('Juros', juros)
                print(f"Juros de R${juros:.2f} aplicados na conta {id_conta}. Novo saldo: R${conta.saldo:.2f}")
            else:
                print(f"A conta {id_conta} não é do tipo Poupança, portanto, não há juros a serem aplicados")

def main():
    gerenciador = GerenciadorFinanceiro()

    while True:
        print("\n*** Menu ***")
        print("1. Criar conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Transferir")
        print("5. Consultar extrato")
        print("6. Calcular juros (apenas para Poupança)")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            id_conta = input("Digite o ID da conta: ")
            tipo_conta = input("Digite o tipo da conta (Poupança ou Corrente): ")
            gerenciador.criar_conta(id_conta, tipo_conta)

        elif escolha == "2":
            id_conta = input("Digite o ID da conta para depósito: ")
            valor = float(input("Digite o valor a ser depositado: R$"))
            gerenciador.depositar(id_conta, valor)

        elif escolha == "3":
            id_conta = input("Digite o ID da conta para saque: ")
            valor = float(input("Digite o valor a ser sacado: R$"))
            gerenciador.sacar(id_conta, valor)

        elif escolha == "4":
            id_origem = input("Digite o ID da conta de origem: ")
            id_destino = input("Digite o ID da conta de destino: ")
            valor = float(input("Digite o valor a ser transferido: R$"))
            gerenciador.transferir(id_origem, id_destino, valor)

        elif escolha == "5":
            id_conta = input("Digite o ID da conta para consultar o extrato: ")
            gerenciador.consultar_extrato(id_conta)

        elif escolha == "6":
            id_conta = input("Digite o ID da conta para calcular os juros: ")
            gerenciador.calcular_juros(id_conta)

        elif escolha == "7":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente")

if __name__ == "__main__":
    main()"""