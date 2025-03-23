saldo = 2000
saque = float(input("informe o valor do saque: "))

if saldo >= saque: #se saldo for maior ou igual a saque, ele vai rodar esse print
    print("realizando saque!")
else: #se não for maior ou seja, se o saque que você for fazer
    #for maior que o saldo, vai rodar esse print
    print("saldo insuficiente!") 


opcao = int(input("informe uma opcao:\n [1] Sacar: \n [2] Extrato: \n [3] sair \n "))

if opcao == 1:
    valor = float(input("informe a quantia para o saque: "))
elif opcao == 2:    #usamos o elif quando temos mais de uma opcao
    print("exibindo o extrato...")
elif opcao == 3:
    print("programa encerrado")
else:
    print("opção invalida")



#if aninhado "if dentro de if"

conta_normal = True
saldo_normal = 2000
saque = float(input("quantos você deseja sacar: "))
cheque_especial = 450
conta_universitaria = False
saldo_universitario = 500

if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado com o uso do cheque especial")
    else:
        print("não foi possivel realizar o saque, saldo insuficiente!")
elif conta_universitaria:
    if saldo_universitario >= saque:
        print("saque realizado com sucesso!")
    else:
        print("saldo insuficiente!")
else:
    print("sistema não reconheceu seu tipo de conta, entre em contato com o banco.")



#if ternário
saldo = 2000
saque = 2500
status = "sucesso" if saldo >= saque else "falha" 
#se o "if" for atendido o "if" retornará a variavel "status"
print(f"{status} ao realizar o saque")