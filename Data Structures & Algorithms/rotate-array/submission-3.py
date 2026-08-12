class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = [None] * len(nums)
        i, j = 0, k % len(nums)
        while i < len(nums):
            result[j] = nums[i]
            i += 1
            j = j + 1 if j + 1 < len(nums) else 0
            # print(f"{i=} | {j=} | {result=}")
        for n in range(len(nums)):
            nums[n] = result[n]