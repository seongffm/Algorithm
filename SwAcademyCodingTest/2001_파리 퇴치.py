T=int(input())
for i in range(1,T+1):
	n,m = map(int,input().split())
	lst=[list(map(int,input().split())) for _ in range(n)]
	res=0
	for j in range(n-m+1):
		for k in range(n-m+1):
			check=0
			for o in range(j,j+m):
				for p in range(k,k+m):
					check+=lst[o][p]
			if check>res:
				res=check
	print(f"#{i} {res}")