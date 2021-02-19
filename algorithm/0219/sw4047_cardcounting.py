import sys
sys.stdin = open('cardcounting.txt', 'r')


color = ['S','D','H','C']
def Count():
    for i in range(0,len(arr),3):
        for j in range(len(color)):
            if arr[i] == color[j] :
                if arr[i+1] == '0':
                    cnt = int(arr[i+2]) -1
                else :
                    cnt = 10 + int(arr[i+2]) -1

                if card_count[j][cnt] != 0:
                    return 'ERROR'
                else :
                    card_count[j][cnt] += 1

T = int(input())
for tc in range(1,T+1):
    arr = list(input())
    card_count = list([0]*13 for _ in range(4))
    result = Count()
    print('#{}'.format(tc),end=' ')
    if result == 'ERROR':
        print(result)
    else :
        data = []
        for i in range(4):
            count = 13
            count -= sum(card_count[i])
            data.append(count)
        print(*data)