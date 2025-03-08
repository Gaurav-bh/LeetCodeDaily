# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.size=len(nums)
#         self.segment=[0 for i in range(2*self.size-1)]
#         self.build(0,0,self.size-1,nums)
#     def build(self,ind,low,high,nums):
#         #print("index",ind)
#         if low==high:
#             #print(low,ind)
#             self.segment[ind]=nums[low]
#             return 
#         mid=(low+high)//2
#         self.build(2*ind+1,low,mid,nums)
#         self.build(2*ind+2,mid+1,high,nums)
#         self.segment[ind]=self.segment[2*ind+1]+self.segment[2*ind+2]


#     def update(self, index: int, val: int) -> None:
#         def updatePoint(low,high,ind):
#             if low==high:
#                 self.segment[ind]=val
#                 return 
#             mid=(low+high)//2
#             if index>=low and index<=mid:
#                 updatePoint(low,mid,2*ind+1)
#             else:
#                 updatePoint(mid+1,high,2*ind+2)
#             self.segment[ind]=self.segment[2*ind+1]+self.segment[2*ind+2]
             
#         updatePoint(0,self.size-1,0)
#         print("here:- i am:- ",self.segment)
            
        

#     def sumRange(self, left: int, right: int) -> int:
#         def query(ind,low,high,l,r):
#             print("query",ind,high,low)
#             if high<l or low>r:
#                 return 0
#             if l<=low and r>=high:
#                 return self.segment[ind]
#             mid=(low+high)//2
#             left=query(2*ind+1,low,mid,l,r)
#             right=query(2*ind+2,mid+1,high,l,r)
#             return left+right
#         return query(0,0,self.size-1,left,right)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.segment = [0] * (4 * self.size + 1)
        self.build(0, 0, self.size - 1, nums)

    def build(self, ind, low, high, nums):
        print(ind,low)
        if low == high:
            
            self.segment[ind] = nums[low]
            return
        mid = (low + high) // 2
        self.build(2 * ind + 1, low, mid, nums)
        self.build(2 * ind + 2, mid + 1, high, nums)
        self.segment[ind] = self.segment[2 * ind + 1] + self.segment[2 * ind + 2]

    def update(self, index: int, val: int) -> None:
        def updatePoint(low, high, ind):
            if low == high:
                self.segment[ind] = val
                return
            mid = (low + high) // 2
            if index >= low and index <= mid:
                updatePoint(low, mid, 2 * ind + 1)
            else:
                updatePoint(mid + 1, high, 2 * ind + 2)  # Fixed issue here
            self.segment[ind] = self.segment[2 * ind + 1] + self.segment[2 * ind + 2]

        updatePoint(0, self.size - 1, 0)  # Start at root (index 0)

    def sumRange(self, left: int, right: int) -> int:
        def query(ind, low, high, l, r):
            if high < l or low > r:
                return 0
            if l <= low and r >= high:  # Fixed condition
                return self.segment[ind]
            mid = (low + high) // 2
            left_sum = query(2 * ind + 1, low, mid, l, r)
            right_sum = query(2 * ind + 2, mid + 1, high, l, r)  # Fixed issue here
            return left_sum + right_sum

        return query(0, 0, self.size - 1, left, right)  # Added return statement
