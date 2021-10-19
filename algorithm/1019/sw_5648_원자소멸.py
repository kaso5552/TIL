import sys
sys.stdin = open('sw_5648_원자소멸_input.txt', 'r')

# 원자가 이동하는 라인체크
# S 는 멈춰있는거 U은 상승 D는 다운
def check_line():
    cnt = 0
    for atom in atoms:
        if atom[2] == 0:
            x, y = '{}S'.format(atom[0]), '{}U'.format(atom[1])
        elif atom[2] == 1:
            x, y = '{}S'.format(atom[0]), '{}D'.format(atom[1])
        elif atom[2] == 2:
            x, y = '{}D'.format(atom[0]), '{}S'.format(atom[1])
        else:
            x, y = '{}U'.format(atom[0]), '{}S'.format(atom[1])

        lines[cnt] = [x, y, atom[3]]
        cnt += 1

def check_crash():
    for idx, line in enumerate(lines):
        x, y, E = line[0], line[1], line[2]
        for i in range(idx+1, N):
            nx, ny ,nE = lines[i][0], lines[i][1], lines[i][2]

            if x[-1] == 'S':
                if nx[-1] != 'S':
                    if y[-1] == 'U' and int(y[0:-1]) >= int(ny[0:-1]):
                        continue
                    elif y[-1] == 'D' and int(y[0:-1]) <= int(ny[0:-1]):
                        continue

                    cx, cy = int(x[0:-1]), int(ny[0:-1])
                    if abs(int(y[0: -1]) - cy) == abs(int(nx[0: -1]) - cx):
                        if int(nx[0: -1]) < cx and nx[-1] == 'U':
                            crashed.append([idx, i, abs(int(y[0: -1]) - cy)])
                        elif int(nx[0: -1]) > cx and nx[-1] == 'D':
                            crashed.append([idx, i, abs(int(y[0: -1]) - cy)])

                elif x[0:-1] == nx[0:-1]:
                    if y[-1] != ny[-1]:
                        if int(y[0:-1]) > int(ny[0:-1]):
                            if y[-1] == 'D':
                                crashed.append([idx, i, abs(int(y[0:-1]) - int(ny[0:-1]))/2])
                        else:
                            if ny[-1] == 'D':
                                crashed.append([idx, i, abs(int(y[0:-1]) - int(ny[0:-1]))/2])

            elif y[-1] == 'S':
                if ny[-1] != 'S':
                    if x[-1] == 'U' and int(x[0:-1]) > int(nx[0:-1]):
                        continue
                    elif x[-1] == 'D' and int(x[0:-1]) < int(nx[0:-1]):
                        continue

                    cx, cy = int(nx[0:-1]), int(y[0:-1])
                    if abs(int(ny[0: -1]) - cy) == abs(int(x[0: -1]) - cx):
                        if int(ny[0: -1]) < cy and ny[-1] == 'U':
                            crashed.append([idx, i, abs(int(ny[0: -1]) - cy)])
                        elif int(ny[0: -1]) > cy and ny[-1] == 'D':
                            crashed.append([idx, i, abs(int(ny[0: -1]) - cy)])

                elif y[0:-1] == ny[0:-1]:
                    if x[-1] != nx[-1]:
                        if int(x[0:-1]) > int(nx[0:-1]):
                            if x[-1] == 'D':
                                crashed.append([idx, i, abs(int(x[0:-1]) - int(nx[0:-1]))/2])
                        else:
                            if nx[-1] == 'D':
                                crashed.append([idx, i, abs(int(x[0:-1]) - int(nx[0:-1]))/2])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atoms = [list(map(int,input().split())) for _ in range(N)]
    lines = [[0] for _ in range(N)]
    state = [0] * N
    visited = [0] * N
    crashed = []
    ans = 0
    check_line()


    check_crash()
    crashed.sort(key=lambda x:x[2])

    for crash in crashed:
        a, b, t = crash[0], crash[1], crash[2]
        if state[a] == 0 and state[b] == 0:
            pass
        elif state[a] == t and state[b] == 0:
            pass
        elif state[a] == 0 and state[b] == t:
            pass
        else:
            continue
        state[a], state[b] = t, t
        if visited[a] == 0:
            ans += atoms[a][-1]
            visited[a] = 1
        if visited[b] == 0:
            ans += atoms[b][-1]
            visited[b] = 1

    print('#{} {}'.format(tc,ans))



