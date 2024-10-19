#문제 음료수 얼려먹기
#그래프(판), 조건에 맞게 끝까지 -> DFS
# N X M크기의 얼음틀, 구멍이뚫려있는건 0, 칸막이는 1
import sys
input = sys.stdin.readline
n,m = int(input().split())
graph=[list(map(int,input()) for _ in range(n))]
def dfs(x,y):
    if x<