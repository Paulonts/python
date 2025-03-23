pessoa = {"nome": "paulo", "idade": 21}
pessoa["telefone"] = "4002-8922"
print(pessoa)
print(pessoa["nome"]) #pega somente o elemento desejado
print(pessoa["telefone"]) #pega somente o elemento desejado


#substituir
pessoa["nome"] = "maria"
pessoa["idade"] = 20
pessoa["telefone"] = "4002-4545"
print(pessoa)

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-3333"},
    "ana@gmail.com": {"nome": "Ana", "telefone": "2222-2222"},
    "patricia@gmail.com": {"nome": "Patricia", "telefone": "1111-1111"},
    "lucas@gmail.com": {"nome": "Lucas", "telefone": "0000-0000"}
}
print("telefone de Ana", contatos["ana@gmail.com"]["telefone"], "\n")

#exibindo dicionario com for

for chave in contatos:
    print(chave, contatos[chave])
print("\n")
for chave, valor in contatos.items(): #mais indicado a ser utilizado
    print(chave, valor) #chave = email,  #valor = valor da variavel

