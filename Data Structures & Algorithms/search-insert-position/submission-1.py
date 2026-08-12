class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = (l + r) // 2
            val = nums[middle]
            if val == target:
                return middle
            elif val > target:
                r = middle - 1
            else:
                l = middle + 1
        # print(f"{l=} | {r=}")
        return l