
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_letters = [0] * 26
        for c in s1:
            s1_letters[ord(c) - ord('a')] += 1

        s2_letters = [0] * 26
        for c in s2[0:len(s1) - 1]:
            s2_letters[ord(c) - ord('a')] += 1
        
        i, j = 0, len(s1) - 1
        while j < len(s2):
            # print(f"{i=} | {j=} | {s2[i:j]}=")
            s2_letters[ord(s2[j]) - ord('a')] += 1
            if all(x == y for x, y in zip(s1_letters, s2_letters)):
                return True
            s2_letters[ord(s2[i]) - ord('a')] -= 1
            i += 1
            j += 1
        return False

