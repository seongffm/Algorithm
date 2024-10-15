import sys
input = sys.stdin.readline
n,m = map(int,input().split())
c_lst= [[0]*m for _ in range(n)]
x,y, direction = map(int,input().split())
c_lst[x][y]=1
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))
# 북 동 남 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]
turn_cnt =0 
res_cnt=1
while True:
    direction-=1
    if direction<0:
        direction=3
    nx = x +dx[direction]
    ny = y +dy[direction]
    if c_lst[nx][ny] ==0 and lst[nx][ny]==0:
        c_lst[nx][ny]=1
        x=nx
        y=ny
        res_cnt+=1
        turn_cnt=0
    else :
        turn_cnt+=1
    if turn_cnt==4:
        nx = x- dx[direction]
        ny = y - dy[direction]
        if lst[nx][ny]==0:
            x=nx
            y=ny
        else:
            break
        turn_cnt=0
print(res_cnt)