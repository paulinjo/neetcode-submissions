from collections import deque

class Solution:
    def openLock(self, deadends: List[str] | set[tuple], target: str | tuple) -> int:
        best = math.inf
        stack = deque()
        deadends = {tuple(int(digit) for digit in deadend) for deadend in deadends}
        target = tuple(int(digit) for digit in target)

        stack.append(((0, 0, 0, 0), 0))
        visited = set()
        while stack:
            combination, length = stack.popleft()
            if combination in deadends:
                continue

            if combination == target:
                best = min(best, length)
                continue

            for i in range(len(combination)):
                n = combination[i]
                for d in (1, -1):
                    new_n = n + d
                    new_n = 0 if new_n == 10 else new_n
                    new_n = 9 if new_n == -1 else new_n

                    next_combination = [*combination]
                    next_combination[i] = new_n

                    next_combination = tuple(next_combination)
                    if next_combination in deadends or next_combination in visited:
                        continue
                    
                    visited.add(next_combination)
                    stack.append((next_combination, length+1))
        return best if best < math.inf else -1