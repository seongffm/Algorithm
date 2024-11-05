#문제)
# NxN의 퍼즐에서 길이가 k인 단어가 들어갈 수 있는 자리 수 출력
#나의풀이)
#틀린접근> 0이 나올때 어떻게 처리할지 생각못함
# T=int(input())
# for i in range(1,T+1):
#     n,k=map(int,input().split())
#     lst=[list(map(str,input().split())) for _ in range(n)]
#     res=0
#     for row in range(n):
#         cnt=""
#         for col in range(n):
#             cnt+=lst[row][col]
#         if "1"*k == cnt:
#             res+=1
#     for col in range(n):
#         cnt=""
#         for row in range(n):
#             cnt+=lst[row][col]
#         if "1"*k in cnt:
#             res+=1
#         print(res)
#     print(f"#{i} {res}")        

#올바른 접근: 0이나올때나 리스트 마지막일때 cnt가 k랑 같은지 체크 및 cnt를 0으로 초기화 하면된다
#올바른풀이)
T=int(input())
for i in range(1,T+1):
    n,k=map(int,input().split())
    lst=[list(map(int,input().split())) for _ in range(n)]
    res=0
    for row in range(n):
        cnt=0
        for col in range(n):
            if lst[row][col]==1:
                cnt+=1
            if lst[row][col]==0 or col==n-1:
                if cnt==k:
                    res+=1
                cnt=0
    for col in range(n):
        cnt=0
        for row in range(n):
            if lst[row][col]==1:
                cnt+=1
            if lst[row][col]==0 or row==n-1:
                if cnt==k:
                    res+=1
                cnt=0
    print(f"#{i} {res}")        