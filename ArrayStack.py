class ArrayStack :
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity-1
    
    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
        else:
            print("stack overflow")

    def pop(self):
        if not self.isEmpty():
            item = self.array[self.top]
            self.top -= 1
            return item
        else:
            print("stack underflow")

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print("stack underflow")

    def __str__(self):
        return str(self.array[0:self.top+1])

# s = ArrayStack(10)
# for i in range(1,6):
#     s.push(i)
# print("push 5회:", s)
# print("push 5회:", s.array)