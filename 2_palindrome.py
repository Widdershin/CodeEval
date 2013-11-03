
def generate_primes(n):
    primes = []
    
    for i in range(2, n + 1):

        if not filter(lambda x: i % x == 0, primes):
            primes.append(i)

    return primes

def is_palindrome(s):
    return s == s[::-1]

def largest_prime_palindrome(n):

    primes = generate_primes(n)

    for prime in reversed(primes):
        if is_palindrome(str(prime)):
            return prime

print largest_prime_palindrome(1000)