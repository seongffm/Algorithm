from collections import Counter
def solution(a, b):
    n=2
    lst_a=[]
    lst_b=[]
    while a!=1:
        if a%n==0:
            lst_a.append(n)
            a//=n
        else:
            n+=1
    lst_a=list(set(lst_a))
    n=2
    while b!=1:
        if b%n==0:
            lst_b.append(n)
            b//=n
        else:
            n+=1
    lst_b=list(set(lst_b))
    lst_b=Counter(lst_b)
    lst_a=Counter(lst_a)
    lst_b=lst_b-lst_a
    for k,v in lst_b.items():
        if k not in [2,5] and v>0:
            return 2
    return 1
print(solution(7,20))
print(solution(11,22))
print(solution(12,21))