class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        n = len(nums)

        for i in range(n - 2):
            # Early exit: smallest element > 0 means no 3 elements can sum to 0
            if nums[i] > 0:
                break

            # Skip duplicate anchor values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1
            target = -nums[i]

            while j < k:
                current_sum = nums[j] + nums[k]

                if current_sum == target:
                    results.append([nums[i], nums[j], nums[k]])
                    
                    # Move pointers past duplicates
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1
                elif current_sum < target:
                    j += 1
                else:
                    k -= 1

        return results