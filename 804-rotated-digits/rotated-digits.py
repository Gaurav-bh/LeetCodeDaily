class Solution:
    def rotatedDigits(self, n: int) -> int:
        def check(number):
            validDigits={2,5,6,9}
            nonValidDigits={3,4,7,}
            flag=False
            while number:
                digit=number%10
                if digit  in validDigits:
                    flag=True
                if digit in nonValidDigits:
                    return False 
                number//=10
            return flag
        count=0
        for i in range(1,n+1):
            if check(i):
                count+=1
        return count