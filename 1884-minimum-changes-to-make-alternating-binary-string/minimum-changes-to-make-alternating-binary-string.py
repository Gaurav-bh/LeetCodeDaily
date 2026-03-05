class Solution:
    def minOperations(self, s: str) -> int:
        one = 0
        n = len(s)
        for i in range(n):
            if i%2==0 and s[i]!='1':
                one += 1
            elif  i%2==1 and s[i]!='0':
                one += 1
        print(one)
        zero = 0
        for i in range(n):
            if i%2==0 and s[i]!='0':
                zero += 1
            elif  i%2==1 and s[i]!='1':
                zero += 1
        print(zero)
        return min(one, zero)
        