from collections import Counter, namedtuple
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        chars = [[-count, char] for char, count in Counter(s).items()]
        
        heapq.heapify(chars)
        result = ""
        tmp = None
        while chars:
            count, char = heapq.heappop(chars)
            
            if tmp:
                heapq.heappush(chars, tmp)
                tmp = None
            
            if result and result[-1] == char:
                return ""
            result += char

            count += 1
            if count < 0:
                tmp = [count, char]

        if tmp:
            if tmp[1] == result[-1]:
                return ""
            else:
                result += tmp[1]

        return result