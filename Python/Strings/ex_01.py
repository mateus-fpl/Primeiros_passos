print ("Comparação de Strings:")

frase1 = input("Digite a primeira frase: ")
frase2 = input("Digite a segunda frase: ")

tamanho1 = len(frase1)
tamanho2 = len(frase2)

print (f'String 1: {frase1}')
print (f'String 2: {frase2}')

print(f'Tamanho de "{frase1}": {tamanho1} caracteres')
print(f'Tamanho de "{frase2}": {tamanho2} caracteres')

if frase1 == frase2:
    print ("As duas strings são do mesmo tamanho")
else:
    print ("As duas strings são de tamanhos diferentes")

if frase1 == frase2:
    print ("As duas strings possuem conteúdo semelhante")
else:
    print ("As duas strings possuem conteúdo diferentes")


