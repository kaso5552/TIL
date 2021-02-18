import sys
sys.stdin = open('iron_stick.txt', 'r')

def Count(arr):
    # 레이저를 만나면 레이저 끝나고부터 다시 보기
    number = 0
    # while문 빠져나가기 용
    count = 0
    # 지금레이저를 쏠때 밑에 있는 철판의 갯수
    iron_count = 0
    # 최종 분할된철판갯수
    result = 0
    while True:
        for i in range(number,len(arr)-1):
            count = i
            # 레이저 쏘는 번호
            if arr[i:i+2] == '()':
                number = i+2
                count = i+1
                result += iron_count
                break
            # 여는거
            elif arr[i] == '(':
                iron_count += 1
            # 닫는거
            else:
                iron_count -= 1
                result += 1
        if count == len(arr)-2:
            result += iron_count
            break
    return result


T = int(input())
for tc in range(1,T+1):
    arr = input()
    result = Count(arr)
    print('#{} {}'.format(tc,result))
