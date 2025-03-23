adicao = 1 + 1
print(adicao)

subtração = 10 - 8
print(subtração)

multiplicacao = 4 * 3
print(multiplicacao)

divisao = 12 / 3
print(divisao ) #divisao com numero flutuante

divisao = 12 // 2
print(divisao) #divisao inteira

modulo = 10 % 3
print(modulo) #modulo (resto da divisao)

exponencial = 2 ** 3
print(exponencial) #exponencial (numero elevado)


#precendencia de operadores  (qual numero vai ser resolvido primeiro)
x = 10 - 5 * 2 #resultado é 10, pq resolve primero a multiplicação 
print(x)
x = (10 - 5) * 2 #resultado é 10, pq se resolve tudo que esta entre parenteses primero
print(x)

#ORDEM DE PRECEDENCIA
# parenteses
# expoentes
# multiplicação e divisao (da esquerda para direita)
# soma e subtracao (da esquerda para direita)

#EXEMPLO
produto_1 = 10
produto_2 = 20 

print(produto_1 + produto_2) # 30
print(produto_1 + produto_2 * 2) # 50
print((produto_1 + produto_2) * 2) # 60
print(((produto_1 + produto_2) * 2) ** 2) # 3.600
 
