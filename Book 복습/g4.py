#문제 n이 1이 될때까지 n-1 or n/k 
#n을 1로 만드는 최소횟수 구하기
#풀이
import sys
input = sys.stdin.readline
n,k=map(int,input().split())
# cnt=0
# while n!=1:
#     if n%k==0:
#         n//=k
#     else:
#         n-=1
#     cnt+=1
# print(cnt)

#일일이 1을 빼는것이 아닌 아이디어를 더한 풀이
result=0
while True:
    target = (n//k)*k
    result+=(n-target)
    n=target
    if n<k:
        break
    result+=1
    n//=k

result+=n-1
print(result)