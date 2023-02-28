def verifica_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num:
        print(num, "pertence à sequência de Fibonacci.")
    else:
        print(num, "não pertence à sequência de Fibonacci.")

verifica_fibonacci(21)  