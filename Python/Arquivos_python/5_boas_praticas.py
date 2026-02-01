from pathlib import Path

ROOT_PATH = Path(__file__).parent

#With garante que o arquivo foi fechado automaticamente
try:
    with open(ROOT_PATH /"llorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")

try:
    with open (ROOT_PATH/'arquivo-utf-8.txt', encoding='utf-8') as arquivo:
        arquivo.write('Aprendendo a manipular arquivos utilizando Python.')
except IOError as exc:
    print(f"Erro aao abrir o arquivo {exc}")

try:
    with open (ROOT_PATH/'arquivo-utf-8.txt', encoding='ascii') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
