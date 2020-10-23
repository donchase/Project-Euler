primes = list(filter(lambda x: x % range(2,x) != 0, range(2, 8)))
print(primes)
