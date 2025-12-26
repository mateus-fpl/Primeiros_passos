peso = float(input("Digite seu peso:"))
alt = float(input("Digite sua altura:"))

IMC = peso/(alt*alt)

if IMC < 18.5:
    print(f"{IMC: .2f}\nAbaixo do peso!")
elif IMC < 24.9:
    print(f"{IMC: .2f}\nPeso ideal.")
elif IMC < 29.9:
    print(f"{IMC: .2f}\nLevemente acima do peso")
elif IMC < 34.9:
    print(f"{IMC: .2f}\nObesidade Grau I")
elif IMC < 39.9:
    print(f"{IMC: .2f}\nObesidade Grau II (severa)")
else: 
    print(f"{IMC: .2f}\nObesidade Grau III (mórbida)")