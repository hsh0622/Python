capacity = 100
array = [None] * capacity
size = 0

def isEmpty():
    if size == 0:
        return True
    else:
        return False

def isFull():
    if size == capacity:
        return True
    else:
        return False

def insert(pos, e):
    global size
    if not isFull() and 0 <= pos <= size:
        for i in range(size, pos, -1):
            array[i] = array[i - 1]
        array[pos] = e
        size += 1
    else:
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()

def delete(pos):
    global size
    if not isEmpty() and 0 <= pos < size:
        e = array[pos]
        for i in range(pos, size - 1):
            array[i] = array[i + 1]
        size -= 1
        return e
    else:
        print("리스트 underflow 또는 유효하지 않은 삭제 위치")
        exit()

if __name__ == "__main__":
    print("최초", array[0:size])
    insert(0, 10)
    insert(0, 20)
    insert(1, 30)
    insert(size, 40)
    insert(2, 50)
    print("삽입x5", array[0:size])
    delete(2)
    print("삭제(2)", array[0:size])
    delete(size-1)
    print("삭제(E)", array[0:size])
    delete(0)
    print("삭제(0)", array[0:size])
