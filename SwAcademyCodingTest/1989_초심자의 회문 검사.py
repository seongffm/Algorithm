#문제)
#거꾸로 읽어도 같은 문자-> 회문
#회문-> 출력 1 아니면 0
T=int(input())
for i in range(1,T+1):
    txt=input().strip()
    if txt[::-1]==txt:
        print(f"#{i} 1")
    else:
        print(f"#{i} 0")