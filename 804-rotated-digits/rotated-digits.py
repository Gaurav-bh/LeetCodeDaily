class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotateDigit = {0:0, 1:1, 8:8, 2:5, 5:2, 6:9, 9:6  }

        def check(n):
            temp = n
            newNum = 0
            k = 0
            while n:
                r = n%10
                n = n//10
                if r not in rotateDigit:
                    return False
                newNum = (10**k)*rotateDigit[r]+newNum 
                k += 1  
            return newNum != temp
        count = 0
    
        for i in range(1,n+1):
            print(i)
            if check(i):
                print("yes")
                count += 1
        return count

        