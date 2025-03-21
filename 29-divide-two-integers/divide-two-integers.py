class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        MAX_INT = 2147483647 
        MIN_INT = -2147483648  
        HALF_MIN_INT = -1073741824  

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        quotient = 0
        while divisor >= dividend:
            
            powerOfTwo = -1
            value = divisor
            while value >= HALF_MIN_INT and value + value >= dividend:
                print(value)
                value += value
                powerOfTwo += powerOfTwo
            quotient += powerOfTwo
            dividend -= value

        return -quotient if negatives != 1 else quotient