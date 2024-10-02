import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a=list(map(str,input().strip().split()))
    for i in a:
        print(i[::-1],end=' ')
    print()