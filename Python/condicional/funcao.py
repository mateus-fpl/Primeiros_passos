def exibir_mensagem():
    print ("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome = "anonimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Amanda")
exibir_mensagem_3()
exibir_mensagem_3(nome="Mateus")

def salvar_carro(marca, modelo, placa, ano):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{placa}/{ano}")
salvar_carro("Fiat", "Palio","ABC-1234", 1999)
salvar_carro(marca="Honda", modelo="Civic", placa="EFG-5432", ano=2009)
salvar_carro(**{"marca": "Volkswagen", "modelo": "FOX", "placa": "IJK-5656", "ano":2006})