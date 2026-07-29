from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        
        if s_counter.keys() != t_counter.keys():
            return False

        for l, n in s_counter.items():
            if t_counter[l] != n:
                return False
        return True