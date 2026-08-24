from collections import defaultdict
UNVISITED, ACTIVE, VISITED = 0, 1, 2
from os import stat

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_req_map = defaultdict(set)
        seen = set()
        no_pre_reqs = set(range(numCourses))
        
        state = {c: UNVISITED for c in range(numCourses)}

        for b, a in prerequisites:
            pre_req_map[a].add(b)
            no_pre_reqs.discard(b)
        
        def dfs(course):
            if state[course] == ACTIVE:
                return False
            
            if state[course] == VISITED:
                return True

            state[course] = ACTIVE
            for next_course in pre_req_map.get(course, []):
                if not dfs(next_course):
                    return False
            state[course] = VISITED
            return True

        for course in no_pre_reqs:
            if not dfs(course):
                return False
        
        return all(state[course] == VISITED for course in range(numCourses))