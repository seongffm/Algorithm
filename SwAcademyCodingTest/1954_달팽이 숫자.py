#문제)
# 1부터 N*N까지의 숫자가 시계 방향으로
# 정수 N 입력받아 N 크기의 달팽이 출력

#방향으로 생각 부족
#오른쪽 아래 왼쪽 위
#--> dx dy방향으로 나누어서 생각
T=int(input())
for i in range(1,T+1):
    n=int(input())
    lst=[[0]*n for _ in range(n)]
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    d = 0
    x,y=0,0
    for num in range(1,n*n+1):
        lst[x][y]=num
        nx,ny=x+dx[d],y+dy[d]
        if nx<0 or nx>=n or ny>=n or ny<0 or lst[nx][ny]:
            d=(d+1)%4
            nx,ny=x+dx[d],y+dy[d]
        x,y=nx,ny
    print(f"#{i}")
    for r in range(n):
        for c in range(n):
            print(lst[r][c],end=" ")
        print()
