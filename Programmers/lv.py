T = int(input())

ans=0
for test_case in range(1, T + 1):
    a_lst=[]
    ans=0
    n=int(input())
    lst=list(map(int,input().split()))
    idx=lst.index(max(lst))
    while lst and idx!=0:
        idx=lst.index(max(lst))
        for _ in range(idx-1):
            a_lst.append(lst.pop())
        m_a=a_lst.pop(0)
        ans+=m_a*len(a_lst)-sum(a_lst)
        lst.pop()
    print(ans)