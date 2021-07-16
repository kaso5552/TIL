# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다.
#
# 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다.
#
# 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 둘레의 길이를 구하는 프로그램을 작성하시오.
#
#
#
# 예를 들어 흰색 도화지 위에 네 장의 검은색 색종이를 <그림 1>과 같은 모양으로 붙였다면 검은색 영역의 둘레는 96 이 된다.

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def fill(x, y):
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

arr = [[0 for _ in range(100)]for _ in range(100)]
N = int(input())
ans = 0
temp = []
for i in range(N):
    a, b = map(int,input().split())
    fill(a, b)

# 완전탐색
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            for z in range(4):
                ni = i + dx[z]
                nj = j + dy[z]
                if 0 <= ni <= 99 and 0 <= nj <= 99 and arr[ni][nj] == 1:
                    continue
                ans += 1
print(ans)