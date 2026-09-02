class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []
        intervals = sorted(intervals)
        current = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= current[1]:
                current[1] = max(interval[1], current[1])
            else:
                results.append(current)
                current = interval
        
        results.append(current)
        return results