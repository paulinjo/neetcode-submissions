class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            
            # first item, or not higher temp
            if not stack:
                stack.append(i)
                continue
            
            print(f"{stack=}")
            while stack and temperatures[stack[-1]] < temperatures[i]:
                results[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return results