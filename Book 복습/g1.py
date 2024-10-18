#문제 
# 거스름돈 종류: 500,100,50,10
# N원 거슬러줄때 동전의 최소갯수 구하기
#풀이
change=[500,100,50,10]
n= int(input())
cnt=0
for i in change:
    cnt+=n//i
    n%=i
    if n==0:
        print(cnt)
        break
