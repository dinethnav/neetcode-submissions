class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def do_math(operator):
            a = stack.pop()
            b = stack.pop()
            c = 0

            # print(stack)

            if operator == "+":
                c = a+b
            
            if operator == "*":
                c = a*b
            
            if operator == "-":
                c = b-a
            
            if operator == "/":
                c = int(b/a)
            stack.append(c)
            # print(a,b,c,stack)


        for i in tokens:
            if i not in {'+', '-', '*', '/'}:
                stack.append(int(i))
            else:
                do_math(i)
        
        return stack[-1]
            
        