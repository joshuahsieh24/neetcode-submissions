class Solution:
    def isValid(self, s: str) -> bool:
        sol = {'}': '{', ']': '[', ')': '('}
        stack = []

        for char in s:
            
            if char in sol:
                if not stack or stack[-1]!=sol[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
            
        return not stack
                


      