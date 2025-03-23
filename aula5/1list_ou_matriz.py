frutas = ["laranjas", "maca", "uva"] #lista declarada
print(f"{frutas}")
frutas = [] #coloca quantas eu quiser
letras = list("python") #cada letra é um elemento
print(f"{letras}")
numeros = list(range(10)) #lista vai de 0 a 9
print(f"{numeros}")
carro = ["ferrari", "F8", 4200000, 2020, "2900KM", "São Paulo", True] #informações do carro
print(f"{carro}")

print(f"""
Carro = {carro[0]}
Modelo = {carro[1]}
Preço = {carro[2]}
Ano = {carro[3]}
Quilometragem = {carro[4]}
Estado = {carro[5]}
""")

print(f"""
Carro = {carro[0]}
Modelo = {carro[1]}
Preço = {carro[2]}
Ano = {carro[3]}
Quilometragem = {carro[4]}
Estado = {carro[-2]} 
""")
#numemros negativos pega de tras para frente

matriz = [
    [ 1 ,"a", 2 ],
    ["b", 3 , 4 ],
    [ 6 , 5 ,"c"]
]

print (matriz[0])
print (matriz[0][0])
print (matriz[0][2])
print (matriz[2][2])


lista = ["p","y","t","h","o","n"]

print (lista[2:])
print (lista[:2])
print (lista[1:3])
print (lista[0:3:2])
print (lista[::])
print (lista[::-1])


for carro_percorrer in carro:
    print(carro_percorrer) #mostra o que tem dentro da lista 1 por 1
print(carro) #mostra o que tem dentro da lista mas de uma vez só


numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
impares = []


#versao 1 compactação
for numero_percorrer_par in numeros:
    if numero_percorrer_par % 2 == 0:
        pares.append(numero_percorrer_par) #essa funcão joga os numeros pares dentro da variavel
print(pares)

for numeros_percorrer_impares in numeros:
    if numeros_percorrer_impares % 2 == 1:
        impares.append(numeros_percorrer_impares) #essa funcão joga os numeros impares dentro da variavel
print(impares)

#versao 2 compactação
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero_par for numero_par in numeros if numero_par % 2 == 0]
print(pares) #PEGA SOMENTE OS NUMEROS PARES DA LISTA

impares = [numero_impar for numero_impar in numeros if numero_impar % 2 == 1]
print(impares) #PEGA SOMENTE OS NUMEROS IMPARES DA LISTA

quadrado = [elevacao**2 for elevacao in numeros ]
print(quadrado) #PEGA TODOS OS NUMEROS DA LISTA E ELEVA A 2


