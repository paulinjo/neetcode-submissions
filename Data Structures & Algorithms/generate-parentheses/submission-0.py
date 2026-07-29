class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        current = ""

        def backtrack(openCount, closedCount):
            nonlocal current
            if closedCount == openCount and len(current) == n * 2:
                results.append(current)
                return
            
            if openCount < n:
                current += "("
                backtrack(openCount + 1, closedCount)
                current = current[:-1]
            if closedCount < openCount:
                current += ")"
                backtrack(openCount, closedCount + 1)
                current = current[:-1]
        backtrack(0, 0)
        return results
