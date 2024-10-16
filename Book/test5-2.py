# 그래프 : 간선과 노드
# 인접행렬(2차원 배열로 그래프 표현) /#인접 리스트(리스트로 그래프 표현)

#인접행렬
INF = 999999999 #무한 비용 의미
graph =[
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]
#인접리스트
graph=[[] for _ in range(3)]
graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((0,7))
graph[2].append((0,5))

# DFS - 스택  #BFS  -  큐
#번호가 낮은 순서부터 처리하도록 구현
#DFS
def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            #업으면 이전노드로 돌아가는 백트래킹진행됨
graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]
visited=[False]*9
print(dfs(graph,1,visited))

#BFS
from collections import deque
def bfs(graph,start,visited):
    queue = deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9
print(bfs(graph,1,visited))




