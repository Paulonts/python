#set retira numeros ou letras repetidas
print (set([1, 1, 2, 3, 4, 3]))
print (set ("abacaxi"))
print (set(("palio", "gol", "celta", "palio")))

linguagens = {"python", "java", "python"}
print(linguagens)



#convertendo set para uma list
numeros = {1, 2, 3, 2}
#print(numeros[0]) nao conseguimos pegar por matriz, pois a variavel "numeros" é um set
numeros = list(numeros)
print(numeros[0])



#metodos da classe set
#union
conjunto_a = {1, 2}
conjunto_b = {3, 4}
print ("union", conjunto_a.union(conjunto_b),"\n")

#intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print("intersection", conjunto_a.intersection(conjunto_b),"\n")

#difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print("difference", conjunto_a.difference(conjunto_b))
print("difference", conjunto_b.difference(conjunto_a),"\n")

#difference symmetric
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print("difference symmetric", conjunto_a.symmetric_difference(conjunto_b),"\n")

#issubset      os elementos do conjunto "a" pertence a "b". os elementos do conjunto "b" não pertence a "a"
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
print("issubset", conjunto_a.issubset(conjunto_b))
print("issubset", conjunto_b.issubset(conjunto_a),"\n")

#isdisjoint    nenhum dos elementos do conjunto se toca 
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}
print("isdisjoint", conjunto_a.isdisjoint(conjunto_b))
print("isdisjoint", conjunto_a.isdisjoint(conjunto_c))

#add 