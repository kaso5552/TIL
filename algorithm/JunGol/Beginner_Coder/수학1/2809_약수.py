# 한 개의 정수를 입력받아 입력받은 정수의 약수를 모두 출력하는 프로그램을 작성하시오.

# 정수 N이 주어진다. (2 ≤ N ≤ 21억)

# 시간초과 조심

import math

N = int(input())
sq = int(math.sqrt(N))
ans = []
for i in range(1, sq+1):
    if N % i == 0:
        ans.append(i)
        if (N / i != i) :
            ans.append(int(N / i))

for i in sorted(ans):
    print(i, end=' ')