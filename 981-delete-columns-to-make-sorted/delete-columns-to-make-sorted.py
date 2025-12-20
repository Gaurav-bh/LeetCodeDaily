class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        
        ans = 0
        for i in range(n):

            for j in range(1,len(strs)):
                curr =  strs[j][i]
                col =  strs[j-1][i]
                #print(curr,col)
                if col>curr:
                    
                    ans += 1
                    break
                
        return ans
            
        