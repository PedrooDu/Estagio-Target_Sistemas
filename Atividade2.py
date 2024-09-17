# Função para verificar se um número pertence à sequência de Fibonacci
def pertence_fibonacci(numero):
    a, b = 0, 1

    if numero == 0 or numero == 1:
        return True

    while b < numero:
        a, b = b, a + b

    return b == numero

#print do resultado
def verificar_numero_fibonacci(numero):
    if pertence_fibonacci(numero):
        return print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        return print(f"O número {numero} não pertence à sequência de Fibonacci.")
    
# Teste
verificar_numero_fibonacci(21)  