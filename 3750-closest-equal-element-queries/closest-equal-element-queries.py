class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        sz = len(nums)
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        for arr in indices.values():
            m = len(arr)
            if m == 1:
                nums[arr[0]] = -1
                continue
            for i in range(m):
                f, b = arr[(i + 1) % m], arr[(i - 1 + m) % m]
                forward = min((sz - arr[i] - 1) + f + 1, abs(arr[i] - f))
                backward = min(abs(b - arr[i]), arr[i] + (sz - b))
                nums[arr[i]] = min(backward, forward)
        for i in range(len(queries)):
            queries[i] = nums[queries[i]]
        return queries