import main


def alterarproduto():
    codigo_produto = int(input("Código: "))
    if codigo_produto in main.cod_produto:
        print("Descrição: ", main.desc_produto, "Quantidade: ", main.qtd_produto)
        main.desc_produto[main.cod_produto.index(codigo_produto)] = input("Nova descrição: ").upper()
        main.qtd_produto[main.cod_produto.index(codigo_produto)] = int(input("Nova quantidade: "))
        print("Descrição alterada para: ", main.desc_produto, "Quantidade alterada para: ", main.qtd_produto)
    else:
        print("\033[31mProduto não cadastrado.\033[m")
