from collections import Counter

def to_count_list(s: str) -> list[int]:
    result = [0] * 26
    for c in s:
        result[ord(c) - ord('a')] += 1
    return result

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1, l2 = to_count_list(s), to_count_list(t)
        return all(a == b for a, b in zip(l1, l2))
