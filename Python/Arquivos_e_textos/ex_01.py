email_bruto = "   mateus.paes@GMAIL.COM   \n"
email_limpo = email_bruto.strip().lower()
nome_usuario = email_limpo.split('@')
nome = nome_usuario[0]

print(f"E-mail limpo: {email_limpo}")
print(f"Nome usuário: {nome}")



