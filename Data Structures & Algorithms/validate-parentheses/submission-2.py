class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for b in s:
            if b in {"{","[","("}:
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                if b == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                if b == ")" :
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                if b == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
