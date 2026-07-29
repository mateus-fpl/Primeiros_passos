from datetime import datetime, timedelta

hoje = datetime.now()
parcela1 = datetime.now() + timedelta(days=30)
parcela2 = datetime.now() + timedelta(days=60)
parcela3 = datetime.now() + timedelta(days=90)

print(f"A primeira parcela será {parcela1.strftime("%d/%m/%Y")}")
print(f"A segunda parcela será {parcela2.strftime("%d/%m/%Y")}")
print(f"A terceira parcela será {parcela3.strftime("%d/%m/%Y")}")


