#문제)
#1부터 N까지의 숫자에서 홀수는 더하고 짝수는 빼는 로직 구현 후 최종 누적값 출력
#N:5 -> 1-2+3-4+5=3
T=int(input())
for i in range(1,T+1):
    lst=[]
    N=int(input())
    for j in range(1,N+1):
        if j%2==0:
            lst.append(j*-1)
        else:
            lst.append(j)
    print(f"#{i} {sum(lst)}")
