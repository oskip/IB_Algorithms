import math


class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        primes = {i for i, p in enumerate(self.getPrimesTo(A)) if p is True}
        primes = sorted(primes)
        for p in primes:
            if A-p in primes:
                lower = min(A - p, p)
                higher = max(A - p, p)
                return p, A - p
                # if lower < solution[0] or (lower == solution[0] and higher < solution[1]):
                #     solution = (lower, higher)
        return (0, 0)

    def getPrimesTo(self, N):
        sieve = [True] * (N+1)
        sieve[0] = False
        sieve[1] = False

        for i in range(2, int(math.sqrt(N))+1):
            j = 2
            while j*i <= N:
                sieve[j*i] = False
                j += 1
        return sieve


class Solution2:
    def primesum(self, n):
        for i in xrange(2, n):
            if self.is_prime(i) and self.is_prime(n - i):
                return i, n - i

    def is_prime(self, n):
        if n < 2:
            return False

        for i in xrange(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True


print Solution2().primesum(16777214)