import cadastrarproduto
import alterarproduto
import removeproduto

opcao = 0

codproduto = []
descproduto = []
qtdeproduto = []
produtos = (codproduto, descproduto, qtdeproduto)

while opcao != 7:
    print('\nMenu')
    opcao = int(input(
        "\t1. Cadastrar Produto\n\t2. Alterar Produto\n\t3. Excluir Produto\n\t4. Listar Estoque de Peça\n\t5. "
        "Comprar Produto\n\t6. Vender Produto\n\t7. Sair\n\tDigite a opção desejada: "))
    if opcao == 1:
        cadastrarproduto.cadastrarprodutos()

    elif opcao == 2:
        senha = input("Digite sua Senha: ")
        if senha == "yN1825*a":
            print("\033[32mAcesso permitido.\033[m")
            alterarproduto.alterarproduto()
        else:
            print("\033[31mSENHA INCORRETA\033[m")

    elif opcao == 3:
        senha = input("Digite sua Senha: ")
        if senha == "yN1825*a":
            print("\033[32mACESSO PERMITIDO\033[m")
            removeproduto.removerproduto()
        else:
            print("\033[31mSENHA INCORRETA\033[m")

    elif opcao == 4:
        print(sorted(produtos))

    elif opcao == 5:
        print("Comprar produto")

    elif opcao == 6:
        print("Vender produto")

    elif opcao == 7:
        print("Saindo...")
        break

    else:
        print("\033[31mOpção inválida!\033[m")