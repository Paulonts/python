#operador "E" = "and"
saldo = 1000
saque = 200
limite = 400
conta_especial = True

retirada = saldo >= saque and limite >= saque
# se o "saldo" for "maior ou igual" a "saque"
# "E"
# "limite" for "menor ou igual" a "saque" eu posso retirar
# aqui as duas afirmacao precisa ser verdadeira


print(retirada) #true = posso retirar




#operador "OU" = "OR"
retirada = saldo >= saque or limite <= saque
# se o "saldo" for "maior ou igual" a "saque"
# "OU"
# "limite" for "menor ou igual" a "saque" eu posso retirar
# aqui somente uma afirmacao precisa ser verdadeira

print(retirada) #true = posso retirar




#operador de negacao
contatos_emergencia = []

averiguar = not 1000 > 1500 #not inverte os valores false passa ser true e vice-versa
print(averiguar)
averiguar = not 1000 < 1500
print(averiguar)




(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)