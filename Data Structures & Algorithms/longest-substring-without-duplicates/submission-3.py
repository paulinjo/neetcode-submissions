class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        longest = 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                longest = max(longest, len(seen))
                r += 1
                continue

            seen.remove(s[l])
            l += 1
            r = l if l > r else r

        return longest