import sys
sys.stdin = open('sw_1240_단순2진암호코드_input.txt', 'r')

num = {
    '0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
    '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9',
}

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    data = [input() for _ in range(N)]
    result = []
    sx = 0
    sy = 0
    for i in range(N-1,-1,-1):
        for j in range(M-1,-1,-1):
            if data[i][j] == '1' :
                sx = i
                sy = j - 55
                break
        if sx != 0:
            break

    for i in range(8):
        start = sy
        end = sy + 7
        result.append(int(num[data[sx][start:end]]))
        sy += 7
    number = (result[0]+result[2]+result[4]+result[6])*3 + (result[1]+result[3]+result[5]+result[7])
    if number % 10 == 0:
        ans = sum(result)
    else:
        ans = 0
    print('#{} {}'.format(tc,ans))