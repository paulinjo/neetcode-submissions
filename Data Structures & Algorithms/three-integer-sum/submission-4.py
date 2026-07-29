class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        nums = sorted(nums)
        for n_i, i, in enumerate(nums):
            n_j = n_i + 1
            n_k = len(nums) - 1
            while n_j < n_k:
                j, k = nums[n_j], nums[n_k]
                current = i + j + k
                print({f"{i=}; {j=}; {k=}"})
                if current == 0:
                    results.add(tuple(sorted([i, j, k])))
                
                if current < 0:
                    n_j += 1
                else:
                    n_k -= 1
        return [list(x) for x in results]