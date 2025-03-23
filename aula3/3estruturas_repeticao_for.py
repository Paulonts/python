texto = input("informe uma frase: ")
VOGAIS = "AEIOU"

for busca_letras in texto:
    if busca_letras.upper() in VOGAIS:
        print(busca_letras, end="")
        print()
print("\n")
#neste codigo foi pedido para citar uma frase, está frase fica armazenada na variavel texto
#criamos um laço de repetição para buscar as vogais que esta na varivel texto
#criamos tambem uma constante vogal, para fazer a comparação
#então dentro do laço de repetição foi criado uma variavel para buscar as vogais dentro da variavel texto
#criamos um if para fazer a verificação dessas vogais dentro da variavel texto
#se acharmos alguma vogal na variavel texto, o nosso print dentro do if vai mostrar





#RANGE NO FOR
for numero in range(0,11):
    print(numero, end="\n")

#exibindo a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")

for numero in range(100):
    if numero % 2 != 0:
        print(numero)

for numero in range(100):
    if numero % 2 == 0:
        print(numero)

for numero in range(100):
    if numero == 97:
        continue
    print(numero)