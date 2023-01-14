class Solution:
    def interpret(self, command: str) -> str:
        # solution with replace
        return command.replace("()", "o").replace('(al)', 'al')
        
        # sloution without replace
        # res = []
        # for elem in command:
        #     if elem == ')':
        #         prev = res.pop()
        #         if prev == '(':
        #             res.append('o')
        #         else:
        #             res[-2] = 'a'
        #             res[-1] = 'l'
        #     else:
        #         res.append(elem)
        # return ''.join(res)