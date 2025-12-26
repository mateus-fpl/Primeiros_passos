quantidade = int(input("Digite quantos números terão no vetor: "))
soma = 0
for i in range(quantidade):
    valor = int(input(f"Digite o {i+1}º numero: "))
    soma = soma+valor
   
media = soma/quantidade
print(f"Seus vetores têm a soma: {soma} e a média é {media}")