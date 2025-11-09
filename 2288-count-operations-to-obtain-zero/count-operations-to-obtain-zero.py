class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        @lru_cache(None)
        def count(num1,num2):
            if num1==0 or num2==0:
                return 0
            c = 0
            if num1>=num2:
                c += count(num1%num2,num2)+num1//num2
            else:
                c += count(num1,num2%num1)+num2//num1
            return c
        

        return count(num1,num2)
        