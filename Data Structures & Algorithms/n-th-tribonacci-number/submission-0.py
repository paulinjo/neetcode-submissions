class Solution:
    def tribonacci(self, n: int) -> int:
        cache = [-1] * max(n+1, 3)
        cache[0] = 0
        cache[1] = 1
        cache[2] = 1

        def dfs(i):
            if i < 0:
                return 0

            if cache[i] != -1:
                return cache[i]

            cache[i] = dfs(i-1) + dfs(i-2) + dfs(i-3)
            return cache[i]
        return dfs(n)