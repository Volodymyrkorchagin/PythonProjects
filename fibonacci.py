def fibonacci(start, end):
    a = 0
    b = 1

    while a <= end:
        if start <= a <= end:
            yield a

        result = a + b
        a = b
        b = result