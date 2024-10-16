import sys
input=sys.stdin.readline
n,m=map(int,input().split())
for _ in range(n):
    graph=[list(map(int,input().strip()))]
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x-1,y)
        dfs(x+1,y)
        return True
    return False
result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result+=1
print(result)