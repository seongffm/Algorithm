#문제
#N=2**a*3**b*5**c*7**d*11*e
#N이 주어질때 a,b,c,d,e출력
# T=int(input())
# for i in range(1,T+1):
#     n=int(input())
#     e=n//11
#     n%=11
#     d=n//7
#     n%=7
#     c=n//5
#     n%=5
#     b=n//3
#     n%=3
#     a=n//2
#     n%=2
#틀린접근
#---------------------
# 올바른접근-->각각 소인수의 갯수
T=int(input())
lst=[2,3,5,7,11]
for i in range(1,T+1):
    N=int(input())
    ans=[]
    for j in lst:
        while N%j==0:
            ans.append(j)
            N//=j
    a=ans.count(2)
    b=ans.count(3)
    c=ans.count(5)
    d=ans.count(7)
    e=ans.count(11)
    print(f"#{i} {a} {b} {c} {d} {e}")

# #소인수분해 아이디어 div*div<=N
# T=int(input())
# for i in range(1,T+1):
#     N=int(input())
#     count=0
#     factors={2:0,3:0,5:0,7:0,11:0}
#     while N%2==0:
#         count+=1
#         N//=2
#     if count>0:
#         factors[2]=count
#     div=3
#     while div*div<=N:
#         count=0
#         while N%div==0:
#             count+=1
#             N//=div
#         if count>0:
#             factors[div]=count
#         div+=2
#     if N>1:
#         factors[N]=1
#     print(f"#{i} {factors[2]} {factors[3]} {factors[5]} {factors[7]} {factors[11]}")