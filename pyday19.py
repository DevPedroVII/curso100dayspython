#Método Python Set union ()

#Retorna um conjunto que contém todos os itens de ambos os conjuntos, as duplicatas são excluídas

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)

#O union()método retorna um conjunto que
# contém todos os itens do conjunto original e
# todos os itens do(s) conjunto(s) especificado(s).

#Sintaxe
#set.union(set1, set2...)

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result)

#discard() Parameters
#A função de discard do python leva um único
#parâmetro do usuário. O parâmetro é 'x'.
#O elemento é descartado se estiver presente no conjunto.

#O valor de retorno do discard() é o elemento que é removido.
# Se o elemento  mencionado pelo usuário não estiver presente no conjunto,
# então o método de descarte retorna None.
