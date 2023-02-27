class Solution:

    # "3[a]2[bc]" -> "aaabcbc"
    def decodeString(self, s: str) -> str:
        k_stack = list()
        c_stack = list()
        k = 0
        c = ''
        for sym in s:
            if sym.isnumeric():
                k = k * 10 + int(sym)
            elif sym.isalpha():
                c += sym
            elif sym == '[':
                k_stack.append(k)
                c_stack.append(c)
                k = 0
                c = ''
            elif sym == ']':
                c = c_stack.pop() + c * k_stack.pop()
        return c
                
            


            