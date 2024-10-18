#문제
# 행기준으로 가장작은거
# 그 후 선별한거 중에 가장 큰거

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ck=[]
result=0
for _ in range(n):
    lst=list(map(int,input().split()))
    min_ = min(lst)
    result=max(min_,result)
print(result)
