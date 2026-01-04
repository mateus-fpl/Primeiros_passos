string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

tamanho1 = len(string1)
tamanho2 = len(string2)

print(f'String 1: "{string1}" - Comprimento: {tamanho1}')
print(f'String 2: "{string2}" - Comprimento: {tamanho2}')

if tamanho1 == tamanho2:
    print("As duas strings possuem o mesmo comprimento.")
else:
    print("As duas strings possuem comprimentos diferentes.")

if string1 == string2:
    print("As duas strings possuem o mesmo conteúdo (são iguais).")
else:
    print("As duas strings possuem conteúdo diferente.")