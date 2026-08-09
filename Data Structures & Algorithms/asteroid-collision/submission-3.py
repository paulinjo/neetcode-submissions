class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            
            while len(stack) > 1:
                # print(f"{stack=}")
                b, a = stack.pop(), stack.pop()
                # print(f"{a=}; {b=}")

                if a < 0 and b < 0 or a > 0 and b > 0:
                    # moving in the same direction => no collision, add both back
                    stack.append(a)
                    stack.append(b)
                    break

                if a < 0 and b > 0:
                    # moving away from one another
                    stack.append(a)
                    stack.append(b)
                    break

                if abs(a) == abs(b):
                    # same size => both destroyed, add none back
                    break

                stack.append(a if abs(a) > abs(b) else b) # keep just the larger one
        return stack