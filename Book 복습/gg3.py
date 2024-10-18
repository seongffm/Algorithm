#문제 
# L자 이동하는 나이트 이동 경우의 수  / 체스판 크기 밖으로 못나감
# 풀이
import sys
input = sys.stdin.readline
start=input().strip()
x=start[0]
y=start[1]
# dx=?
# dy=?
#해결 -> x,y묶음으로 나이트가 이동할 수 있는 8가지 방향 다 주어주기
steps=[(2,-1),(2,1),(1,2),(1,-1),(-2,-1),(-2,1),(-1,2),(-1,-1)]
result = 0
for i in steps:
    nx=ord(x)+i[0]
    ny=int(y)+i[1]
    if ord("a")<=nx<=ord("h") and 1<=ny<=8:
        result+=1
print(result)

#x,y는 갱신안하고 모든 경우의 수 nx,ny가 조건에 맞는지 보면 된다