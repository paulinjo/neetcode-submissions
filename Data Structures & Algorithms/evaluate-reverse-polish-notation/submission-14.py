class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t == "+":
                y, x = nums.pop(), nums.pop()
                nums.append(x + y)
                continue
            if t == "-":
                y, x = nums.pop(), nums.pop()
                nums.append(x - y)
                continue
            if t == "*":
                y, x = nums.pop(), nums.pop()
                nums.append(x * y)
                continue
            if t == "/":
                y, x = nums.pop(), nums.pop()
                nums.append(int(x / y))
                continue
            
            # print(f"{t=} | {nums=}")÷
            nums.append(int(t))
            
        return nums.pop()