class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def compute_subsets(i: int, current_subset: list[int]):
            if i == len(nums):
                results.append(current_subset)
                return
            
            compute_subsets(i+1, current_subset + [nums[i]])
            compute_subsets(i+1, current_subset)
        
        compute_subsets(0, [])
        return results