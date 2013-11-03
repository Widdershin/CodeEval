def generate_n_primes(n):
    primes = []
    
    i = 2
    while len(primes) < n:

        if not filter(lambda x: i % x == 0, primes):
            primes.append(i)

        i += 1

    return primes

print sum(generate_n_primes(1000))