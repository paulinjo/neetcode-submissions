class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = (r + l) // 2
            print(f"{middle=}")
            val = nums[middle]
            if val == target:
                return middle
            elif val < target:
                l = middle + 1
            else:
                r = middle - 1
        return -1