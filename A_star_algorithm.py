import queue  # 파이썬에서 제공하는 큐(줄 서기) 기능을 불러옴

# 퍼즐의 시작 상태 (리스트로 3x3 퍼즐 표현)
start = [1, 4, 2,
         8, 6, 3,
         7, 0, 5]

# 퍼즐의 목표 상태 (이 모양을 만들면 성공)
goal = [1, 2, 3,
        8, 0, 4,
        7, 6, 5]

# 상태(퍼즐의 모양과 정보)를 담는 틀 만들기
class State :
    # 새로운 퍼즐 상태를 만들 때 필요한 값들을 저장
    def __init__(self, board, goal, depth = 0):
        self.board = board   # 현재 퍼즐 모양
        self.depth = depth   # 지금까지 몇 번 움직였는지
        self.goal = goal     # 맞추어야 할 목표 모양

    # i1과 i2 위치의 숫자를 서로 바꿔서 새로운 퍼즐 만들기
    def get_new_board(self,i1,i2,depth):
        new_board = self.board[:]   # 현재 퍼즐을 복사
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]  # 두 자리 바꾸기
        return State(new_board, self.goal, depth)  # 바꾼 퍼즐로 새 상태 만들기
    
    # 빈칸(0)을 움직여서 갈 수 있는 모든 새로운 퍼즐 상태 만들기
    def expand(self, moves):
        result = []                # 새 퍼즐들을 담을 리스트
        i = self.board.index(0)    # 빈칸(0)이 어디 있는지 찾기

        # 왼쪽으로 이동 가능한 경우
        if not i in [0, 3, 6]: 
            result.append(self.get_new_board(i, i - 1, moves))

        # 오른쪽으로 이동 가능한 경우
        if not i in [2, 5, 8]:
            result.append(self.get_new_board(i, i + 1, moves))

        # 위쪽으로 이동 가능한 경우
        if not i in [0, 1, 2]:
            result.append(self.get_new_board(i, i - 3, moves))

        # 아래쪽으로 이동 가능한 경우
        if not i in [6, 7, 8]:
            result.append(self.get_new_board(i, i + 3, moves))

        return result   # 만들어진 새 퍼즐들 돌려주기
    
    # 점수를 계산: (움직인 횟수 + 잘못 놓인 숫자의 개수)
    def f(self):
        return self.h() + self.g()
    
    # 잘못 놓인 숫자가 몇 개인지 세기 (빈칸 제외)
    def h(self):
        count = 0
        for i in range(9):   # 퍼즐 9칸 확인
            if self.board[i] != 0 and self.board[i] != self.goal[i]:
                count += 1   # 제자리에 없는 숫자면 개수 +1
        return count
    
    # 지금까지 몇 번 움직였는지 돌려주기
    def g(self):
        return self.depth
    
    # 두 퍼즐이 같은 모양인지 확인할 때 사용
    def __eq__(self, other):
        return self.board == other.board
    
    # 두 퍼즐이 다른 모양인지 확인할 때 사용
    def __ne__(self, other):
        return self.board != other.board
    
    # 작은 점수를 가진 퍼즐이 우선순위 큐에서 먼저 나오도록 설정
    def __lt__(self, other):
        return self.f() < other.f()
    
    # 큰 점수를 가진 퍼즐은 나중에 나오도록 설정
    def __gt__(self, other):
        return self.f() > other.f()
    
    # 퍼즐 모양을 보기 좋게 출력할 때 사용
    def __str__(self):
        return f"점수 = {self.f()} 잘못된 위치 = {self.h()} 이동횟수 = {self.g()}\n" + \
                str(self.board[ : 3]) + "\n" + \
                str(self.board[3 : 6]) + "\n" + \
                str(self.board[6 : ]) + "\n"

# 앞으로 확인할 퍼즐 상태들을 저장하는 우선순위 큐 만들기
open_queue = queue.PriorityQueue()  # 우선순위 큐 생성
open_queue.put(State(start, goal))  # 처음 퍼즐 상태를 큐에 넣기

closed_queue = []  # 이미 확인한 퍼즐 상태를 저장
depth = 0
count = 0  # 몇 번 탐색했는지 세기

# 탐색 시작
while not open_queue.empty():         # 아직 볼 퍼즐이 남아 있다면 계속 반복
    current = open_queue.get()        # 점수가 가장 낮은 퍼즐 꺼내기
    count += 1                        # 탐색 횟수 늘리기
    print(count)                      # 몇 번째 탐색인지 출력
    print(current)                    # 퍼즐 상태 출력

    # 퍼즐이 목표 상태와 같다면 성공
    if current.board == goal:
        print("탐색 성공")
        break

    # 빈칸을 움직여서 새로운 퍼즐 상태들을 만든다
    depth = current.depth + 1
    for state in current.expand(depth):
        # 아직 보지 않은 퍼즐이면 큐에 넣기
        if state not in closed_queue and state not in open_queue.queue:
            open_queue.put(state)

    # 현재 퍼즐은 다시 보지 않도록 기록
    closed_queue.append(current)
else:
    # 큐가 비었는데 목표 퍼즐을 못 찾았다면 실패
    print("탐색 실패")