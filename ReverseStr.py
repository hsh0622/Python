from ArrayStack import ArrayStack

s = ArrayStack(50)

msg = input("문자열 입력: ")
for c in msg:
    s.push(msg)

print("문자열 출력: ", end="")
while not s.isEmpty():
    print(s.pop(), end="")
print()