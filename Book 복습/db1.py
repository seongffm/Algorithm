#문제 음료수 얼려먹기
#그래프(판), 조건에 맞게 끝까지 -> DFS
# N X M크기의 얼음틀, 구멍이뚫려있는건 0, 칸막이는 1
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph=[list(map(int,input().strip())) for _ in range(n)]
#상하좌우
def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m:
       return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
cnt=0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            cnt+=1
print(cnt)