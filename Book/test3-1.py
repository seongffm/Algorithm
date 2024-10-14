import sys
input = sys.stdin.readline

# n,m,k=map(int,input().split())
# lst=list(map(int,input().split()))
# lst=sorted(lst,reverse=True)
# cnt=0
# sum=0
# while cnt!=m:
#     for _ in range(k):
#         sum+=lst[0]
#         cnt+=1
#     sum+=lst[1]
#     cnt+=1
# print(sum)

# 위 코드는 시간초과 발생
# 시간초과 해결->
n,m,k = map(int,input().split())
lst=list(map(int,input().split()))
lst=sorted(lst,reverse=True)
first=lst[0]
second = lst[1]
cnt=m//(k+1)*k+m%(k+1)
res=0
res+=cnt*first
res+=(m-cnt)*second
print(res)