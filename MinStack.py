# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) - Push element x onto stack.
# pop() - Removes the element on top of the stack.
# top() - Get the top element.
# getMin() - Retrieve the minimum element in the stack.
# Note that all the operations have to be constant time operations.
#
# Questions to ask the interviewer :
#
# Q: What should getMin() do on empty stack?
# A: In this case, return -1.
#
# Q: What should pop do on empty stack?
# A: In this case, nothing.
#
# Q: What should top() do on empty stack?
# A: In this case, return -1

class MinStack:
    def __init__(self):
        self.s = []
        self.mins = []
        self.min = 2**31-1
        
    # @param x, an integer
    def push(self, x):
        self.s.append(x)
        if self.min >= x:
            self.mins.append(self.min)
            self.min = x

    # @return nothing
    def pop(self):
        if len(self.s) > 0: 
            if self.top() == self.min: 
                self.min = self.mins.pop() if len(self.mins) > 0 else -1
            return self.s.pop()

    # @return an integer
    def top(self):
        return self.s[-1] if len(self.s) > 0 else -1

    # @return an integer
    def getMin(self):
        return self.min if len(self.s) > 0 else -1