# 선택 정렬(selection sort)이란 내부정렬 알고리즘의 하나로 다음 순서대로 실행하여 정렬을 한다.
#
#
#
# 1. 주어진 수열 중에 최소값(같은 값이 여러 개 있는 경우 처음 값)을 찾는다.
#
# 2. 찾은 최소값을 맨 앞의 값과 자리를 바꾼다.
#
# 3. 맨 앞의 값을 뺀 나머지 수열을 같은 방법으로 전체 개수-1번 반복 실행한다.
#
#
#
# n개의 주어진 수열을 위와 같은 방법으로 정렬한다.
#
#
#
# 수열이 주어지면 선택정렬의 과정을 한 단계씩 출력한다.​

N = int(input())
temp = list(map(int,input().split()))
for i in range(N-1):
    num = temp[i]
    num_idx = i
    for j in range(i,N):
        if num > temp[j]:
            num = temp[j]
            num_idx = j

    temp[i], temp[num_idx] = temp[num_idx], temp[i]
    for i in range(N):
        print(temp[i],end=' ')
    print()