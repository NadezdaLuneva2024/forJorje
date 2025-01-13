# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def fibonacci(n: int) -> list[int]:
    """
    Skriv beskrivning här.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_list = [0, 1]
    for i in range(2, n):
        nesta_tal = fib_list[-1] + fib_list[-2]
        fib_list.append(nesta_tal)    
    return fib_list