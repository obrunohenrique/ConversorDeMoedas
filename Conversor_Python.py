from lib.interface import *
from lib.converções import *
from time import sleep

while True:
    menu('CONVERSOR DE MOEDAS')
    opcao = leiaint('Digite sua opção para Conversão(Digite 0 para Sair do Sistema): ')
    if opcao == 0:
        cabecalho('\033[31mEncerrando o Sistema...\033[m')
        sleep(1)
        break
    valor_real = leiafloat('Digite o valor em Real: R$ ')
    if opcao == 1:
        #Convertendo para Dólar
        valor_convertido = valor_real / float(cotacao_dolar)
        carregando()
        print(f'Valor em Real: R${valor_real}\nValor em Dólar: US${valor_convertido:.2f}')
    elif opcao == 2:
        #Convertendo para Euro
        valor_convertido = valor_real / float(cotacao_euro)
        carregando()
        print(f'Valor em Real: R${valor_real}\nValor em Euro: €{valor_convertido:.2f}')
        print('Aguarde o Retorno...')
    elif opcao == 3:
        #Convertendo para Bitcoin
        valor_convertido = valor_real / float(cotacao_bitcoin)
        carregando()
        print(f'Valor em Real: R${valor_real}\nValor em Bitcoin: {valor_convertido} BTC')
        linha()
        print('Aguarde o Retorno...')
    else:
        print(f'Essa opção não existe, Tente Novamente...')
        linha()
        print('Aguarde o Retorno...')
        sleep(2)
