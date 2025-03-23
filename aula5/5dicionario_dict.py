#"fromkeys" usado para quando nao tem nome em especifico para ser utilizado
print (dict.fromkeys(["nome", "telefone"])) 
print (dict.fromkeys(["nome", "telefone"], "vazio"))   #colocar nome padrao 
print("\n")

#get usado para saber se uma chave existe ou não no dicionario
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-3333"}
}
#contatos["chave"] # keyError
print(contatos.get("chave")) # nome
print(contatos.get("chave", {})) # {}
print(contatos.get("guilherme@gmail.com", {})) # nome
print("\n")

#items
print(contatos.items()) #saber achave e os valores dentro da chave
print("\n")

#keys
print(contatos.keys()) #saber quantas chaves tem
print("\n")

#pop
resultado = contatos.pop("guilherme@gmail.com") #exclui os valores dentro da chave
print(resultado)
resultado = contatos.pop("guilherme@gmail.com", "chave não encontrada" )
print(resultado)
print("\n")

#setdefault serve para saber se um valor esta na sua chave, se nao tiver ele adiciona
contato = {"nome": "guilherme", "telefone": "1111-1111"}

contato.setdefault("nome", "giovana") #se ja tiver um valor ele nao altera
print(contato)
contato.setdefault("idade", 28)
print(contato)
print("\n")

#values retorna todos os valores pode ser usado tambem o for (arquivo "5dicionarios")
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-3333"},
    "ana@gmail.com": {"nome": "Ana", "telefone": "2222-2222"},
    "patricia@gmail.com": {"nome": "Patricia", "telefone": "1111-1111"},
    "lucas@gmail.com": {"nome": "Lucas", "telefone": "0000-0000"}
}
print(contatos.values())
print("\n")

#in usado para verificar se determinado valor esta dentro da chave
resultado = "guilherme@gmail.com" in contatos
print(resultado)
resultado = "nome" in contatos["guilherme@gmail.com"]
print(resultado)