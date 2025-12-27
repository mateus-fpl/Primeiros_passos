quantidade = int(input("Digite quantos numeros vão no vetor: "))
numeros =[]

for i in range(quantidade):
    valor = int(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)
    
numeros.sort()
segundo_maior = numeros[-2]

print(f"O segundo maior numero é {segundo_maior}")