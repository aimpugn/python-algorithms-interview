# https://leetcode.com/problems/implement-stack-using-queues/

from queue import LifoQueue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = LifoQueue()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.que.put(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.que.get()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.que.queue[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.que.qsize() == 0
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.que.queue)
param_2 = obj.pop()
print(param_2)
print(obj.empty())
print(obj.que.queue)

param_3 = obj.top()
print(param_3)
print(obj.que.queue)

# param_4 = obj.empty()