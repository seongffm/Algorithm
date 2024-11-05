#문제)
#시 분 으로 이루어진 시각 2개 입력 받아 더한 값을 시 분으로 출력하는 프로그램
#(시각은 12시간제) (분은 0이상 59이하 정수)
#풀이)
T=int(input())
for i in range(1,T+1):
    h,m,n_h,n_m=map(int,input().split())
    r_h=h+n_h
    r_m=m+n_m
    if r_m>=60:
        r_h+=1
        r_m-=60
    if r_h>12:
        r_h-=12
    print(f"#{i} {r_h} {r_m}")