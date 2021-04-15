import sys
sys.stdin = open('sw_11767_베이비진게임_input.txt', 'r')


T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    player = [[0] * 10 for _ in range(3)]
    ans = 0
    game_count = 0
    count = 1
    while arr:
        game_count += 1
        card = arr.pop(0)
        player[count][card] += 1

        if game_count >= 5 :
            for j in range(10):
                if j <= 7:
                    if player[count][j] >=1 and player[count][j+1] and player[count][j+2] >=1:
                        ans = count
                        break
                if player[count][j] == 3:
                    ans = count
                    break
        if ans != 0:
            break
        if count == 1:
            count = 2
        else:
            count = 1

    print('#{} {}'.format(tc, ans))

