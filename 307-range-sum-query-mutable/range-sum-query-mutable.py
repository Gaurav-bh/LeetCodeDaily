class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.n = len(nums)
        self.bit = [0]*(self.n+1)
        for i in range(self.n):
            self.add(i,nums[i])
        #print(self.bit)
        
    def add(self, index: int, val: int) -> None:
        index += 1
        while index<=(self.n):
            self.bit[index] += val
            index += (index & (-index))
        #print(self.bit)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]   # compute difference
        self.nums[index] = val
        self.add(index, delta)
         
    def prefixSum(self,index):
        index += 1
        s = 0 
       
        while index>0:
            s += self.bit[index]
            index -= (index & (-index))
        return s


    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right) - self.prefixSum(left-1)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)