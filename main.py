from utils.mercado import menu
from time import sleep
from typing import Dict, List
from models.produto import Produto


def main() -> None:
    try:
        menu()
    except ValueError:
        print('Opção Inválida, por favor digite uma das opções listdas no menu.')
        sleep(2)
        menu()


if __name__ == '__main__':
    main()
