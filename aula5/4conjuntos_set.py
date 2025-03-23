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