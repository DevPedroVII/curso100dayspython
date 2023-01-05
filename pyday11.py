



#Uma maneira de criar uma string de várias linhas é usar """ no início e no final das linhas. Usando aspas triplas em vez de aspas simples ou duplas, podemos atribuir um texto de várias linhas à string. método mais fácil de copiar várias linhas de algum lugar e atribuí-las a uma variável de string sem qualquer alteração.

#Código de exemplo:

multi_line_string = """this is line number 1
this is line number 2
this is line number 3
this is line number 4"""

print(multi_line_string)

#Uma string com várias linhas também pode
# ser criada colocando a barra invertida \ no final de cada linha da string com várias linhas.

#Sua função é a mesma que o método dos parênteses ().
# Ele também apenas concatena todas as linhas múltiplas e cria uma string com várias linhas.

#Código de exemplo:

multi_line_string = "this is line number 1 " \
"this is line number 2 " \
"this is line number 3 " \
"this is line number 4" \

print(multi_line_string)

#str.lstrip() método remove os caracteres principais especificados
# o argumento do método. Se não houver nenhum argumento dado,
# ele simplesmente remove os espaços em branco principais.


