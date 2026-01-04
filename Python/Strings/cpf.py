cpf = input("Digite o CPF (xxx.xxx.xxx-xx): ")

if len(cpf) == 14 and cpf[3] == "." and cpf[7] == "." and cpf[11] == "-":
    
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    
    if cpf_limpo.isdigit():
       
        soma = 0
        peso = 10
        for i in range(9):
            soma += int(cpf_limpo[i]) * peso
            peso -= 1
        
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto
        
        
        soma = 0
        peso = 11
        for i in range(10):
            soma += int(cpf_limpo[i]) * peso
            peso -= 1
            
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto
        
        
        if int(cpf_limpo[9]) == digito1 and int(cpf_limpo[10]) == digito2:
            print("CPF Válido!")
        else:
            print("CPF Inválido (Dígitos verificadores não batem).")
    else:
        print("Erro: O CPF deve conter apenas números nos locais indicados.")
else:
    print("Formato inválido! Use o padrão xxx.xxx.xxx-xx")

