class Solution:
    def smallestNumber(self, n: int) -> int:

        def set_all_unset_bits(n):
            if n == 0:
                return 1
            
            n |= (n >> 1)
            n |= (n >> 2)
            n |= (n >> 4)
            n |= (n >> 8)
            n |= (n >> 16)
            return n

        return set_all_unset_bits(n)  # Output: 15

        