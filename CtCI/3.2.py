class MinStack:
    def __init__(s):
        s.stack = []
        s.minStack = []

    def push(s, val):
        if len(s.minStack) == 0:
            s.minStack.append(val)
        else:
            s.minStack.append(s.minStack[-1] if s.minStack[-1] < val else val)
        s.stack.append(val)

    def pop(s):
        if len(s.stack) == 0: return None
        s.minStack.pop()
        return s.stack.pop()

    def getMin(s):
        return s.minStack[-1] if len(s.minStack) > 0 else None

stack = MinStack()
stack.push(20)
print stack.getMin()
stack.push(12)
print stack.getMin()
stack.push(3)
print stack.getMin()
stack.push(14)
print stack.getMin()
stack.pop()
print stack.getMin()
stack.pop()
print stack.getMin()
stack.push(2)
stack.push(3)
print stack.getMin()
stack.pop()
print stack.getMin()
