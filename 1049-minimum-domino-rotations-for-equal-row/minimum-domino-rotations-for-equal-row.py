class Solution:
    def minDominoRotations(self, top: List[int], bottom: List[int]) -> int:
        n=len(top)
        val1=top[0]
        val2=bottom[0]
        countVal1=1
        countVal2=1
        for i in range(1,n):
            if top[i]==val1 or bottom[i]==val1:
                countVal1+=1
            if top[i]==val2 or bottom[i]==val2:
                countVal2+=1
        if countVal1!=n and countVal2!=n:
            return -1
        countVal1inTop=0
        countVal2inTop=0

        countVal1inBottom=0
        countVal2inBottom=0
        for i in range(n):
            if top[i]==val1:
                countVal1inTop+=1
            if top[i]==val2:
                countVal2inTop+=1
            if bottom[i]==val1:
                countVal1inBottom+=1
            if bottom[i]==val2:
                countVal2inBottom+=1
        if countVal1==n:
                return n-max(countVal1inTop,countVal1inBottom)
        if countVal2==n:
                return n-max(countVal2inTop,countVal2inBottom)
                    