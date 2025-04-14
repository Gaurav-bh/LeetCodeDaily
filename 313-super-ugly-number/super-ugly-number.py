class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglies = [1]
        np = len(primes)
        indices = [0] * np
        next = primes.copy()

        for i in range(1, n):
            uglies.append(ugly := min(next))

            for k in range(np):
                if ugly == next[k]:
                    indices[k] += 1
                    next[k] = primes[k] * uglies[indices[k]]

        return uglies[n - 1]