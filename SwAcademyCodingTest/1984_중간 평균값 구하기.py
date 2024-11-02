#문제)
# 10개 수 입력 받아 최댓값과 최솟값 제외한 나머지의 평균값 출력

#풀이)
T=int(input())
for i in range(1,T+1):
    lst=list(map(int,input().split()))
    lst.remove(max(lst))
    lst.remove(min(lst))
    print(f"#{i} {round(sum(lst)/len(lst))}")