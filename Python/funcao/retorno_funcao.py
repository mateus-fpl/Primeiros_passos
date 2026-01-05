def positivo_negativo(n):
    if n > 0:
        return "P"
    else:
        return "N"

resultado = positivo_negativo(10)
resultado2 = positivo_negativo(-2)

print(f"O resultado é {resultado}")
print(f"O resultado é {resultado2}")