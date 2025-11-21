class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        prefix = [0 for i in range(n+1)]
        unique = set()
        first = {}
        last = {}
        for i in range(n):
            unique.add(s[i])
            #prefix[i+1] = len(unique)
            if s[i] not in first:
                first[s[i]] = i
            last[s[i]] = i
        #rint(prefix)
        #print(first)
        #print(last)
        ans = 0
        for i in unique:
            if i in first and i in last and (first[i]!=last[i]):
                print("yes")
                se=set()
                for i in range(first[i]+1,last[i]):
                    se.add(s[i])
                ans+=len(se)
        return ans

       
        

        