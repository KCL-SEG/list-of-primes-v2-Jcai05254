"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("number of primes must be a positive number")
    list = []
    numb_iteration = 2
    while len(list) < number_of_primes:
        is_prime = True
        for p in list:
            if p * p > numb_iteration:
                break
            if numb_iteration % p == 0:
                is_prime = False
                break
        if is_prime:
            list.append(numb_iteration)
        numb_iteration += 1
    return list
