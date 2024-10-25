# from collections import deque
# t=int(input())
# for i in range(1,t+1):
#     txt=input().strip()
#     que = deque(txt)
#     for i in que:
#         if que[i]:
#             print("")
        #?? 갯수, 중복문자(set처리) 아닌데..

#올바른 접근, 풀이 >>
    #마디 길이가 10이니까 슬라이싱으로 처음 ,2*처음 고려하여 비교하여 구현
t= int(input())
for j in range(1,t+1):
    txt = input().strip()
    ans=0
    for i in range(1,11):
        if txt[:i] == txt[i:2*i] and txt[-1] == txt[:i][-1]:
            ans=i
            break
    print(f"#{j} {ans}")

#samsung, lalacost 테스트케이스 통과하려면 슬라이싱하고 난뒤 같을때 + 마지막 문자도 고려(samsung처럼 마디가 2종류일때)
