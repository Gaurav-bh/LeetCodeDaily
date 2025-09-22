class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heappush(minHeap,(nums1[0]+nums2[0],0,0))
        n = len(nums1)
        m = len(nums2)
        count = 0
        ans = []
        visited = set()
        visited.add((0,0))
        while count < k:
            #print(minHeap)
            val, i , j = heapq.heappop(minHeap)
            
            ans.append([nums1[i],nums2[j]])
            if j<m-1 and  (i,j+1) not in visited:
                heapq.heappush(minHeap, (nums1[i]+nums2[j+1],i,j+1))
                visited.add((i,j+1))
            if i<n-1 and (i+1,j) not in visited:
                heapq.heappush(minHeap, (nums1[i+1]+nums2[j],i+1,j))
                visited.add((i+1,j))
            count += 1
        return ans

        