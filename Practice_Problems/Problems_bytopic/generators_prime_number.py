'''
Create a generator that yields prime numbers
up to a given limit.

gen = prime_generator(20)
Output: 2, 3, 5, 7, 11, 13, 17, 19
'''

def prime_numbers_generator(n):
    for x in range(2, n):      # start from 2, smallest prime
        is_prime = True
        for i in range(2, x):  # check if x is divisible by anything
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            yield x            # only yield if prime ✅

gen = prime_numbers_generator(20)
for prime in gen:
    print(prime, end=',')
