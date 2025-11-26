class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        pre = 0
        s = 0
        for i in possible:
            if i==0:
                s -= 1
            else:
                s += 1
        n = len(possible)
        for i in range(n-1):
            if possible[i]==1:
                pre +=1
            else:
                pre -=1

            if pre>(s-pre):
                return i+1
        return -1
