import sys
input = sys.stdin.readline
pos = input().strip()
m=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
x,y=ord(pos[0]),int(pos[1])
cnt=0
for m_x,m_y in m:
    if ord("a")<=(x+m_x)<=ord("h") and 1<=(y+m_y)<=8:
        cnt+=1
print(cnt)

    