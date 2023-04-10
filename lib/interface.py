def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mOcorreu um ERRO no envio dos dados! Por favor, tente novamente.\033[m')
        except KeyboardInterrupt:
            print('\033[31m\nInfelizmente, sem essa informação a conversão não poderá ser realizada.\033[m')
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mOcorreu um ERRO no envio dos dados! Por favor, tente novamente.\033[m')
        except KeyboardInterrupt:
            print('\033[31m\nInfelizmente, sem essa informação a conversão não poderá ser realizada.\033[m')
        else:
            return n


def linha(tam=40):
    print('-' * tam)


def cabecalho(txt):
    linha()
    print(f'{txt}'.center(40))
    linha()


def menu(titulo):
    cabecalho(titulo)
    print(f'\033[32m1\033[m -> \t\t\033[36mDólar\033[m')
    print(f'\033[32m2\033[m -> \t\t\033[36mEuro\033[m')
    print(f'\033[32m3\033[m -> \t\t\033[36mBitcoin\033[m')
    linha()


def carregando():
    from time import sleep
    cabecalho("Convertendo...")
    sleep(1)
