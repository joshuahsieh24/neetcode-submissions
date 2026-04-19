class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for num in tokens:
            if(num == "+"):
                stack.append(stack.pop() + stack.pop())
            elif num == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif num == "*":
                stack.append(stack.pop() * stack.pop())
            elif num == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(num))
        return stack[0]

