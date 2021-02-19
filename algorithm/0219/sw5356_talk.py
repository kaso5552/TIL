import sys
sys.stdin = open('talk.txt', 'r')

def Talk():
    data = ''
    max_length = 0
    for i in range(5):
        if max_length < len(arr[i]):
            max_length = len(arr[i])
    for i in range(max_length):
        for j in range(5):
            if i >= len(arr[j]):
                continue
            else:
                data += arr[j][i]

    return data

T = int(input())
for tc in range(1,T+1):
    arr = list(input() for _ in range(5))
    ans = Talk()
    print('#{} {}'.format(tc,ans))