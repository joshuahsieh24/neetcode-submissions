class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        sum = 0
        for i, n in enumerate(numbers):
            sum = target - n
            if sum in map:
                return [map[sum]+1, i+1]
            map[n]=i
        
        return []
        