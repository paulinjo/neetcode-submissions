class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i <= j:
            c_i, c_j = s[i], s[j]

            if not c_i.isalnum():
                i += 1
                continue

            if not c_j.isalnum():
                j -= 1
                continue

            if c_i.lower() != c_j.lower():
                return False

            i += 1
            j -= 1

        return True