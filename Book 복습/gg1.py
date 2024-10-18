#문제
#N x N의 정사각형 공간에서 상하좌우 방향으로 이동  찾는게 아니라 이동 후 위치 구하는것
#풀이
#행,열별로 나누고 상하좌우 이동 정하고 해당 방향으로 이동
import sys
input = sys.stdin.readline
n=int(input())
lst=list(map(str,input().strip().split()))
x,y=1,1
dx={'U':-1,'D':1,'L':0,'R':0}
dy={'U':0,'D':0,'L':-1,'R':1}
for i in lst:
    nx,ny=x+dx[i],y+dy[i]
    if not nx<1 or ny<1 or nx>n or ny>n:
        x,y=nx,ny
print(x,y)

