def verificador_ano_bissexto():
    ano = int(input())  # Lê o ano da entrada

    # Verifica se o ano é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("SIM")
    else:
        print("NÃO")

verificador_ano_bissexto()
