class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            target = nums[i] * -1
            j, k = i+1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    results.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        return [list(r) for r in results]