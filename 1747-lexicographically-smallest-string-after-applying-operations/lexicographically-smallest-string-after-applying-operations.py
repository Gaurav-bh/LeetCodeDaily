from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set([s])
        q = deque([s])
        best = s
        n = len(s)

        while q:
            cur = q.popleft()
            best = min(best, cur)

            # add 'a' to all odd indices
            add = list(cur)
            for i in range(1, n, 2):
                add[i] = str((int(add[i]) + a) % 10)
            add = ''.join(add)
            if add not in seen:
                seen.add(add)
                q.append(add)

            # rotate right by b
            rot = cur[-b:] + cur[:-b]
            if rot not in seen:
                seen.add(rot)
                q.append(rot)

        return best