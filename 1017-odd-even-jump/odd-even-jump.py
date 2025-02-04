from sortedcontainers import SortedDict
class Solution(object):
    

    def oddEvenJumps(self,A):
        N = len(A)
        if N <= 1:
            return N
        
        odd = [False] * N
        even = [False] * N
        odd[-1] = even[-1] = True
        
        vals = SortedDict()
        vals[A[-1]] = N - 1
        
        for i in range(N - 2, -1, -1):
            v = A[i]
            
            if v in vals:
                odd[i] = even[vals[v]]
                even[i] = odd[vals[v]]
            else:
                lower = vals.iloc[vals.bisect_left(v) - 1] if vals.bisect_left(v) > 0 else None
                higher = vals.iloc[vals.bisect_right(v)] if vals.bisect_right(v) < len(vals) else None
                
                if lower is not None:
                    even[i] = odd[vals[lower]]
                if higher is not None:
                    odd[i] = even[vals[higher]]
            
            vals[v] = i
        
        return sum(odd)


