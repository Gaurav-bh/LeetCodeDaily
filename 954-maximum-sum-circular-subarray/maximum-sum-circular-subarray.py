class Solution:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        n=len(arr)
        sum=0
        tempMax_Sum=0
        tempMin_sum=0
        min_sum=math.inf
        max_sum=-1*math.inf
        for i in range(n):
            sum+=arr[i]
            #print(tempMax_Sum)
            tempMax_Sum+=arr[i]
            #print(tempMax_Sum)
            max_sum=tempMax_Sum if tempMax_Sum>max_sum else max_sum
            if tempMax_Sum<0:
                #print("yes")
                tempMax_Sum=0
            #print("after",tempMax_Sum)


            tempMin_sum+=arr[i]
            min_sum=tempMin_sum if tempMin_sum<min_sum else min_sum
            tempMin_sum=0 if tempMin_sum>0 else tempMin_sum
        #print(max_sum)
        #print(min_sum)
        #print(sum)
        if sum==min_sum:
            return max_sum
        else:
            return max(max_sum,sum-min_sum)
                