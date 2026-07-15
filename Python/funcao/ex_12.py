# 🧪 Exercício: Validador de Urinálise (EAS)
# Crie uma função que receba três parâmetros e decida se o laudo está "LIBERADO" ou "RETIDO PARA REVISÃO".

# Parâmetros de Entrada:
# proteinas (String): "Ausente", "+" ou "+++".

# leucocitos_campo (Int): Quantidade por campo.

# aspecto (String): "Límpido" ou "Turvo".

# Critérios para RETER o laudo (Basta um ser verdadeiro):
# proteinas igual a "+++"

# leucocitos_campo maior que 10

# aspecto igual a "Turvo"

# Retorno da Função:
# Deve retornar uma tupla com: (Status, Lista_de_Motivos).
# (Se for liberado, a lista de motivos retorna vazia []).

def paciente_urinalise (proteina, leucocitos_campo, aspecto):
    resultado_paciente = []

    if proteina == "+++":
        resultado_paciente.append(proteina)

    if leucocitos_campo > 10:
        resultado_paciente.append(leucocitos_campo)

    if aspecto == "Turvo":
        resultado_paciente.append(aspecto)

    if len(resultado_paciente) > 0:
        status = "RETIDO!"
    else:
        status = "LIBERADO!"

    return resultado_paciente, status

prot = input("Digite a quantidade de proteínas: ")
while True:
    try:
        leuc = float(input("Digite a quantidade de leucócitos: "))
        if leuc >= 0:
            break
        else:
            print("Não se aceita valores negativos.")
    except ValueError:
        print("Digite um número maior que 0")

aspect = input("Digite a cor da urina(Limpido/Turvo): ")

resultado = paciente_urinalise(prot, leuc, aspect)

print("--------- Urinálise ------------")
print(f"O resultado do paciente é {resultado}")


