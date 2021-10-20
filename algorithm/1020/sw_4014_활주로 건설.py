import sys
sys.stdin = open('sw_4014_활주로 건설_input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, X = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        # 가로줄 체크
        height = arr[i][0]
        is_check = 1
        visited = [0] * N
        for j in range(1, N):
            # 같은 높이 일때
            if height == arr[i][j]:
                continue
            # 1. 현재높이보다 1 높은 곳을 만났을때
            if height + 1 == arr[i][j]:
                for k in range(j-1, j-X-1, -1):
                    if 0 <= k < N and arr[i][k] == height and visited[k] == 0:
                        visited[k] = 1
                    else:
                        is_check = 0
                        break
                if is_check:
                    height = arr[i][j]
                else:
                    break

            # 2. 현재높이보다 1 낮은 곳을 만났을때
            elif height == arr[i][j] + 1:
                for k in range(j,j+X):
                    if 0 <= k < N and arr[i][k] == height - 1 and visited[k] == 0:
                        visited[k] = 1
                    else:
                        is_check = 0
                        break

                if is_check:
                    height = arr[i][j]
                else:
                    break
            else:
                is_check = 0
                break

        # 무사히 건설 했으면
        if is_check:
            ans += 1

        # 세로줄 체크
        height = arr[0][i]
        is_check = 1
        visited = [0] * N
        for j in range(1, N):
            if height == arr[j][i]:
                continue
            # 1. 현재높이보다 1 높은 곳을 만났을때
            if height + 1 == arr[j][i]:
                for k in range(j-1, j-X-1, -1):
                    if 0 <= k < N and arr[k][i] == height and visited[k] == 0:
                        visited[k] = 1
                    else:
                        is_check = 0
                        break
                if is_check:
                    height = arr[j][i]
                else:
                    break

            # 2. 현재높이보다 1 낮은 곳을 만났을때
            elif height == arr[j][i] + 1:
                for k in range(j,j+X):
                    if 0 <= k < N and arr[k][i] == height - 1 and visited[k] == 0:
                        visited[k] = 1
                    else:
                        is_check = 0
                        break

                if is_check:
                    height = arr[j][i]
                else:
                    break
            else:
                is_check = 0
                break

        # 무사히 건설 했으면
        if is_check:
            ans += 1




    print(f'#{tc} {ans}')