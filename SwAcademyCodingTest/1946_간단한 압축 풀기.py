#문제)
#너비가 10인 원본 문서
#압축된 문서를 입력받아 원본 문서를 만드는 프로그램
T=int(input())
for i in range(1,T+1):
    n=int(input())
    char=""
    for _ in range(n):
        a,b=map(str,input().split())
        char+=a*int(b)
    print(f"#{i}")
    for j in range(1,len(char)+1):
        print(char[j-1],end="")
        if j%10==0:
            print()
    print()

#개선방향-> 슬라이싱
T=int(input())
for i in range(1,T+1):
    n=int(input())
    char=""
    for _ in range(n):
        a,b=map(str,input().split())
        char+=a*int(b)
    print(f"#{i}")
    for j in range(0,len(char),10):
        print(char[j:j+10])