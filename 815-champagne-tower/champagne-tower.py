class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured==0:
            return 0
        l=[poured]
        
        for i in range(query_row):
            temp=[]
            temp.append(max((l[0]-1)/2,0))
            for i in range(1,len(l)):
                temp.append(max((l[i-1]-1)/2,0)+max((l[i]-1)/2,0));
            temp.append(temp[0])
            l=temp.copy()
        return min(1,l[query_glass])