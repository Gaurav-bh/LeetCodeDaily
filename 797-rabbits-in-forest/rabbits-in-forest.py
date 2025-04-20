class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = [0] * 1000
        for x in answers:
            count[x] += 1

        ans = 0
        for k in range(1000):
            ans += (-count[k]) % (k + 1) + count[k]
        return ans
