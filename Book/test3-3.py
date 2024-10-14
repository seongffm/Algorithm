#나의 풀이
# import sys
# input = sys.stdin.readline
# n,k=map(int,input().split())
# cnt=0
# while n!=1:
#     if n%k==0:
#         n//=k
#     else:
#         n-=1
#     cnt+=1
# print(cnt)

#책의 풀이
import sys
input = sys.stdin.readline
n,k=map(int,input().split())
cnt=0
while True:
    target=(n//k)*k #1을 빼는 연산 횟수 구하기위해
    cnt +=(n-target) #1을 빼는 연산 횟수 구하기
    n=target 
    if n<k:
        break
    cnt+=1
    n//=k
cnt+=(n-1) #1을 빼는 횟수 구하기
print(cnt)