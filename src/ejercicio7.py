"""La Secuencia de Fibonacci: Encuentre los primeros 100 números.
Luego guardar e imprimir en una lista cada uno de ellos.
Genere un archivo de texto"""


def fibonacci(n, memo):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib_n = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    memo[n] = fib_n

    return fib_n


n = 17
memo = {}
resultado = fibonacci(n, memo)
print(f"El término {n} de la secuencia de Fibonacci es: {resultado}")
print(memo)
