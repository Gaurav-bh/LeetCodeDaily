class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hashMap=dict()
        for key,val in nums1:
            if key not in hashMap:
                hashMap[key]=val
            else:
                hashMap[key]+=val
        
        for key,val in nums2:
            if key not in hashMap:
                hashMap[key]=val
            else:
                hashMap[key]+=val
        res=[]
        for i in hashMap:
            res.append([i,hashMap[i]])
        res.sort()
        return res
        