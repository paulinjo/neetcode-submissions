class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 0
        for n in nums:
            if n - 1 in nums_set:
                continue
            
            current = 1
            i = 1
            while True:
                if n + i in nums_set:
                    current += 1
                    i += 1
                else:
                    break
            best = max(best, current)
        return best
