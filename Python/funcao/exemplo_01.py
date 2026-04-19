def formatar_nome(nome_sujo):
    nome_limpo = nome_sujo.strip().title()
    return nome_limpo

usuario = "   mAteus pAes   "
nome_final = formatar_nome(usuario)

print(nome_final)

def gerar_usuario(login_sistema):
    login = login_sistema.strip().lower().replace(" ", "")
    return login


cadastro = gerar_usuario("   Mateus  paes")
print(cadastro)