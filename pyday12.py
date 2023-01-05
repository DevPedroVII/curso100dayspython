#Python Keywords

#A inpalavra-chave tem dois propósitos:
# É usada para verificar se um valor está presente em uma sequência (lista, intervalo, string etc.).
# Também é usada para percorrer uma sequência em um forloop:

fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)
if "banana" in fruits:
  print("yes")


#Laços de repetições

#Uma estrutura de repetição em Python é um recurso para
# desenvolver tarefas repetitivas em um loop contínuo.
# O loop funciona até uma condição ser satisfeita.

#A estrutura de repetição
# em Python funciona como
# um bloco de código ideal
# para executar uma única operação em todos os dados.

#Contudo, se você precisa alterar o código a depender da informação lida,
#você pode estabelecer subcondições (com diferentes IFs) para verificações específicas.

##FOR
#FOR vai repetir uma ação de acordo com o que o usuário informar
#Syntax Python ex:

# * for <item> in <conjunto_de_itens>:
#    <bloco_de_codigo> *

#item: corresponde a cada elemento presente na variável que permite a iteração;

#conjunto_de_itens: pode ser uma lista, uma string, uma tupla,
# um dicionário ou um objeto que permita iterações.

frutas = ['Abacaxi', 'Morango', 'Uva']
for fruta in frutas:
    print(fruta)

for fruta in ['Abacaxi', 'Morango', 'Uva']:
    print(fruta)

#BREAK

#break a execução do loop ao encontrar uma condição específica.

#Devemos utilizar a instrução break
# em conjunto com uma estrutura condicional,
# como a if/else ou até mesmo com outro laço de repetição for.

#EX
#for <item> in <conjunto_de_itens>:
#    <bloco_de_codigo>
#    if <condicao_verdadeira>:
#         <outras_instrucoes>
#         break

#exemplo pratico

pessoas = [({'nome': 'João', 'cidade': 'Belo Horizonte'}),
                     ({'nome': 'Maria', 'cidade': 'São Paulo'}),
                     ({'nome': 'Pedro', 'cidade': 'Curitiba'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    print(contador)
    if pessoa['nome'] == 'Maria':
        print(pessoa['nome'], "mora em", pessoa['cidade'])
        break

# range()

#A função range() retorna
#uma série de números consecutivos. Por padrão,
#ela inicia no número 0 e é incrementada adicionando 1.

#A função range() é utilizada na estrutura de repetição for para executarmos
# um determinado conjunto de instruções pela
# quantidade de vezes indicadas na função. Veja um exemplo:

for numero in range(10):
    if numero % 2 == 0:
        print("O número", numero, "é par")

# else

#A estrutura de repetição for também pode ser utilizada com a cláusula else.
# Na prática, ela funciona quando o loop é encerrado sem nenhuma interrupção,
# como se utilizássemos a instrução break.
# É importante dizer que a cláusula else na estrutura de repetição for é opcional.

frutas = ['Abacaxi', 'Morango', 'Uva']
for fruta in frutas:
    print(fruta)
else:
    print("Laço de repetição finalizado.")
