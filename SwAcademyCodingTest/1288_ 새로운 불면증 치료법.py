#문제
#N의 배수 양 세기
#N의 배수 계속 센 다음 0~9 다있으면 멈추기
T=int(input())
for i in range(1,T+1):
    N=int(input())
    lst=[0,1,2,3,4,5,6,7,8,9]
    ch=[]
    d=N
    while lst!=ch:
        for j in str(d):
            ch.append(int(j))
        ch=list(set(ch))
        ch.sort()
        d+=N
    print(f"#{i} {d-N}")