from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        longest = 0
        counts = Counter()
        while r < len(s):
            counts[s[r]] += 1
            most_common = counts.most_common(1)[0][1]
            # print(f"{l=} | {r=} | {s[l:r+1]=} | {counts=} | {counts.most_common(1)}")
            if len(s[l:r+1]) - most_common <= k:
                longest = max(longest, (r - l + 1))
            else:
                counts[s[l]] -= 1
                l += 1
            r += 1
        return longest
