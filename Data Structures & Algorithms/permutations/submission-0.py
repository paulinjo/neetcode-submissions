class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def compute(current: list[int]):
            nonlocal results

            if len(current) == len(nums):
                results.append(current)
                return

            for n in nums:
                if n not in current:
                    compute(current + [n])

        compute([])
        return results