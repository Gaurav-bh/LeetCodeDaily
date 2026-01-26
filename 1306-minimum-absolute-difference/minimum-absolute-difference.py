class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        absoluteDiff = 1000000009
        n = len(arr)
        for i in range(1,n):
            if (arr[i]-arr[i-1]) == absoluteDiff:
                ans.append((arr[i-1],arr[i]))
            elif (arr[i]-arr[i-1]) < absoluteDiff:
                absoluteDiff = (arr[i]-arr[i-1]) 
                ans = []
                ans.append((arr[i-1],arr[i]) )
        return ans
        