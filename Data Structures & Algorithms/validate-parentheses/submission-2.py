class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ans = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in ans:
                if stack and stack[-1] == ans[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False


