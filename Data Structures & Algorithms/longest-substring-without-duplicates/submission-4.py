class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            seen = set()
            l = 0
            maxCount = 0
            for r in range(len(s)):
                while(s[r] in seen):
                    seen.remove(s[l])
                    l+=1
                seen.add(s[r])
                maxCount = max(maxCount, r - l + 1)

            return maxCount

                
