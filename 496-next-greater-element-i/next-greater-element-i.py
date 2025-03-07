class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        n=len(nums2)
        nextGreater=[-1 for i in range(n)]
        dic={}
        for i in range(n):
            dic[nums2[i]]=i
            while st and st[-1][0]<nums2[i]:
                val,ind=st.pop()
                nextGreater[ind]=nums2[i]
            st.append((nums2[i],i))
        ans=[]
        for i in nums1:
            ans.append(nextGreater[dic[i]])
        return ans


        