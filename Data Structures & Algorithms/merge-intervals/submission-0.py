class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #go through each element pair, if end >= to next element start then first element start paired with next element end. then compare that pair end with next elemetn start. oh yeah need to sort everything first
        intervals.sort(key=lambda x: x[0])
        res=[intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            if start <= lastEnd:
                res[-1][1] = max(end, lastEnd)
            else:
                res.append([start, end])
        return res