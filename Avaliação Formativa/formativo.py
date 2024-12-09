# Sistema de Controle de Estoque Simplificado

"""estoque = 0

while True:
    print("\nEscolha uma operação:")
    print("1. Adicionar")
    print("2. Vender")
    print("3. Verificar estoque")
    print("4. Sair")

    operacao = input("Digite o número da operação desejada: ")

    if operacao == '1':
        quantidade = int(input("Quantas unidades deseja adicionar? "))
        estoque += quantidade
        print(f"Estoque atualizado! Total de unidades: {estoque}")

    elif operacao == '2':
        quantidade_venda = int(input("Quantas unidades deseja vender? "))

        if quantidade_venda > estoque:
            print("Estoque insuficiente!")
        else:
            for i in range(quantidade_venda):
                estoque -= 1
            print(f"Venda realizada! Estoque atual: {estoque}")

    elif operacao == '3':
        print(f"Estoque atual: {estoque} unidades.")

    elif operacao == '4':
        print("Saindo do programa...")
        break

    else:
        print("Operação inválida! Tente novamente.")"""
