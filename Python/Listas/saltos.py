ordem = ["Primeiro salto", "Segundo salto", "Terceiro salto", "Quarto salto", "Quinto salto"]
saltos_totais = []

while True:
    nome_do_atleta = input("Digite o nome do competidor: ")
    
    if nome_do_atleta == "":
        print("Programa encerrado")
        break
    else: 
    

        for i in range(5):
            saltos = float(input(f"Altura do {i+1}° salto: "))
            saltos_totais.append(saltos)

        print()

        resultado = " - ".join(map(str, saltos_totais))
        media = sum(saltos_totais)/len(saltos_totais)

        print(f"Nome do Atleta: {nome_do_atleta}")

        for i in range(len(saltos_totais)):
            print(f"{ordem[i]}: {saltos_totais[i]:.1f} m")

        print()
        print("Resultado final:")
        print(f"Nome do Atleta: {nome_do_atleta}")
        print(f"Saltos: {resultado}")
        print(f"Média dos saltos: {media}m")

        break