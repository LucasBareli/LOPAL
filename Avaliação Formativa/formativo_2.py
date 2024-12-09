# Sistema Básico de Controle Financeiro - Lucas Duarte Bareli

"""def registrar_transacao(tipo, valor, descricao, categoria, mes):
    transacao = {
        "tipo": tipo,
        "valor": valor,
        "descricao": descricao,
        "categoria": categoria,
        "mes": mes
    }
    transacoes.append(transacao)

def exibir_saldo():
    return saldo

def listar_transacoes():
    if not transacoes:
        print("Nenhuma transação registrada.")
    else:
        print("\nTransações Registradas:")
        for transacao in transacoes:
            print(f"Tipo: {transacao['tipo']}, Valor: R${transacao['valor']:.2f}, Descrição: {transacao['descricao']}, Categoria: {transacao['categoria']}, Mês: {transacao['mes']}")

def listar_transacoes_por_categoria(categoria):
    transacoes_categoria = [t for t in transacoes if t["categoria"].lower() == categoria.lower()] # Para aceitar maiuscula e minuscula
    if not transacoes_categoria:
        print(f"Nenhuma transação registrada na categoria '{categoria}'.")
    else:
        print(f"\nTransações na categoria '{categoria}':")
        for transacao in transacoes_categoria:
            print(f"Tipo: {transacao['tipo']}, Valor: R${transacao['valor']:.2f}, Descrição: {transacao['descricao']}")

def relatorio_por_categoria():
    relatorio = {}
    for transacao in transacoes:
        categoria = transacao['categoria']
        if categoria not in relatorio:
            relatorio[categoria] = {'receitas': 0, 'despesas': 0}
        if transacao['tipo'] == "Receita":
            relatorio[categoria]['receitas'] += transacao['valor']
        else:
            relatorio[categoria]['despesas'] += transacao['valor']

    print("\nRelatório por Categoria:")
    for categoria, valores in relatorio.items():
        print(f"Categoria: {categoria}, Total Receitas: R${valores['receitas']:.2f}, Total Despesas: R${valores['despesas']:.2f}")

def saldo_mensal(mes):
    saldo = 0
    for transacao in transacoes:
        if transacao['mes'] == mes:
            if transacao['tipo'] == "Receita":
                saldo += transacao['valor']
            else:
                saldo -= transacao['valor']
    return saldo

saldo = 0
transacoes = []

while True:
    print("\n1. Registrar uma receita")
    print("2. Registrar uma despesa")
    print("3. Exibir saldo")
    print("4. Listar transações")
    print("5. Listar transações por categoria")
    print("6. Relatório por categoria")
    print("7. Saldo mensal")
    print("8. Sair")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        valor_receita = float(input("Digite o valor da receita: "))
        descricao_receita = input("Digite uma descrição sobre a receita: ")
        print("1. Alimentação\n2. Lazer\n3. Transporte\n4. Salário")
        categoria_receita = input("Qual categoria melhor se encaixa? ")
        mes_receita = int(input("Digite o mês da receita (1-12): "))
        registrar_transacao("Receita", valor_receita, descricao_receita, categoria_receita, mes_receita)
        saldo += valor_receita
        print("Receita registrada com sucesso!")

    elif opcao == 2:
        valor_despesa = float(input("Digite o valor da despesa: "))
        descricao_despesa = input("Digite uma descrição sobre a despesa: ")
        print("1. Alimentação\n2. Lazer\n3. Transporte\n4. Salário")
        categoria_despesa = input("Qual categoria melhor se encaixa? ")
        mes_despesa = int(input("Digite o mês da despesa (1-12): "))
        registrar_transacao("Despesa", valor_despesa, descricao_despesa, categoria_despesa, mes_despesa)
        saldo -= valor_despesa
        print("Despesa registrada com sucesso!")

    elif opcao == 3:
        print(f"O saldo atual é: R${exibir_saldo():.2f}")

    elif opcao == 4:
        listar_transacoes()

    elif opcao == 5:
        categoria = input("Digite a categoria que deseja listar: ")
        listar_transacoes_por_categoria(categoria)

    elif opcao == 6:
        relatorio_por_categoria()

    elif opcao == 7:
        mes = int(input("Digite o mês que deseja saber o saldo (1-12): "))
        print(f"O saldo total no mês {mes} é: R${saldo_mensal(mes):.2f}")

    elif opcao == 8:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida, tente novamente.")"""
