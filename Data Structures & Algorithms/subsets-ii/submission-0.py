class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i: int, path: list[int]):
            if i == len(nums):
                res.append(path.copy())
                return

            # Choice 1: INCLUDE nums[i]
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

            # Choice 2: EXCLUDE nums[i]
            # Skip ALL future duplicates of nums[i] so we don't exclude THIS '2'
            # only to turn around and include the NEXT '2' in a separate branch!
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1, path)

        dfs(0, [])
        return res