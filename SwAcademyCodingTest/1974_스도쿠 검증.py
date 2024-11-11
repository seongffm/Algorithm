#문제)
#스도쿠, 가로9칸 세로9칸 ,1~9까지의 숫자
#3X3 크기의 작은 격자 또한 1~9까지의 숫자(겹치지 않음)
#출력 조건만족 1 불만족 0
T=int(input())
for i in range(1,T+1):
    lst= [list(map(int,input().split())) for _ in range(9)]
    check=[1,2,3,4,5,6,7,8,9]
    res3=[]
    res12=[]
    for j in range(9):
        res1,res2=[],[]
        for m in range(9):
            res1.append(lst[m][j])
            res2.append(lst[j][m])
        if sum(res1)==sum(res2)==sum(check):
            res12.append(j+1)

    for k in range(3):
        for l in range(3):
            res3.append(lst[k][l])
    if sum(res12)==sum(res3)==sum(check):
        print(f"#{i} 1")
    else:
        print(f"#{i} 0")