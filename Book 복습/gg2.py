#문제
#시각 시 분 초 하나라도 3이 포함되는 모든 경우의 수를 출력
#N시 59분 59초
cnt=0
for i in range(0,int(input())+1):
    for j in range(0,60):
        for k in range(0,60):
            if "3" in str(k) or "3" in str(j) or "3" in str(i):
                cnt+=1
print(cnt)

