#문제
# 판이 주어지고 조건에 맞는 이동 수 구현
#풀이
# n x m 맵 생성하고 현재 위치, 방향 주어지고 맵 주어짐
# 방향에 따라 한칸 이동하고 맵과 방문 여부에 따른 이동 제한
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
x,y,d = map(int,input().split())
check=[[0]*m for _ in range(n)]
check[x][y]=1
cnt=0
lst=[list(map(int,input().split())) for _ in range(n)]
directions=[0,1,2,3] #북 동 남 서
dx=[0,-1,0,1]
dy=[-1,0,1,0] 
while True:
    nd=d-1
    if nd<0:
        nd=3
    nx=x+dx[nd]
    ny=y+dy[nd]
    if check[nx][ny]==0 and lst[nx][ny]==0:
        check[nx][ny]=1
        x=nx
        y=ny
        cnt+=1
        

