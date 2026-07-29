class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        op_map = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: y - x,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(y / x),
        }

        for t in tokens:
            print(f"{t=}; {stack=}")
            if t not in op_map.keys():
                stack.append(int(t))
                continue
            
            x, y = stack.pop(), stack.pop()
            stack.append(op_map[t](x, y))
        return stack.pop()