# "in" verificar se algo está na sequência]

curso = "curso de python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

print("python" in curso)

print("maça" not in frutas)

print("maça" in frutas)

print(200 in saques)

print(100 and 1500 in saques)

print((150 or 1500) in saques) #ele verifica somente se o primeiro numero é verdadeiro, seguindo a ordem da variavel
#geralmente é usado um "for" para verificar com mais precisão

print((1500 or 150) in saques) #ele verifica somente se o primeiro numero é verdadeiro


