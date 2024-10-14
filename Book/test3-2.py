import sys
input = sys.stdin.readline

n,m=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]
res=[]
for i in range(n):
    res.append(min(lst[i]))
print(max(res))

#책의 풀이
# n,m = map(int,input().split())
# result=0
# for i in range(n):
#     data = list(map(int,input().split()))
#     min_value = min(data)
#     result=max(result,min_value)
# print(result)