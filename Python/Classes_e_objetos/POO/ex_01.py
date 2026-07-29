class Sistema:
    def __init__(self, nome, email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = True

    def desativar(self):
            self.ativo = False

    def atualizar_email(self, novo_email):
        if novo_email == self.email:
            print(f"⚠️ O e-mail informado ({novo_email}) já é o atual.")
        elif self.ativo != True:
            print(f"⚠️ O cadastro deve estar ativo para alterar o email!.")
        else:
            self.email = novo_email

    def autenticar(self, senha_digitada):
        return senha_digitada == self.senha

    def alterar_senha(self, senha_atual, nova_senha):
        if senha_atual != self.senha:
            print("⚠️ Senha incorreta!")
        elif len(nova_senha) < 6:
            print("⚠️ A nova senha precisa ter ao menos 6 caracteres!")
        else:
            self.senha = nova_senha
            print("✅ Senha alterada com sucesso!")


    def exibir_perfil(self):
        if self.ativo == True:
            print(f"Nome: {self.nome} | Email: {self.email} | Status: Ativo")
        else:
            print(f"Nome: {self.nome} | Email: {self.email} | Status: Inativo")


usuario1 = Sistema("Mateus", "mateus_mateus@gmail.com","******")
usuario1.atualizar_email("mateus_suetam@gemini.com")
usuario1.alterar_senha("******","12345")
usuario1.exibir_perfil()

