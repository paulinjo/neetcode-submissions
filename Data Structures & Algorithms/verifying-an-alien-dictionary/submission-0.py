class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord_map = {c: i for c, i in zip(order, range(len(order)))}
        
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if ord_map[c2] > ord_map[c1]:
                    break
                if ord_map[c1] > ord_map[c2]:
                    return False
            
            # print(f"{w2[:len(w1)]}=")
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return False
        return True