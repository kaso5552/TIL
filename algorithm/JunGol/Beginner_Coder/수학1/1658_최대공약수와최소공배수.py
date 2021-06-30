# 두개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

A, B = map(int,input().split())
if A < B :
    A, B = B, A

ans1 = 0
for i in range(1, B+1):
    if A % i == 0 and B % i == 0:
        ans1 = i

print(ans1)

cntA = 1
cntB = 1

while True:
    if (B * cntB) < (A * cntA):
        cntB += 1
    elif (B * cntB) == (A * cntA):
        print(A * cntA)
        break
    else:
        cntA += 1
