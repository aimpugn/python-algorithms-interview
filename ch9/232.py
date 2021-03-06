class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self._lenth = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        self._lenth += 1
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
           return None
        self._lenth -= 1

        return self.stack.pop(0)

        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
           return None
        
        return self.stack[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self._lenth == 0

        
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()