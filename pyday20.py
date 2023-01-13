#Dicionarios

#Os dicionários são coleções de itens e seus elementos são armazenados de forma não ordenada.

#Exemplo de sua sintaxe:

#dicio = {'chave': 'valor'}

#print(type(dicio))

#Criando dicionários
#Agora vamos ver 6 maneiras de criar um mesmo dicionário!

#O modo mais simples de criar um dicionário:


#dicio_2 = {'primeiro': 1, 'segundo':  2, 'terceiro': 3}
#Também podemos utilizar a função dict do próprio Python (built-in function), passando as chaves e valores como parâmetros:

#dicio = dict(primeiro=1, segundo=2, terceiro=3)
#Utilizando a função zip para concatenar a chave:valor em um elemento do objeto dict:

#dicio_3 = dict(zip(['primeiro', 'segundo', 'terceiro'], [1, 2, 3]))
#Utilizando uma lista de tuplas com itens simbolizando chave e valor em um objeto dict:


#dicio_4 = dict([('primeiro', 1), ('segundo', 2), ('terceiro', 3)])

#Com Dict Comprehensions!


#dicio_6 = {name: idx + 1 for idx, name in enumerate(('primeiro', 'segundo', 'terceiro'))}
#Por mais estranho que pareça, podemos tentar transformar uma variável do tipo dicionário em dicionário.


#dicio_5 = dict({'primeiro': 1, 'segundo':  2, 'terceiro': 3})

#Dicionários também contam com um método chamado get() que fornecerá o mesmo resultado

nome_Idade = {
    'Maria': 50,
    'Mario': 25
}

