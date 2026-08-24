class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def dfs(step: int) -> int:
            if step == n:
                return 1
            
            if step > n:
                return 0
            
            if cache[step] != -1:
                return cache[step]

            cache[step] = dfs(step + 1) + dfs(step + 2)
            
            return cache[step]
        
        return dfs(0)