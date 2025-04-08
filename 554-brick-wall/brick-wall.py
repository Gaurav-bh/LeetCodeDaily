class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hash={}
        wall_height=len(wall)
        for i in range(wall_height):
            no_of_bricks=len(wall[i])
            pre=0
            for j in range(no_of_bricks-1):
                pre+=wall[i][j]
                hash[pre]=hash.get(pre,0)+1
        min_crossed_bricks=math.inf
        if not hash:
            return wall_height
        for i in hash:
            min_crossed_bricks=min(min_crossed_bricks,wall_height-hash[i])
        return min_crossed_bricks
        