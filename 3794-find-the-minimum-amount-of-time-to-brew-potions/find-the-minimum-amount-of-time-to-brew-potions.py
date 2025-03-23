# class Solution:
#     def minTime(self, skill: List[int], mana: List[int]) -> int:
#         m=len(mana)
#         n=len(skill)
#         #dp=[[0 for i in range(n) ] for j in range(m)]
#         curr=[0 for i in range(n)]
#         #rev=[0 for i in range(n)]
        
        
#         #print(prev)
#         #print(atEachPotion)
#         for i in range(m):
#             for j in range(n):
#                 if j>0:
#                     curr[j]=max(curr[j],curr[j-1])
#                 curr[j]+=mana[i]*skill[j]
#             #print("first",curr)
#             for j in range(n-1,0,-1):
                
#                 curr[j-1]=curr[j]-mana[i]*skill[j]
#             #prev=curr.copy()
#         return curr[n-1]
        
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        dp = [0]*n
        for j in range(m): 
            for i in range(n): 
                if i: dp[i] = max(dp[i-1], dp[i])
                dp[i] += skill[i] * mana[j]
            for i in range(n-1, 0, -1): 
                dp[i-1] = dp[i] - skill[i] * mana[j]
        return dp[n-1]