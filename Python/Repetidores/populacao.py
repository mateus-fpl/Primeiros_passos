pop_A = 80000
pop_B = 200000
anos = 0

while pop_A <= pop_B:
    pop_A = pop_A * (1.03)
    pop_B = pop_B * (1.015)
    anos = anos + 1

print(f"Levará {anos} anos para o país A ultrapassar o país B.")
print(f"População final de A: {pop_A:.0f}")
print(f"População final de B: {pop_B:.0f}")