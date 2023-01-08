## metodos LIST

#append	item	Acrescenta um novo item no final da lista

#insert	posição, item	Insere um novo item na posição dada

#pop	nenhum	Remove e returno o último item
#pop	posição	Remove e retorna o item da posição.

##Pertinência em uma Lista

#in e not in são operadores booleanos ou lógicos que testam a pertinência (membership)
#em uma sequência. Já usamos esses operadores com strings e eles também funcionam aqui.

frutas = ["maca", "laranja", "banana", "cereja"]

print("maca" in frutas)
print("pera" in frutas)

#Listas são mutáveis
Diferentemente de strings, listas são mutáveis (mutable).
Isto significa que podemos alterar um item em uma lista
acessando-o diretamente como parte do comando de atribuição.
Usando o operador e
indexação (colchetes) à esquerda de um comando de atribuição, podemos atualizar um dos itens de uma lista.
