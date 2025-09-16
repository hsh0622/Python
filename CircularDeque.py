from CircularQueue import *

class CircularDeque(CircularQueue):
    def __init__(self, capcity=10):
        super().__init__(capcity)

    def addRear(self, item):
        self.enqueue(item)

    def deleteFront(self):
        return self.dequeue()
    
    def getFront(self):
        return self.peek()
    
    def addFront(self, item):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else: pass
    
    def deleteRear(self):
        if not self.isEmpty():
            item = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item
        else: pass

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else: pass

if __name__ == "__main__":
    dq = CircularDeque()

    for i in range(9):
        if i%2==0 : dq.addRear(i)
        else : dq.addFront(i)
    print("홀수->전단, 짝수->후단:", dq)

    for i in range(2): dq.deleteFront()
    for i in range(3): dq.deleteRear()
    print(" 전단삭제x2 후단삭제x3:", dq)

    for i in range(9,14): dq.addFront(i)
    print("   전단삽입 9,10,...13:", dq)