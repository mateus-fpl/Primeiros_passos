def principal():
    print('executando a funcao princiapl')

    def funcao_interna():
        print('executado a função interna')

    def funcao_2():
        print('executando a função 2')

    funcao_interna()
    funcao_2()

principal()