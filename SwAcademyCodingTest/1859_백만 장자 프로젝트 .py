T=int(input())
for i in range(1,T+1):
	n=int(input())
	lst = list(map(int,input().split()))
	lst=lst[::-1]
	cur = lst[0]
	c=[]
	res=0
	for j in lst:
		if cur > j:
			res+=cur-j  
		else:
			cur=j
	print(f"#{i} {res}")