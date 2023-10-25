def fib(n):
    """Calculates the nth Fibonacci number"""

    if n < 0:
        raise ValueError("Input 0 or greater only!")

    if n < 2:
        return n

    last = 0
    next = 1

    for _ in range(1, n):
        last, next = next, last + next
        print(last, next)
    return next

print(fib(9))

