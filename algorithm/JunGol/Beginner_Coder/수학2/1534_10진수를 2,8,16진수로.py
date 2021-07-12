# 10진수를 입력 받아서 2, 8, 16진수로 바꾸어 출력하는 프로그램을 작성하시오.

# 입력의 첫줄에는 10진수 N(1≤N≤100,000)과 바꿀 진수 B(2, 8, 16)가 공백으로 구분하여 입력된다.
#
# 16진수에서 10이상의 수는 순서대로 'A', 'B', 'C', 'D', 'E', 'F'로 나타낸다.

# 입력받은 10진수를 B진수로 바꾸어 출력한다.

N, A = map(int,input().split())
data = {10 : 'A', 11 : 'B', 12: 'C', 13 : 'D', 14: 'E', 15 : 'F'}
ans = []
while N > 0 :
    if N % A < 10 :
        ans.append(N % A)
    else:
        ans.append(data[N % A])
    N = int(N / A)

for i in range(len(ans)-1,-1,-1):
    print(ans[i],end='')