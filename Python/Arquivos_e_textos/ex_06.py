emails = [
    "   mateus@gmail.com   \n",
    "ANA@HOTMAIL.COM",
    "  joao.silva@outlook.com ",
    "INVALIDO.COM"
]

emails_validos = []

for email in emails:
    email_limpos = email.strip().lower()
    if "@" in email:
        emails_validos.append(email_limpos)

print(emails_validos)