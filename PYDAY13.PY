#while True em Python

#O loop while é usado para executar um bloco
# de código repetidamente até que determinada condição booleana
# seja avaliada como False.
# Se escrevermos enquanto True, o loop será executado para sempre.

#while True:
 #   pass

#Se executarmos o código acima, esse loop será executado
# um número infinito de vezes. Para sair desse loop, usaremos explicitamente a
# Instrução *break* .

N = 10
Sum = 0

# This loop will run forever
while True:
    Sum += N
    N -= 1

    # the below condition will tell
    # the loop to stop
    if N == 0:
        break

print(f"Sum of First 10 Numbers is {Sum}")

#No exemplo acima, usamos a instrução while True para executar o
# loop while e adicionamos uma instrução if que interromperá a execução
# do loop quando o valor de N se tornar 0 Se não escrevermos esta instrução if,
# então o loop será executado para sempre e começará a
# adicionar os valores negativos de N à soma.

#slice() Function

#A slice()função retorna um objeto de fatia.

#Um objeto de fatia é usado para especificar como fatiar uma sequência.
#Você pode especificar onde começar a fatiar e onde terminar.
#Você também pode especificar a etapa, que permite, por exemplo, fatiar apenas itens alternados.
