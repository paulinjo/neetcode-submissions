class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.is_palindrome_helper(s, True)

    def is_palindrome_helper(self, s: str, can_delete: bool) -> bool:
        i, j = 0, len(s) - 1
        while i <= j:
            if not s[i].isalnum():
                i += 1
                continue

            if not s[j].isalnum():
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                if not can_delete:
                    return False

                return self.is_palindrome_helper(s[i+1:j+1], False) or self.is_palindrome_helper(s[i:j], False)

            i += 1
            j -= 1
        return True