class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        memo = {}

        def uniqueSubsequences(i: int, j: int) -> int:

            M, N = len(s), len(t)

            if i == M or j == N or M - i < N - j:
                return int(j == N)

            if (i, j) in memo:
                return memo[i, j]

            ans = uniqueSubsequences(i + 1, j)

            if s[i] == t[j]:
                ans += uniqueSubsequences(i + 1, j + 1)

            memo[i, j] = ans
            return ans

        return uniqueSubsequences(0, 0)