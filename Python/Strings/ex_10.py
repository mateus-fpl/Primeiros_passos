numero = int(input("Digite um número: "))
valor_digitado = numero

unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", 
            "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

for i in range (valor_digitado, 99):
    if i < 20:
        print(unidades[i]) 
    else:
        
        d = i // 10  
        u = i % 10   
        
        if u == 0:
            print(dezenas[d])
        else:
            print(f"{dezenas[d]} e {unidades[u]}")