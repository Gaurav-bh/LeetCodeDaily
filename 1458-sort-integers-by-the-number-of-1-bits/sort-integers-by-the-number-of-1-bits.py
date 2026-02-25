class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def calculateOnes(num):
            count = 0 
            while num:
                r = num%2
                if r==1:
                    count +=1
                num //=2
            return count

        def check(a, b):
            onesA = calculateOnes(a)
            onesB = calculateOnes(b)
            if onesA > onesB:
                return 1
            elif onesA < onesB:
                return -1
            return 0
            
        n = len(arr)

        for i in range(n):
            for j in range(i+1,n):
                k = check(arr[i], arr[j])
                if  k == 0:
                    if arr[i] > arr[j]:
                        arr[i], arr[j] = arr[j], arr[i]
                elif k>0:
                    arr[i], arr[j] = arr[j], arr[i]

        return arr

        