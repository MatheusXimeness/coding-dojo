# 1 STEP 
#   - Treat the entry
# 2 STEP 
#   - Create the construtor
# 3 STEP 
#   - implement the push - adds an element
# 4 STEP 
#   - Implement the pop - remove from the top
# 5 STEP 
#   - Implement the top - get the last element
# 6 STEP 
#   - Implement the getMin - return the minimun element

class MinStack(object):

    def __init__(self):
        self.my_stack = []

    def push(self, value):
        if self.my_stack:
           self.my_stack.append((value, min(value, self.my_stack[-1][1])))
        else:
            self.my_stack.append((value, value))

    def pop(self):
        if self.my_stack:
            self.my_stack.pop()
        return None

    def top(self):
        if self.my_stack:
            return self.my_stack[-1][0]
        return None

    def getMin(self):
        if self.my_stack:
            return self.my_stack[-1][1]

my_stack = MinStack()
print(my_stack.push(-2))
print(my_stack.push(0))
print(my_stack.push(-3))
print(my_stack.getMin())
print(my_stack.pop())
print(my_stack.top())
print(my_stack.getMin())