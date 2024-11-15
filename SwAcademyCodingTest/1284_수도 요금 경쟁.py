#문제)
#총 사용 W리터
#A : 리터당 P원 / 
#B:R리터 이하 기본요금Q, Q리터 초과 ->기본요금+초과한만큼*S원
T=int(input())
for i in range(1,T+1):
    P,Q,R,S,W = map(int,input().split())
    ansA,ansB=0,0
    res=0
    ansA=W*P
    if W<=R:
        ansB=Q
    else:
        ansB+=Q
        ansB+=(W-R)*S
    if ansA>ansB:
        res=ansB
    else:
        res=ansA
    print(f"#{i} {res}")