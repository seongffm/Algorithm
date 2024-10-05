import sys
input = sys.stdin.readline

money = int(input())
change = [500,100,50,10]
res=[]
for i in change:
    res.append(money//i)
    money%=i
for j in res:
    print(j)
print(sum(res))