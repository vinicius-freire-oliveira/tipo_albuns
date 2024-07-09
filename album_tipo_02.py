with open("listagem_coletaneas.txt", "r") as arquivo1:
    for linha in arquivo1:
        linha_limpa = linha.strip()
        print(linha_limpa)

print()

with open("listagem_soundtracks.txt", "r") as arquivo2:
    for linha in arquivo2:
        linha_limpa = linha.strip()
        print(linha_limpa)

print()

with open("listagem_tributos.txt", "r") as arquivo3:
    for linha in arquivo3:
        linha_limpa = linha.strip()
        print(linha_limpa)

print()

with open("listagem_coletaneas.txt", "r") as arquivo1:
    contador = 0
    for linha in arquivo1:
        if linha.strip():
            contador += 1
    print("Total Coletâneas:", contador)

with open("listagem_soundtracks.txt", "r") as arquivo2:
    contador = 0
    for linha in arquivo2:
        if linha.strip():
            contador += 1
    print("Total Soundtracks:", contador)

with open("listagem_tributos.txt", "r") as arquivo3:
    contador = 0
    for linha in arquivo3:
        if linha.strip():
            contador += 1
    print("Total Tributos:", contador)

print()

with open("listagem_coletaneas.txt", "r") as arquivo1:
    texto = arquivo1.read()
    contador = texto.count("1996")
    print("Total Coletâneas em 1996:", contador)

with open("listagem_soundtracks.txt", "r") as arquivo2:
    texto = arquivo2.read()
    contador = texto.count("1994")
    print("Total Soundtracks em 1994:", contador)

with open("listagem_tributos.txt", "r") as arquivo3:
    texto = arquivo3.read()
    contador = texto.count("1995")
    print("Total Tributos em 1995:", contador)