

from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        
        # Preprocess grid
        litter_pos = {}
        litter_id = 0
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sx, sy = i, j
                elif classroom[i][j] == 'L':
                    litter_pos[(i, j)] = litter_id
                    litter_id += 1
        
        total_litter = len(litter_pos)
        full_mask = (1 << total_litter) - 1
        
        queue = deque()
        visited = dict()
        
        # Start from S with energy and no litter collected
        queue.append((sx, sy, 0, energy, 0))  # x, y, mask, energy left, steps
        visited[(sx, sy, 0)] = energy
        
        while queue:
            x, y, mask, e, steps = queue.popleft()
            
            # All litter collected
            if mask == full_mask:
                return steps
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                    ne = e - 1
                    if ne < 0:
                        continue
                    
                    nmask = mask
                    if (nx, ny) in litter_pos:
                        nmask |= (1 << litter_pos[(nx, ny)])
                    
                    if classroom[nx][ny] == 'R':
                        ne = energy
                    
                    key = (nx, ny, nmask)
                    if visited.get(key, -1) < ne:
                        visited[key] = ne
                        queue.append((nx, ny, nmask, ne, steps + 1))
        
        return -1

        