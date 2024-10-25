res=[]
lst=["3","6","9"]
for i in range(1,int(input())+1):
    ans=0
    for j in lst:
        if j in str(i):
            ans+=str(i).count(j)
    if ans:
        res.append("-"*ans)
    else:
        res.append(str(i))
for i in res:
    print(i,end=" ")

