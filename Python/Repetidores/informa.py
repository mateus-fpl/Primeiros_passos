while True:
    nome = input("Escreva seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("O nome deve ter mais que 3 caracteres")

while True:
    idade = int(input("Escreva a sua idade: "))
    if 0 <= idade <= 150:
        break
    else:
        print("A idade deve ser maior que 0 e menor que 150!")

while True:
    salario = float(input("Digite seu salário: "))
    if salario > 0:
        break
    else:
        print("O salário deve ser pelo menos de 1 real")
while True:
    estado_civil= input("Coloque seu estado civil(s,c,v,d): ").lower()
    if estado_civil in 'scvd':
        break
    else:
        print("O estado cívil deve ser: s, c, v, d")

print("-" * 20)

print(f"Seu nome é: {nome}")
print(f"Sua idade é: {idade}")
print(f"Seu salário é: R$ {salario:.2f}")
print(f"Seu estado civil é: {estado_civil}")