#Sets – Conjuntos em Python

#Armazena apenas itens não-duplicados (únicos)
#Suporta operações matemáticas sobre conjuntos (união, intersecção, etc)
#Não é possível modificar os itens existentes, mas podemos adicionar novos elementos (sets são mutáveis).
#Suporta elementos de qualquer tipo, não-ordenados e não-indexados.
#Podem conter apenas objetos imutáveis, como strings, ints, floats e tuplas de objetos também imutáveis.
#São escritos com chaves.
#Os sets são iteráveis (podemos acessar seus elementos um a um),
# e não são considerados sequências como as tuplas e as listas.
# Eles também não suportam indexação e slicing. Assim,
# os itens de um set são retornados em uma ordem diferente cada vez que acessamos o conjunto todo.
planeta_anao = {'Plutão','Ceres','Eris','Haumea','Makemake'}
print(planeta_anao)

#Criamos um conjunto atribuindo seus elementos, separados por vírgulas e entre chaves, a uma variável.

#Podemos descobrir o tamanho de um conjunto (número de elementos) com a função len():

qtde_planetas = len(planeta_anao)
print(qtde_planetas)

#É possível verificar se um conjunto possui um valor em particular com os operadores in e not in:

print('Ceres' in planeta_anao)
print('Lua' in planeta_anao)
print('Eris' not in planeta_anao)
