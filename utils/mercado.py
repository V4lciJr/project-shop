from time import sleep
from typing import List, Dict
from models.produto import Produto
from utils.helper import format_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []  # dicionario para implementacao do carrinho de compras


def menu() -> None:
    print('=============================================')
    print('============== BEM VINDO(A) =================')
    print('============== Project Shop =================')
    print('=============================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar Produto(s)')
    print('2 - Listar Produto(s)')
    print('3 - Adicionar produto(s) ao carrinho')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair do Sistema')

    opcao: int = int(input('\nOpçao: '))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        add_carrinho()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Agradecemos a sua visita!!\nVolte Sempre !')
        sleep(2)
        exit(0)
    else:
        print('Opção Inválida')
        sleep(1)
        menu()


def cadastrar_produto():
    print('Cadastro de Produto(s)')
    print('======================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)
    print(f'O produto {produto.nome} foi cadastrado com sucesso!!')

    resposta = input('Deseja cadastrar mais algum produto ? [y/n] ')
    if resposta.lower() == 'y':
        cadastrar_produto()
    sleep(2)
    menu()


def listar_produto() -> None:
    if len(produtos) > 0:
        print('Lista de Produtos')
        print('=================')
        for produto in produtos:
            print(produto)
            print('*****************')
            sleep(0.5)
    else:
        print('Ainda não existem produtos na cadastrados.')
    sleep(1)
    menu()


def add_carrinho() -> None:
    if len(produtos) > 0:
        print('**************************************************************')
        print('****************** Produtos disponíveis **********************')

        for p in produtos:
            print(f'{p}\n')

        print('Informe o código do produto, que deseja adicionar ao carrinho:')
        codigo: int = int(input('Digite o código do produto desejado: '))

        produto: Produto = get_produto_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                contem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:                      # caso o produto ja esteja no carrinho
                        item[produto] = quant + 1  # so incrementa a quantidade do produto
                        print(f'Seu carrinho possui {quant + 1} unidade(s) do produto {produto.nome}.')
                        contem_no_carrinho = True
                        sleep(1)

                if not contem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionao ao carrinho.')

            else:
                p = {produto: 1}
                carrinho.append(p)
                print(f'O produto {produto.nome} foi adidionado ao carrinho.')
        else:
            print(f'O produto de código {codigo} não foi encontrado.')

        resposta = input('Deseja continuar adicionando produtos ao seu carrinho? [y/n] ')
        if resposta.lower() == 'y':
            add_carrinho()
    else:
        print('Não existem produtos no cadastro.')
    sleep(1)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Seu carrinho de compras atual: ')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('***********************')
    else:
        print('Seu carrinhos de compras está vazio :(')

    sleep(4)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Seu carrinho de compras:')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('*******************')
                sleep(0.5)
        print(f'Sua fatura atual é : {format_float_str_moeda(valor_total)}')
        print('Volte Sempre !!')
        carrinho.clear()
    else:
        print('Ainda não existem produtos no seu carrinho.')

    sleep(2)
    menu()


def get_produto_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p