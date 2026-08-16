import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        best = math.inf
        while j < len(nums):
            current = sum(nums[i:j+1])
            # print(f"{i=} | {j=} | {nums[i:j+1]} | {current=} | {best=}")
            if current >= target:
                best = min(best, (j - i) + 1)
                i += 1
            else:
                j += 1            
        return best if best < math.inf else 0