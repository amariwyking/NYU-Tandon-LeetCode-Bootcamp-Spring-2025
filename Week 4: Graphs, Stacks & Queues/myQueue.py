from collections import deque

class MyQueue:
    # The limitation here is that I must use a stack in order to implement the queue functions
    # I am allowed the use of two distinct queues

    # A stack is allowed to push to top, peek/pop from the top, track size, and return is empty


    def __init__(self):
        self.length = 0
        self.stack = deque()
        pass


    def push(self, x: int) -> None:
        """
        Pushes element x to the back of the queue
        """

        temp = deque()

        while len(self.stack) > 0:
            temp.append(self.stack.pop())
        
        self.stack.append(x)

        while len(temp) > 0:
            self.stack.append(temp.pop())

        return


    def pop(self) -> int:
        """
        Removes the element from the front of the queue and returns its value
        """

        # Can simply use deque.pop() to remove the item at the front of the queue (top of the stack)
        return self.stack.pop()


    def peek(self) -> int:
        """
        Returns the element at the front of the queue
        """

        return self.stack[-1]


    def empty(self) -> bool:
        """
        Returns true if the queue is empty, false otherwise
        """

        return len(self.stack) == 0