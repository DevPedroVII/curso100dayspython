#Function

#Funções são um recurso poderoso das linguagens de programação.
# Ao desenvolver uma aplicação utilizamos elas a todo momento,
# quer sejam as que nós mesmos escrevemos para as rotinas especificas ou
# aquelas já disponibilizadas pela linguagem de programação escolhida,
# suas bibliotecas e frameworks.

#Resumindo

#funções são blocos de código que realizam
# determinadas tarefas que normalmente precisam ser executadas
# diversas vezes dentro de uma aplicação.

#A sintaxe de uma função é definida por três partes
# : nome, parâmetros e corpo,
# o qual agrupa uma sequência de linhas que representa algum comportamento.

#EX

def hello(meu_nome):
  print('Olá',meu_nome)

#Def ()

#def = definição de função necessária para o Python entender que isso é uma função.

def area(base, altura):

    area = base * altura

    print(area)

    return area



area(10,5)

#return = utilizado para retornar um valor calculado pelos comandos.
# Nos dois casos é retornado o valor da variável.

# yield = Yield é basicamente uma palavra chave que é utilizada semelhante ao return
#Porém esta função retorna um generator!

#Devemos utilizar o yield ou o generator
# quando há uma lista muito grande que queremos lidar, para não termos que salvar esta na memória

#Lambda = As funções Lambda são chamadas de funções anônimas:
# funções que o usuário não precisa definir,
# ou seja, não vai precisar escrever a função e depois utilizá-la dentro do código.

