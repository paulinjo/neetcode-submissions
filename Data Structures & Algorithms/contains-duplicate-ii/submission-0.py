from collections import Counter

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        l, r = 0, 0
        while r < len(nums):
            if nums[r] in seen:
                return True
            
            seen.add(nums[r])
            r += 1
            if (r - l) > k:
                seen.remove(nums[l])
                l += 1
        return False
