class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        result = 0
        while l <= r:
            mid = (l + r) // 2
            val = mid ** 2
            if val == x:
                return mid
            elif val > x:
                r = mid - 1
            else:
                l = mid + 1
                result = mid
        return result