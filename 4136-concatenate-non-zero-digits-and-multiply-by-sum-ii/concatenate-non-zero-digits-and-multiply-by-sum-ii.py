class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # prefix arrays
        prefVal = [0] * (n+1)
        prefSum = [0] * (n+1)
        prefCnt = [0] * (n+1)

        # Precompute pow10 for maximum possible non-zero digits
        # Worst case all digits are non-zero → max count = n
        pow10 = [1] * (n+1)
        for i in range(1, n+1):
            pow10[i] = (pow10[i-1] * 10) % MOD

        # Build prefix arrays
        for i in range(n):
            d = ord(s[i]) - 48
            prefVal[i+1] = prefVal[i]
            prefSum[i+1] = prefSum[i]
            prefCnt[i+1] = prefCnt[i]

            if d != 0:
                prefVal[i+1] = (prefVal[i] * 10 + d) % MOD
                prefSum[i+1] += d
                prefCnt[i+1] += 1

        res = []
        for l, r in queries:
            # prefix differences
            val1 = prefVal[l]
            val2 = prefVal[r+1]

            sum1 = prefSum[l]
            sum2 = prefSum[r+1]

            cnt1 = prefCnt[l]
            cnt2 = prefCnt[r+1]

            # length of substring (only non-zero digits)
            k = cnt2 - cnt1

            # substring value = val2 - val1 * 10^k
            substringVal = (val2 - (val1 * pow10[k]) % MOD + MOD) % MOD
            substringSum = (sum2 - sum1)

            ans = (substringVal * substringSum) % MOD
            res.append(ans)

        return res
