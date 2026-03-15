class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        def compute():

            i = 0
            ans = 0

            while i < len(nums)-1:
                j = i+1
                prev = nums[j-1]
                d = nums[j] - prev
                flag = True
                last = 0

                while j < len(nums):
                    if nums[j]-prev == d:
                        prev = nums[j]

                        j+=1
                    else:
                        if flag:
                            prev = nums[j-1]+d
                            flag = False
                            last = j
                        else:
                            break
                        j+=1
                ans = max(ans, j - i)

                if flag:
                    i = j-1
                else: i = last-1
                if ans > len(nums)-i: return ans

            return ans

        ans = compute()
        #n = len(nums)
        nums.reverse()

        
        return max(ans,compute())
            
                    
        