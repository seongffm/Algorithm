#문제 
#command 종류:
#0:현재속도유지 1:가속 2:감속
#N초동안 총 이동한 거리 구하기
T=int(input())
for i in range(1,T+1):
    N=int(input())
    res=0
    r_v=0
    for _ in range(N):
        line=input().split()
        if line[0]=="0":
            res+=r_v
        elif line[0]=="1":
            r_v+=int(line[1])
            res+=r_v
        elif line[0]=="2":
            r_v-=int(line[1])
            if r_v<0:
                r_v=0
            res+=r_v
    print(f"#{i} {res}")




