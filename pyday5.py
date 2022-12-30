#Modules in Python

#Os modulos sao codigos separados Reponsaveis pela funcionalidade de de um grande codigo
#é como criar um carro cada Modulo é como se fosse uma "parte do carro" no processo de criaçao
# para utilizar os modulos é so necessario dar um import em cada page

#

import random

random_side = random.randint(0,1)

if random_side == 1:
    print("heads")
else:
    print("tails")
