import sys
sys.stdin = open('sw_4880_토너먼트카드게임_input.txt','r')

def Game(s,e):
    if s == e:
        return s
    first_win = Game(s,(s+e)//2)
    second_win = Game((s+e)//2+1,e)
    return Game2(first_win,second_win)


# 가위바위보
def Game2(x,y):
    a, b = arr[x-1], arr[y-1]
    if a == b:
        return x
    elif a == 1 and b == 3:
        return x
    elif a == 2 and b == 1:
        return x
    elif a == 3 and b == 2:
        return x
    else:
        return y

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    start = 1
    end = N
    ans = Game(start,end)
    print('#{} {}'.format(tc,ans))