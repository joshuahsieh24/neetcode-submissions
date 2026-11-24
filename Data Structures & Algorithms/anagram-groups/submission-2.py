class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            group[sortedS].append(s)
        
        return list(group.values())
