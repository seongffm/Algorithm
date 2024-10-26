# for i in range(int(input())):
#     print(f'#{i+1}')
# t=int(input())
# for i in range(t) :
#     ans="1 "
#     ans+=(str(i)+' ')*(i-1)
#     if i>0:
#         print(ans+"1")
#     else:
#         print(ans)

#올바른 풀이
t=int(input())
for i in range(1,t+1):
	print(f"#{i}")
	n = int(input())
	lst=[[0]*n for _ in range(n)]
	lst[0][0]=1
	for j in range(1,n):
		for k in range(n):
			if k == 0:
				lst[j][k]=1
			else:
				lst[j][k]=lst[j-1][k-1]+lst[j-1][k]
	for l in range(n):
		for m in range(n):
			if lst[l][m]:
				print(lst[l][m],end=' ')
		print()