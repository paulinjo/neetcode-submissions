class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1] * len(nums), [1] * len(nums)
        i = 0
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        j = len(nums) - 2
        while j >= 0:
            suffix[j] = suffix[j + 1] * nums[j + 1]
            j -= 1
        return [p * s for p, s in zip(prefix, suffix)]