class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        def countOnes(s):
            count = 0 
            for i in s:
                if i=="1":
                    count += 1
            return count
        
        lasers = []
        for i in bank:
            laser = countOnes(i)
            if laser!=0:
                lasers.append(laser)

        ans = 0 
        n = len(lasers)
        for i in range(1,n):
            ans += lasers[i-1]*lasers[i]
        return ans



        