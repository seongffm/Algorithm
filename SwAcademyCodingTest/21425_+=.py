for _ in range(int(input())):
	a,b,n = map(int,input().split())
	cnt=0
	res=0
	while res<=n:
		cnt+=1
		res=min(a,b)
		res+=max(a,b)
		if a>=b:
			b+=a
		else:
			a+=b
	print(cnt)

#더 쉽게 생각 했으면 됬다..
for _ in range(int(input())):
    a, b, n = map(int, input().split())
    cnt = 0
    while a <= n and b <= n:
        cnt += 1
        # a와 b의 값 갱신
        if a < b:
            a += b
        else:
            b += a
    print(cnt)


			