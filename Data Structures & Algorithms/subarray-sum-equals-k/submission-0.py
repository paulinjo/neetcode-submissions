from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] += 1
        found = 0
        for n in nums:
            current_sum += n
            found += prefix_sums[current_sum - k]
            prefix_sums[current_sum] += 1
        return found