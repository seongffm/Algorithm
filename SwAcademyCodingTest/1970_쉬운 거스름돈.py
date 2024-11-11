#문제)
#거스름돈 거르기(최소 갯수)
#돈 종류: 50,000 10,000 5,000 1,000 500 100 50 10
#풀이)
T=int(input())
lst=[50000,10000,5000,1000,500,100,50,10]
for i in range(1,T+1):
    res=[]
    n=int(input())
    for j in lst:
        res.append(n//j)
        n%=j
    print(f"#{i}")
    for k in res:
        print(k,end=" ")
    print()