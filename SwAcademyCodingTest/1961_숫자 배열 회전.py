#문제)
#N*N 행렬이 주어질때 
#90도 180도 270도 회전, N열 출력
#출력 1열-90도 180도 270도....
#풀이)
# 3행~1행 1열/ 3행 3열~1열/ 1행~3행 3열 
# 3행~1행 2열/ 2행 3열~1열/ 1행~3행 2열
# 3행~1행 3열  1행 3열~1열/ 1행~3행 1열
T=int(input())
for i in range(1,T+1):
    r_90,r_180,r_270="","",""
    n=int(input())
    lst=[list(map(int,input().split())) for _ in range(n)]
    print(f"#{i}")
    for row in range(n):
        for col in range(n):
            r_90+=str(lst[n-col-1][row])
            r_180+=str(lst[n-row-1][n-col-1])
            r_270+=str(lst[col][n-row-1])
        r_90+=" "
        r_180+=" "
        r_270+=" "
    lst1=list(map(str,r_90.split()))
    lst2=list(map(str,r_180.split()))
    lst3=list(map(str,r_270.split()))
    for j in range(n):
        print(lst1[j],lst2[j],lst3[j])

#문제 발생! :int로 형 변환할때 0으로 시작하는 문자열은 0을 자동으로 제거하고 정수형으로 처리한다
#ex) int("0123") -> 123 


