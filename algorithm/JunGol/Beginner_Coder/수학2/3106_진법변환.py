# A진법 수 N을 입력 받아 B진법 수로 출력하는 프로그램을 작성하시오.
#
# N에 사용되는 값은 0 ~ 9, A ~ Z이다.
#
# (2 ≤ A, B ≤​ 36) ( 0≤​ N≤​ 263-1 )
def change10(n):
    ans = 0
    nl = len(n)
    for i in range(nl-1,-1,-1):
        if n[i] <= '9':
            ans += int(n[i]) * (A ** (nl - 1 - i))
        else:
            ans += (ord(n[i]) - 55) * (A ** (nl - 1 - i))
    return ans

def changeResult(num):
    temp = []
    while num > 0 :
        if num % B < 10:
            temp.append(int(num % B))
        else:
            temp.append(chr(int(num % B) + 55))
        # 파이썬 float는 15자리까지 가능 16자리넘어가면안됨
        # int(num / B)는 불가
        num = num // B
    if temp:
        return temp
    return [0]

while True:
    tc = input()
    if tc == '0':
        break
    A, N, B = tc.split()
    A, B = int(A), int(B)
    result = changeResult(change10(N))
    result.reverse()
    for i in result:
        print(i,end='')
    print()
