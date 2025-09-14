Sistema de gerenciamento de estoque

estoque = {}

while True:
    print("\n=== MENU ===")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Atualizar quantidade")
    print("4 - Exibir estoque")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite  o produto: ")
        quantidade = int(input("Digite a quantidade: "))
        estoque[nome] = quantidade
        print("Produto adicionado")

    elif opcao == "2":
        nome = input("Digite o produto que vai remover: ")
        if nome in estoque:
            del estoque[nome]
            print("Produto removido")
        else:
            print("Produto não encontrado")

    elif opcao == "3":
        nome = input("Digite o produto aque ira atualizar: ")
        if nome in estoque:
            quantidade = int(input("Digite a nova quantidade: "))
            estoque[nome] = quantidade
            print("Quantidade atualizada")
        else:
            print("Produto não encontrado")

    elif opcao == "4":
        if len(estoque) == 0:
            print("O estoque está vazio.")
        else:
            print("\n--- Estoque Atual ---")
            for produto in estoque:
                print(produto, ":", estoque[produto])

    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida, tente novamente!")
