import sys
sys.stdin = open('sw_5658_보물상자비밀번호_input.txt', "r")

def change():
    for i in range(4):
        result = 0
        for j in range(lenght):
            if temp_list[i][lenght - j - 1] <= '9':
                result += 16 ** j * int(temp_list[i][lenght - j - 1])
            else:
                temp = ord(temp_list[i][lenght - j - 1]) - 55
                result += 16 ** j * temp
        if result in total:
            continue
        total.append(result)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    num_list = list(input())
    # 회전용
    temp_list = []
    total = []
    lenght = int(N / 4)

    for i in range(4):
        temp = i * lenght
        temp_list.append(num_list[temp:temp+lenght])
    change()

    for i in range(lenght - 1):
        num = [temp_list[j][-1] for j in range(4)]
        for j in range(4):
            if j == 0:
                temp_list[j] = [num[-1]] + temp_list[j][0:lenght - 1]
            else:
                temp_list[j] = [num[j - 1]] + temp_list[j][0:lenght - 1]
        change()
    print(f'#{tc} {sorted(total, reverse=True)[K-1]}')