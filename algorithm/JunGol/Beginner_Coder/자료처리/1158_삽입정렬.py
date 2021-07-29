# 삽입정렬(Insertion sort)은 자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여,
#
# 자신의 위치를 찾아 삽입하는 방법이다.
#
#
#
#
# 수열이 {5 4 3 7 6}이 있을 경우의 삽입정렬 과정은 다음과 같다.
#
# 처음상태에서 처음 값 5 앞에 아무것도 없으므로 5는 이미 정렬된 상태가 되므로, 이후 4부터 정렬과정을 살펴보자.
#
#
#
#
#
#
#
# ※ 3단계의 경우 7은 앞의 "3 4 5"보다 크므로 제자리에 삽입된다.
#
#
# n개의 수열이 주어지면 위와 같은 방법으로 정렬하는 과정 각 단계를 출력하는 프로그램을 작성하시오.

N = int(input())
temp = list(map(int,input().split()))
for i in range(1,N):
    for j in range(i):
        if temp[i] < temp[j]:
            temp[i], temp[j] = temp[j], temp[i]
    for i in range(N):
        print(temp[i],end=' ')
    print()
