# Notes picture the numbers flowing in and out.
# You bassically have one empty stack at all times

class MyQueue(object):

    def __init__(self):
        self.stackLeft = []
        self.stackRight = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.stackRight.append(x)

        

    def pop(self):
        """
        :rtype: int
        """
        self.move()

        return self.stackLeft.pop()
        
        

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.stackLeft[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stackLeft) == 0 and len(self.stackRight) == 0
        
    def move(self):
        if not self.stackLeft:
            while self.stackRight:
                self.stackLeft.append(self.stackRight.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()