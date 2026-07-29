from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = len(s1)
        s1_counts = Counter(s1)
        
        def equal_counts(c1, c2):
            for k, v in c1.items():
                if c2.get(k) != v:
                    return False
            return True

        while j <= len(s2):
            substring = s2[i:j]
            substring_counts = Counter(substring)
            if equal_counts(s1_counts, substring_counts):
                return True
            i += 1
            j += 1

        return False