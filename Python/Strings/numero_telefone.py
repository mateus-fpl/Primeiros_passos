telefone = input("Insira seus 8 números de telefone: ")

numero_limpo = telefone.replace("-", "")

if len(numero_limpo) == 7:
    numero_corrigido = "3" + numero_limpo
    print()
    print("Valida e corrige número de telefone")
    print(f"Telefone: {telefone}")
    print("Telefone possui 7 dígitos. Vou acrescentar o 3 na frente.")
    print(f"Telefone corrigido sem formatação: {numero_corrigido}")
    print(f"Telefone corrigido com formatação: {numero_corrigido[:4]}-{numero_corrigido[4:]}")
else:
    print("O número está correto.")


