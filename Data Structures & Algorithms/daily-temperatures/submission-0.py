class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            count = 1
            j = i + 1

            while j < len(temperatures):
                if temperatures[j] > n:
                    res[i] = count
                    break
                j += 1
                count += 1

        return res