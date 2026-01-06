contatos = {
    "mateus_paes@yahoo.com.br": {"nome": "Mateus", "telefone": "0000-0000"},
    "amanda.pereiradasilva@gmail.com": {"nome": "Amanda", "telefone": "1111-1111", "extra": {"a": 1}},
}

telefone = contatos["mateus_paes@yahoo.com.br"]["telefone"]
print(telefone)

extra = contatos["amanda.pereiradasilva@gmail.com"]["extra"]["a"]
print(extra)