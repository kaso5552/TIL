import sys
sys.stdin = open('sw_1242_암호코드스캔_input.txt', 'r')
# sys.stdin = open('input.txt', 'r')
num = {
    '3211': '0', '2221': '1', '2122': '2', '1411': '3', '1132': '4',
    '1231': '5', '1114': '6', '1312': '7', '1213': '8', '3112': '9',
}
num16 = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    data = [input() for _ in range(N)]
    se = []
    result = []
    result_num2 = []
    ans  = 0
    for i in range(N-1,-1,-1):
        sy = 9999999
        for j in range(M-1,-1,-1):
            if data[i][j] != '0' :
                if data[i+1][j] == '0' and j < sy:
                    ex = i
                    ey = j
                    sx = i
                    sy = j
                    while data[sx][ey] != '0':
                        sx -= 1
                    sx += 1
                    while ey >= 0:
                        if data[sx][ey] != data[ex][ey] or data[ex + 1][ey] != '0' or data[sx - 1][ey] != '0':
                            break
                        if data[sx][ey] != '0' and data[sx-1][ey] == '0':
                            sy = ey
                        ey -= 1
                    se.append([sx,sy,j])
    for i in se:
        num2 = data[i[0]][i[1]:i[2]+1]
        result_num2 = []
        for j in num2:
            result_num2.append(num16[j])
        f_num2 = ''.join(result_num2)
        count = len(f_num2)//56
        if len(f_num2) % 56 >= 40:
            count += 1
        result_num = []
        result = []
        for j in range(len(f_num2)-1,-1,-1):
            if f_num2[j] == '1':
                while True:
                    length = count * 7
                    start = j - 55 * count - (count-1)
                    while start < 0 :
                        f_num2 = '0' + f_num2
                        start += 1
                    sample_0 = 0
                    sample_1 = 0
                    result_num = []
                    for k in range(start,len(f_num2)-1):
                        if f_num2[k] == '0' :
                            sample_0 += 1
                            if f_num2[k+1] == '1':
                                result_num.append(str(int(sample_0/count)))
                                sample_0 = 0
                        elif f_num2[k] == '1':
                            sample_1 += 1
                            if f_num2[k+1] == '0':
                                result_num.append(str(int(sample_1/count)))
                                sample_1 = 0
                    result_num.append(str(int((sample_1+1)/count)))
                    for k in range(0,32,4):
                        result.append(int(num[''.join(result_num[k:k+4])]))
                    number = (result[0] + result[2] + result[4] + result[6]) * 3 + (
                                result[1] + result[3] + result[5] + result[7])
                    if number % 10 == 0:
                        ans += sum(result)
                    break
                break
    print('#{} {}'.format(tc,ans))


