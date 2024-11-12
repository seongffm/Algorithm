#문제)
#N개의 숫자열 Ai M개의 숫자열 Bj
T = int(input())
for i in range(1,T+1):
    n,m = map(int,input().split())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    lst=[]
    if n>m:
        for j in range(n-m+1):
            res=0
            lst1_r=lst1[j:m+j]
            for k in range(m):
                res+=lst2[k]*lst1_r[k]
            lst.append(res)
        print(f"#{i} {max(lst)}")
    else:
        for j in range(m-n+1):
            res=0
            lst2_r=lst2[j:n+j]
            for k in range(n):
                res+=lst1[k]*lst2_r[k]
            lst.append(res)
        print(f"#{i} {max(lst)}")
        