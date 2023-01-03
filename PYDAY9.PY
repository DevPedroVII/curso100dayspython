#mutabilidade
#Uma string no Python é uma sequência de caracteres imutável.

#para ver como isso ocorre na prática,
# vamos fazer uso da função id(), que retorna à identidade de um objeto.

nome = 'Eduardo'
print(id(nome))
nome = 'Felipe'
print(id(nome))

#Há casos em que é necessário juntar informações textuais e para esses denominamos concatenação, que é a junção do conteúdo de strings. Vamos fazer um exemplo no qual podemos ver como isso ocorre na prática:

nome = 'Daniel'
sobrenome = 'Silva'

nome_completo = nome + ' ' + sobrenome

print(nome_completo)
#Para fazer a concatenação entre strings no Python é necessário usar o sinal de adição +.

#Comparação de Strings
#No Python podemos comparar strings de duas formas distintas: com o operador == ou is.

nome_1 = 'Eduardo'
nome_2 = 'Eduardo'

if nome_1 == nome_2:
    print('iguais')
else:
    print('diferentes')

#Já com o operador is, o que será comparado é
# a referência do endereço na memória.
# Vamos usar o mesmo código anterior apenas trocando a condição:

nome_1 = 'Eduardo'
nome_2 = 'Eduardo'

if nome_1 is nome_2:
    print('iguais')
else:
    print('diferentes')

#Principais métodos de Strings

#Método find()
# Com o método find() podemos procurar uma substring dentro de uma string
# e retornar a posição onde ela foi encontrada, como mostra o Código

mensagem = 'string no Python'
print(mensagem.find('Python')) # 10

#No caso de a ocorrência não ser encontrada,
# o resultado será -1, como mostra o Código

mensagem = 'string no Python'
print(mensagem.find('Java'))

#Método replace()

#O método replace() é utilizado para substituir
# ocorrências de substrings dentro de uma string.

mensagem = 'Quero aprender Java! Na DevMedia tem salas de Java para aprender essa linguagem'
nova_mensagem = mensagem.replace('Java', 'Python')
print(nova_mensagem)

#Método split()

#Com o método split() desmembramos uma string em múltiplas strings
# através de um separador passado no parâmetro, retornando todas numa lista.

mensagem = 'Estou aprendendo Python na DevMedia'
nova_mensagem = mensagem.split(' ')
print(type(nova_mensagem)) # type 'list'
print(nova_mensagem) # ['Estou', 'aprendendo', 'Python', 'na', 'DevMedia']

##  obrigatório o uso de um separador na função split()
# quando usada com aspas, pois caso contrário, um erro
# será gerado com a mensagem ValueError: empty separator.
# Se as aspas não forem usadas com split(), a função considerará o espaço em branco como separador.

#Método upper()

#Com o método upper() retornamos uma cópia
#da string com todas as letras minúsculas convertidas em maiúsculas.
# Segue no Código

mensagem = 'eu gosto de Python'
nova_mensagem = mensagem.upper()

print(nova_mensagem) # EU GOSTO DE PYTHON

#Método lower()

#Com o método lower(), retornamos uma cópia da string com todas as letras maiúsculas convertidas
# em minúsculas. Vejamos o Código

mensagem = 'eu gosto de Python'
nova_mensagem = mensagem.lower()

print(nova_mensagem) # eu gosto de python

#Acentuação no Python
#Para podermos usar acentuação no Python, devemos definir a codificação utf-8

nome = 'João da Silva'
print(nome)

#O código acima irá gerar o seguinte erro: SyntaxError: Non-ASCII character
# '\xc3' que é gerado devido ao caractere acentuado que usamos na variável nome.
