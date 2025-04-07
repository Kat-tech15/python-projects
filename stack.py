# class MinStack:
def __init__(self):
    self.stack = []
    self.min_stack = []


def push(self, x):
    self.stack.append(x)
    if not self.min_stack or x <= self.min_stack[-1]:
        self.min_stack.append(x)


def pop(self):
    if self.stack.pop() == self.min_stack[-1]:
        self.min_stack.pop()


def top(self):
    return self.stack[-1]


def getMin(self):
    return self.min_stack[-1]


min_stack = MinStack()
min_stack.push(5)
min_stack.push(3)
min_stack.push(7)
print(min_stack.getMin())