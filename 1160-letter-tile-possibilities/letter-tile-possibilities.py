class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        n = len(tiles)
        def rec( tiles,curr,ans):
            if tiles=="":
                ans.add(curr)
                return 
            for i in range(len(tiles)):
                #print(tiles,i)
                rec(tiles[:i]+tiles[i+1:],curr+tiles[i],ans)
                rec(tiles[:i]+tiles[i+1:],curr,ans)
        
        rec(tiles,"",ans)
        print(ans)
        return len(ans)-1
            
        