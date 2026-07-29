from datetime import datetime,timedelta

valor = float(input("Digite o valor da fatura: "))
vencimento = datetime.now()
pagamento = input("Digite a data do pagamento: ")
pagamento_modificado = datetime.strptime(pagamento, '%d/%m/%Y')


if pagamento_modificado < vencimento:
    print("Dias de atraso: 0")
    print(f"O valor total a pagar é: R$ {valor:.2f}")
else:
    atraso = pagamento_modificado - vencimento
    dias = atraso.days 

    # Cálculo dos juros (0.1% ao dia = 0.001) sobre o valor original
    juros = valor * 0.001 * dias
    valor_com_juros = valor + juros

    print(f"Dias de atraso: {dias} dia(s)")
    print(f"Valor dos juros por atraso: R$ {juros:.2f}")
    print(f"O valor total com o acréscimo dos juros é: R$ {valor_com_juros:.2f}")