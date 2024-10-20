#문제
#처음위치 (1,1) ~ 출구(N,M)
#탈출하기 위한 최소 칸의 갯수
#가까운거 탐색하면서 출구까지 가야함 -> bfs
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]
#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
from collections import deque
def bfs(x,y):
    queue= deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))    


