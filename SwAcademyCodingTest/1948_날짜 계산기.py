#문제
#  월,일 날짜 2개 입력 받아 두 번째 날짜가 첫번째 날짜의 며칠째인지 출력
#풀이
T=int(input())
for i in range(1,T+1):
    m_1,d_1,m_2,d_2=map(int,input().split())
    lst=[31,28,31,30,31,30,31,31,30,31,30,31]
    if m_1==m_2:
        res=d_2-d_1+1
    else:
        res=lst[m_1-1]-d_1
        for j in range(m_1,m_2-1):
            res+=lst[j]
        res+=d_2+1
    print(res)

    #개선방향 슬라이싱후 sum함수 사용
    #근데 가독성 차이만 있는듯