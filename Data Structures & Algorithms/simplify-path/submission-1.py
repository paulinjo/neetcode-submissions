import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = re.split(r'/+', path)
        cannonical_path = []
        for p in [t for t in re.split(r'/+', path) if t]:
            if p == "..":
                if cannonical_path:
                    cannonical_path.pop()
            elif p == ".":
                continue
            else:
                cannonical_path.append(p)
        
        return "/" + "/".join(p for p in cannonical_path)