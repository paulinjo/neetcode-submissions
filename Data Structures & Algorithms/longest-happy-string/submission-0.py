import heapq
from collections import namedtuple

Letter = namedtuple('Letter', ['remaining', 'char'])

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pool = [
            Letter(char=c, remaining=-i) for c, i in
            [('a', a), ('b', b), ('c', c)] 
        ]
        pool = list(filter(lambda letter: letter.remaining < 0, pool))
        heapq.heapify(pool)
        held_letter = None

        result = ""

        while pool:
            letter = heapq.heappop(pool)
            
            if held_letter:
                heapq.heappush(pool, held_letter)
                held_letter = None
            
            result += letter.char
            remaining = letter.remaining + 1

            letter = Letter(char=letter.char, remaining=remaining)

            if remaining == 0:
                continue

            if result[-2:] == letter.char * 2:
                held_letter = letter
                continue

            heapq.heappush(pool, letter)
        return result
