while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if 0 <=  nota <= 10:
        print(f"A nota do(a) aluno(a) é: {nota}")
        break
    else:
        print ("Nota inválida. Digite novamente um valor válido.")
    