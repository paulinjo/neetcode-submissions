class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        seen = set()
        while j < len(nums):
            if nums[j] in seen:
                j += 1
                continue
            
            nums[i] = nums[j]
            seen.add(nums[j])
            i += 1
            j += 1
        return i