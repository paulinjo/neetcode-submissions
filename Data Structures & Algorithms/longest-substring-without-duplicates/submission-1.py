class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        best = 0

        while left < right and right <= len(s):
            substr = s[left:right]
            no_duplicates = len(substr) == len(set(substr))
            if no_duplicates:
                best = max(best, len(substr))
                right += 1
            else:
                left += 1
                right = right if left < right else right+1
        return best