numero = int(input("Digite um número até 99: "))

unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

if numero < 10:
    print(unidades[numero])

elif numero < 20:
    print(especiais[numero - 10])

else:
    
    d = numero // 10  
    u = numero % 10   
    
    if u == 0:
        print(dezenas[d])
    else:
        print(f"{dezenas[d]} e {unidades[u]}")