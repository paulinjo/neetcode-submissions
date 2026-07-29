from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = k+1
        best = k+1
        while j <= len(s):
            substring = s[i:j]
            substring_counts = Counter(substring)
            replaceable = sum(substring_counts.values()) - substring_counts.most_common(1)[0][1]
            print(substring)
            if replaceable <= k:
                j += 1
                best = max(best, len(substring))
            else:
                i += 1
                j += 1
        return best