# Crie um programa que solicite ao usuário a informação de 3 estaturas. Caso existam estaturas iguais, o 
# programa deve apresentar a mensagem “Há, pelo menos, 2 pessoas com a mesma estatura”. 
# Caso contrário, o programa deve informar a maior estatura.

altura_maxima = 2.6
altura_minima = 0.30
while True:
    try:
        altura1 = float(input("Digite a 1º altura: "))
        altura2 = float(input("Digite a 2º altura: "))
        altura3 = float (input("Digite a 3º altura: "))
        if altura1 > altura_maxima or altura2 > altura_maxima or altura3 > altura_maxima:
            print("Limite máximo de altura excedido")
            continue

        if altura1 < altura_minima or altura2 < altura_minima or altura3 < altura_minima:
            print("Limite minímo de altura excedido")
            continue
        break       
    except ValueError:
        print ("Você deve digitar somente alturas. Tente outra vez.")

if altura1 == altura2 or altura1 == altura3 or altura2 == altura3:
    print("Há pelo menos duas alturas equivalentes.")
else:
    maior_altura = max(altura1, altura2, altura3)

print (f"A maior altura é {maior_altura:.2f} cm. Vá conquistar o mundo!")