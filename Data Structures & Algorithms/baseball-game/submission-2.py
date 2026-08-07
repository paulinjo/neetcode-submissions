class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for o in operations:
            if o == "+":
                scores.append(scores[-1] + scores[-2])
                continue
            
            if o == "D":
                scores.append(scores[-1] * 2)
                continue

            if o == "C":
                scores.pop()
                continue

            scores.append(int(o))
        
        return sum(scores)