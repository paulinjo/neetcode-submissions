class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            current = numbers[i] + numbers[j]
            if current == target:
                return [i+1, j+1]

            if current > target:
                j -= 1
            else:
                i += 1
        raise ValueError("Unable to find solution")