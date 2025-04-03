class Solution:
    def minInsertions(self, s: str) -> int:

        str1=s
        str2=s[::-1]
        n=len(s)
        m=n
        @lru_cache(200000)
        def lcs(i,j,m,n):
            if i==m or j==n:
                return 0
            c=0
            if str1[i]==str2[j]:
                c=lcs(i+1,j+1,m,n)+1
            c=max(c,lcs(i+1,j,m,n))
            c=max(c,lcs(i,j+1,m,n))

            return c
        return n-lcs(0,0,m,n)
        
        