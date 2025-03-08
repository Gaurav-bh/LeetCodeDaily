class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        i=len(digits)-1
        while i>-1 and carry==1:
            val=digits[i]+carry
            carry=val//10
            val=val%10
            digits[i]=val
            i-=1
        if carry:
            return [1]+digits
        return digits
        