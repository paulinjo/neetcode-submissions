class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}#{s}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        length_str = ""
        i = 0
        while i < len(s):
            if s[i] != "#":
                length_str += s[i]
                i += 1
                print(f"{i=}; {length_str=}")
                continue
            
            length = int(length_str)
            result.append(s[i+1:i+1+length])
            length_str = ""
            i += 1 + length
        return result