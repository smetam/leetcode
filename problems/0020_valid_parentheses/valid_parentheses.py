class Solution:
    def isValid(self, s: str) -> bool:
        matching = {'(': ')', '[': ']', '{': '}'}
        closing = set(matching.values())
        stack = []
        for bracket in s:
            if bracket in closing:
                if len(stack) < 1:
                    return False
                last_opened = stack.pop()
                if matching[last_opened] != bracket:
                    return False
            else:
                stack.append(bracket)
        return len(stack) == 0
