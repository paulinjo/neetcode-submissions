class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def compute(i: int, current_nums: list[int]):
            nonlocal result

            if sum(current_nums) == target:
                result.append(current_nums)
                return
            
            if sum(current_nums) > target:
                return

            if i == len(nums):
                return

            compute(i, current_nums + [nums[i]])
            compute(i+1, current_nums)
        compute(0, [])
        return result