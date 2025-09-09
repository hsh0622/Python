class Node:
    def __init__ (self, elem, next=None):
        self.data = elem
        self.link = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def isFull(self):
        return False
    
    def getNode(self, pos):
        if pos < 0:
            return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
    
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data
        
    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
            elif before.link != None:
                before.link = before.link.link

    def __str__(self):
        arr = []
        node = self.head
        while node is not None:
            arr.append(node.data)
            node = node.link
        return str(arr)
    
if __name__ == "__main__":
    L = LinkedList()

    print("최초", L)
    L.insert(0, 10)
    L.insert(0, 20)
    L.insert(1, 30)
    L.insert(3,40)
    L.insert(2,50)
    print("삽입x5", L)
    print("연결리스트 3번째 값: ", L.getEntry(3-1))
    L.delete(2)
    print("삭제(2)", L)
    L.delete(3)
    print("삭제(3)", L)
    L.delete(0)
    print("삭제(0)", L)