class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        i = 0
        n = len(asteroids)
        while i<n:
            if mass >= asteroids[i]:
                mass += asteroids[i]
            else:
                return False
            i += 1
        return True

        