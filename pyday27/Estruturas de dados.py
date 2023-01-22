#Estruturas de dados

#list.append(x)
#Adiciona um item ao fim da lista. Equivalente a a[len(a):] = [x].

#list.extend(iterable)
#Prolonga a lista,
#adicionando no fim todos os elementos do argumento iterable passado como parâmetro.
#Equivalente a a[len(a):] = iterable.

#list.insert(i, x)
#Insere um item em uma dada posição.
#O primeiro argumento é o índice do elemento antes do qual será feita a inserção,
#assim a.insert(0, x) insere um elemento na frente da lista e a.insert(len(a), x) e equivale a a.append(x).

#list.remove(x)
#Remove o primeiro item encontrado na lista cujo valor é igual a x.
# Se não existir valor igual, uma exceção ValueError é levantada.


#list.pop([i])
#Remove um item em uma dada posição na lista e o retorna.
#Se nenhum índice é especificado, a.pop() remove e devolve o último item da lista.
#(Os colchetes ao redor do i na demonstração do método indica que o parâmetro é opcional,
#e não que é necessário escrever estes colchetes ao chamar o método.
# Você verá este tipo de notação frequentemente na Biblioteca de Referência Python.)

#list.clear()
#Remove todos os itens de uma lista. Equivalente a del a[:].

#list.reverse()
#Inverte a ordem dos elementos na lista.

list.copy()
Devolve uma cópia rasa da lista. Equivalente a a[:].
