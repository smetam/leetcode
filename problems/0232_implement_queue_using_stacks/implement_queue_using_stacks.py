class Stack:
    def __init__(self) -> None:
        self._stack = []

    def push(self, elem: int) -> None:
        self._stack.append(elem)

    def pop(self) -> int:
        if self.empty():
            return None
        return self._stack.pop()

    def peek(self) -> int:
        if self.empty():
            return None
        return self._stack[-1]
        
    def empty(self) -> bool:
        return len(self._stack) == 0


class MyQueue:

    def __init__(self):
        self._stack = Stack()
        self._q = Stack()
        
    def push(self, x: int) -> None:
        self._stack.push(x)

    def _stack_to_q(self):
        if not self._q.empty():
            return
        while not self._stack.empty():
            elem = self._stack.pop()
            self._q.push(elem)

    def pop(self) -> int:
        self._stack_to_q()
        if self._q.empty():
            return None
        return self._q.pop()

    def peek(self) -> int:
        self._stack_to_q()
        if self._q.empty():
            return None
        return self._q.peek()
        
    def empty(self) -> bool:
        return self._q.empty() and self._stack.empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()