nome = "Guilherme"
idade = 28
profissao = "programador"
linguagem = "Python"

print("Óla, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado"
      "no curso de %s." % (nome, idade, profissao, linguagem)) 
#Hoje em dia não é muito utilizado esse tipo de interpolação

print("Óla, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado"
      "no curso de {}.".format (nome, idade, profissao, linguagem)) 
#não é muito usado

print("Óla, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado"
      "no curso de {linguagem}.".format (nome=nome, idade=idade, profissao=profissao, linguagem=linguagem)) 
#Não é muito usado

print(f"Óla, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado"
      f"no curso de {linguagem}.") 
#mais usado atualmente

PI = 3.14159
print(f"Valor de PI: {PI:.2f}")