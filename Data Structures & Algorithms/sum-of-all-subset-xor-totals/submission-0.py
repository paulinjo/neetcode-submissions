class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def subsets(i: int, current_subset: list[int]):
            nonlocal res

            if i == len(nums):
                x = 0
                for n in current_subset:
                    x ^= n
                res += x
                return

            subsets(i+1, current_subset + [nums[i]])
            subsets(i+1, current_subset)
        
        subsets(0, [])
        return res