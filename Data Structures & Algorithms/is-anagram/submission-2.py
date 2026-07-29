from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s, counter_t = Counter(s), Counter(t)
        
        if len(counter_s) != len(counter_t):
            return False

        for c in counter_s.keys():
            if counter_s.get(c) != counter_t.get(c):
                return False
        return True