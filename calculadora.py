# Solicita ao usuário para digitar o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário para digitar a operação a ser realizada
op = input("Digite a operação (+, -, *, /): ")

# Solicita ao usuário para digitar o segundo número
num2 = float(input("Digite o segundo número: "))

# Realiza a operação e exibe o resultado
if op == '+':
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif op == '-':
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif op == '*':
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif op == '/':
    resultado = num1 / num2
    print(f"{num1} / {num2} = {resultado}")
else:
    print("Operação inválida")
