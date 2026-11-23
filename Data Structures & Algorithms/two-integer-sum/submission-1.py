class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, n in enumerate(nums):
            result = target - n
            if result in temp:
                return [temp[result], i]
            temp[n]=i