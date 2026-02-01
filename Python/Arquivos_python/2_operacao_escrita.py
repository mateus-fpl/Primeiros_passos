arquivo = open('teste.txt', 'w')
arquivo.write("Esrevendo dados em um novo arquivo de texto.")
arquivo.writelines(['\n', 'escrevendo ','\n', 'um ','\n', 'novo ','\n', 'texto'])
arquivo.close()