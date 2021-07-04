for i in range(int(input())):
    n=int(input())
    if n&not(n&(n-1)):
        print('YES')
    else:
        print('NO')
