from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = defaultdict(int)
        l, r = 0, 0
        best = 0

        while l <= r and r < len(s):
            c_l, c_r = s[l], s[r]
            
            if counts[c_r]:
                counts[c_l] -= 1
                l += 1
            else:
                counts[c_r] += 1
                r += 1
                best = max(best, (r - l))
        return best