def fibonacci(num):
    x1, x2 = 1, 1
    arr_fib = []
    while num > 0:
        arr_fib.append(x1)
        x1, x2 = x2, x1 + x2
        num -= 1
    return(arr_fib)

print(fibonacci(15))
