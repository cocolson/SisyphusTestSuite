def bubble_sort(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be list type.")
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("List elements must be of int type.")
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def fibonacci(n):
    if not isinstance(n, int):
        raise ValueError("Input must be of int type.")
    if n < 1:
        raise ValueError("Input must be greater than 0.")
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        next = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next)
    return fib_seq

def prime_gen(n):
    if not isinstance(n, int):
        raise ValueError("Input must be of int type.")
    if n < 2:
        raise ValueError("Input must be greater than 2.")
    primes = []
    for num in range(2, n + 1):
        prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            primes.append(num)
    return primes

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True