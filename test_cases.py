import random
def generate_random_list(size, lower, upper):
    return [random.randint(lower, upper) for _ in range(size)]

def generate_bubble_sort_tests():
    tests = []
    tests.append(([], []))
    tests.append(([42], [42]))
    tests.append(([4, 2, 4, 1, 3], [1, 2, 3, 4, 4]))
    random_list = generate_random_list(1000, -1000, 1000)
    tests.append((random_list, sorted(random_list)))
    return tests

def generate_fibonacci_tests():
    tests = [1, 2, 5, 10, 15, 25, 80, 400, 1000, 20000, 40000]
    return tests

def generate_prime_tests():
    tests = [10, 50, 100, 200, 500]
    return tests

