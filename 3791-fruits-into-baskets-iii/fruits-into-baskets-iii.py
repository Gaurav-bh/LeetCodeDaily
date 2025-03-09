class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        def build(ind,low,high,arr,segment):
            if low==high:
                segment[ind]=arr[low]
                return 
            mid=(high+low)//2
            build(ind*2+1,low,mid,arr,segment)
            build(ind*2+2,mid+1,high,arr,segment)
            segment[ind]=max(segment[ind*2+1],segment[ind*2+2])

        def search(ind,low,high,k,segment):
            if k>segment[ind]:
                return -1
            if low==high:
                segment[ind]=-1
                return low
            mid=(high+low)//2
            pos=-1
            if k<=segment[ind*2+1]:
                pos=search(ind*2+1,low,mid,k,segment)
            else:
                pos=search(ind*2+2,mid+1,high,k,segment)
            segment[ind]=max(segment[ind*2+1],segment[ind*2+2])
            return pos



        i=0
        j=0
        n=len(fruits)
        m=len(baskets)
        count=0
        j=0
        visited=[False for i in range(m)]
        segment=[-1 for i in range(4*n)]
        build(0,0,n-1,baskets,segment)
        #print(segment)
        for i in range(n):
            #print(segment,count)
            if search(0,0,n-1,fruits[i],segment)==-1:
                count+=1
        return count

            
            