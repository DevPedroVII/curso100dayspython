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
