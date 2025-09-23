class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=list(map(int,version1.split(".")))
        v2=list(map(int,version2.split(".")))
        l1=len(v1)
        l2=len(v2)
        rang=0
        if l1<l2:
            for i in range(l1):
                if v1[i]>v2[i]:
                    return 1
                elif v1[i]<v2[i]:
                    return -1
            for i in range(l1,l2):
                if v2[i]!=0:
                    return -1
            return 0
        else:
            for i in range(l2):
                if v1[i]>v2[i]:
                    return 1
                elif v1[i]<v2[i]:
                    return -1
            for i in range(l2,l1):
                if v1[i]!=0:
                    return 1
            return 0
        
        