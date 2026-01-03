notas = []

for i in range(4):
   num = float(input(f"Digite a {i+1}° nota: "))
   notas.append(num)

media = sum(notas)/len(notas)

print()
print(f"As notas foram: {notas}")
print(f"A média das notas foram: {media:.2f}")