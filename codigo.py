"""
exercicio proposto
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Nao permita que o programa quebre com
erros de indice inexistentes na lista

funçoes 
inserir item na lista
apagar item da lista
listar valores da lista
se a lista estiver vazia exibir um erro
"""
i=0
lista= []

while True:

    letra_escolhida = input('Escolha uma opção:\n[I]nserir, [A]pagar, [L]istar: ')
    letra_escolhida = letra_escolhida.lower()

    if letra_escolhida == 'i':

        inserir = input ('\nValor: ')

        if len(inserir) < 1:
            print('Por favor insira algum valor\n')

        else:

            lista.append (inserir)

            print('\nValor inserido com sucesso\n')

    elif letra_escolhida =='a':

        if len(lista)<1:

            print('\nUps, lista vazia.\nNão temos o que apagar aqui\n')

        else:

            print('\nApagado o ultimo valor: ', lista[-1].capitalize(),'\n')
            lista.pop()
            
    elif letra_escolhida == 'l':
        
        if len (lista) < 1 :

            print (f'\nLista de compras: \nLista vazia \n')

        else:

            print('\nSua lista é:')

            for item in lista:

                print(item.captalize())

            print('\n')

    else:
        print(' \nOpção invalida. \nRevise as opções disponiveis e escolha uma delas. \n')

    
