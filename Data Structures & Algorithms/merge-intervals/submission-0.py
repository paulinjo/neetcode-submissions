class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        results = []
        current_interval = intervals[0]
        for interval in intervals[1:]:
            s1, e1 = current_interval
            s2, e2 = interval

            if s2 > e1:  # past the end; no longer overlapping
                results.append(current_interval)
                current_interval = interval
                continue

            current_interval = [min(s1, s2), max(e1, e2)]
        results.append(current_interval)
        return results
