#Condições falsas - sequencias vazias

#Listas vazias são valores falsos, ou seja, elas
# avaliam como False em um contexto booleano:
#EX:
num = [""]
bool(num)
False  #*ATENÇÃO COM OS SPACES*

#Pode adicionar elementos a uma lista vazia
# usando os métodos append() e insert()

#append() adiciona o elemento ao final da lista.
#insert() adiciona o elemento em um índice específico da lista à sua escolha.

# listas podem ser valores verdadeiros ou falsos,
# dependendo de estarem vazias ou não ao serem avaliadas

if num:
	print("A lista não está vazia")
else:
	print("A lista está vazia")

#Em geral:Se a lista não está vazia, a verificação gera True,
# então a instrução de if é executada.
#Se a lista está vazia, a verificação gera False, então a instrução de else é executada.


num = []
for i in range(3, 15, 2):
	num.append(i)

#Verificamos o valor da variável para ver se os itens foram
# adicionados com sucesso e confirmamos
# que a lista não está mais vazia.

#list()

#Como alternativa, você pode criar uma lista vazia com o
# construtor de tipo list(), que cria um novo objeto de lista.

#Se nenhum argumento for dado, o construtor
# cria uma nova lista vazia, [].
