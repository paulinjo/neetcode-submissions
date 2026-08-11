class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        results = set()

        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                t = target - nums[a] - nums[b]
                
                c, d = b+1, len(nums) - 1
                while c < d:
                    if nums[c] + nums[d] == t:
                        results.add(tuple(sorted(nums[n] for n in [a,b,c,d])))
                        c += 1
                        d -= 1
                    elif nums[c] + nums[d] < t:
                        c += 1
                    else:
                        d -= 1
        return [list(x) for x in results]