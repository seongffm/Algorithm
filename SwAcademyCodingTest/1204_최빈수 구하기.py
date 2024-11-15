#문제 
#최빈수
from collections import Counter
# Counter에 리스트 할당해서 빈수의 딕셔너리 구할 수 있고
T=int(input())
for i in range(1,T+1):
    n=int(input())
    lst=list(map(int,input().split()))
    c_lst=Counter(lst)
    # values중 max값으로 최빈수 값 구하고
    max_freq=max(c_lst.values())
    # 최빈수 값의 key값들의 집합을 구하고
    res=[score for score, freq in c_lst.items() if freq==max_freq]
    #그 중 max값 출력
    ans=max(res)
    print(f"#{n} {ans}")


