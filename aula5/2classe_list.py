lista = []

lista.append(1) #"append"adiciona na lista
lista.append('python')
lista.append([40, 20, 10])
print(lista)
print("")


#CLEAR
lista_clear = []
lista_clear.append(1)
lista_clear.clear() #"clear"limpa a lista
lista_clear.append('python')
lista_clear.append([40, 20, 10])
print(lista_clear)
print("")


#COUNT
cores = ["vermelho","azul","verde","azul"] 

print (cores.count("vermelho")) #conta quantas vezes p elemento aparece na lista
print (cores.count("azul"))
print (cores.count("verde"))
print("")


#EXTEND
linguagens = ["python", "js", "c"]
print(linguagens)
linguagens.extend(["java", "csharp"]) #extende a lista igual o append, so que tudo de uma vez
print(linguagens)
print("")


#INDEX
linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.index("java")) #mostra em que posição "java/elemento" está
print(linguagens.index("python")) #ele mostra a primeira ocorrencia, então se tiver mais de um igual na lista, ele para nno primeiro que achar
print("")


#POP
linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.pop()) #pega do ultimo colocado dentro da lista para a primeira e remove
print(linguagens.pop())
print(linguagens.pop(1))
print(linguagens)
print("")

#REMOVE
linguagens = ["python", "js", "c", "java", "csharp"]
(linguagens.remove("c")) #remove itens dentro da lista
print(linguagens)

#REVERSE
linguagens = ["python", "js", "c", "java", "csharp"]
print (linguagens[::-1])
linguagens.reverse()
print(linguagens)
print("")

#SORT
linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.sort(), linguagens) #coloca em ordem alfabetica crescente

linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.sort(reverse=True), linguagens) #coloca em ordem alfabetica decrescente

linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.sort(key=lambda x: len(x)), linguagens) #ordena por tamanho da palavra em ordem crescente

linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.sort(key=lambda x: len(x), reverse=True), linguagens) #ordena por tamanho da palavra em ordem decrescente
print("")

#LEN para ver o tamanho da lista
linguagens = ["python", "js", "c", "java", "csharp"]
print(len(linguagens))