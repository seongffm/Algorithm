#문제)
#주어진 N길이의 숫자열을 오름차순으로 정렬하여 출력
T=int(input())
for i in range(1,T+1):
    n=int(input())
    lst=list(map(int,input().split()))
    lst.sort()
    print(f"#{i}",end=" ")
    for j in range(n):
        print(lst[j],end=" ")
    print()