class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        k = [[strs[0][i]] for i in range(n)]
        ans = set()
        for j in range(1,len(strs)):
            s = strs[j]
            for i in range(n):
                curr = s[i]
                col = k[i][-1]
                #print(curr,col)
                if col>curr:
                    
                    ans.add(i)
                k[i].append(curr)
        return len(ans)
            
        