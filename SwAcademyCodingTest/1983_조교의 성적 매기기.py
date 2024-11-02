#문제)
#테스트 케이스 갯수, N명학생, K번째 학생 학점 출력
# T=int(input())
# for j in range(1,T+1):
#     n,k=map(int,input().split())
#     l=n//10
#     lst=["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
#     ans=[]
#     for i in range(1,n+1):
#         a,b,c=map(int,input().split())
#         ans.append((i,0.35*a+0.45*b+0.20*c))
#     ans.sort(reverse=True)
#     cnt=0
#     while l:
#         ans[cnt]=lst[cnt]
#         l-=1
    
#     print(f"#{j} {ans[k-1]}")

#올바른 풀이
t=int(input())
score=["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
for i in range(1,t+1):
    n,k=map(int,input().split())
    lst=[]
    for _ in range(n):
        a,b,c=map(int,input().split())
        lst.append(a*0.35+b*0.45+c*0.20)
    res_score=lst[k-1]
    v=n//10
    lst.sort(reverse=True)
    print(f"#{i} {score[lst.index(res_score)//v]}")

#곱하기 해서 리스트를 늘릴라고 했는데 
#이 코드는 리스트의 인덱스를 활용하여 중복된 성적을 가진 학생들에게 동일한 학점을 부여하는 방식으로 동작
#리스트는 그대로 두고 나눈값으로 인덱싱하여 결과 도출
