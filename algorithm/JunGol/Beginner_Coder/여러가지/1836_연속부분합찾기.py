# N개의 정수를 담고 있는 배열이 주어졌을 때,
#
# 여기서 가능한 연속 부분합의 최댓값을 구하는 프로그램을 작성하라.
#
#
#
# 여기서 연속 부분합이라는 것은 배열에서 연속된 숫자들을 선택해서 합하였을 때의 값을 말한다.
#
# 아무 배열도 택하지 않는 경우도 연속 부분합에 포함됨을 유의하자.
N = int(input())
temp = list(map(int,input().split()))
ans = 0
num = 0
for i in temp:
    if num > 0 : num += i
    else:
        num = i
    if ans < num:
        ans = num
print(ans)