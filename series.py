def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def sum_series(n, first=0, second=1):
    a, b = first, second
    for _ in range(n):
        a, b = b, a + b
    return a
