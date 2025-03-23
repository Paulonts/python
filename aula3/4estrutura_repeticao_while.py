#mesma pegado do for, mas utilizamos quando não sabemos o tanto de vez que vai repetir
opcao = -1

while opcao != 0:
    opcao = int(input("[1]sacar: \n[2]Extrato: \n[0]Sair: \n "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("exibindo o extrato...")
    elif opcao != 1 and 2 and 0:
        print("opção invalida")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")



while True:
    numero = int(input("informe um numero: "))

    if numero == 10:
        break

print(f"numero achado {numero}")