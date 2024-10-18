import sys
input = sys.stdin.readline
n,m,k = map(int,input().strip().split())
lst=sorted(list(map(int,input().strip().split())),reverse=True)
first=lst[0]
second=lst[1]
print((m//(k+1))*(first*k+second)+m%(k+1)*first)

#책 아이디어
count = int(m/(k+1))*k
count+=m%(k+1)
result=0
result+=count*first+(m-count)*second
print(result)

