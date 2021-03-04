import sys
sys.stdin = open('sw_5099_피자굽기_input.txt', 'r')

def enQueue(item,m):
    global rear
    rear = (rear+1) % m
    Q[rear] = item

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    Ci = list(map(int,input().split()))
    data = []
    Q = []
    # 피자번호와 치즈양을 함께 data에 저장한다
    for idx,ci in enumerate(Ci):
        data.append((idx+1,ci))
    # 처음에 피자를 N(화덕안의 피자 최대갯수) 를 넣는다
    for i in range(N):
        Q.append((data[i][0],data[i][1]//2))
    front = -1
    # 지금 마지막으로 들어간 피자번호
    count = N
    # 화덕에 피자를 넣는것을 반복
    while True:
        m = len(Q)
        front = (front + 1) % m
        cheese = Q[front][1]
        if cheese != 0:
            Q[front] = (Q[front][0], cheese // 2)
        elif cheese == 0:
            # 남은 피자가 있다면
            if count < M :
                Q[front] = (data[count][0],data[count][1]//2) # 피자를 꺼내고 그자리에 다음피자 추가
                count += 1 # 남은 피자번호 +1
            # 남은피자가 없다면
            else:
                Q.pop(front) # 피자를 꺼내고
                front -= 1
                if m-1 == 1: # 화덕안에 피자가 1개 남은지 확인
                    break

    print('#{} {}'.format(tc,Q[0][0]))