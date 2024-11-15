#문제 Encoding
#3byte=>ord하고->2진수 8bit*3->6bit*4->10진수->chr(x) 문제의 표
#를 반대로 ->Decoding

#인코딩 과정: 문자->ord()->(10진수)->2진수->조건에맞게 슬라이싱->10진수변환->(표,chr 조건)
#디코딩과정: 입력받은 문자->표로인해 10진수로 바꾸고-> 6비트의 2진수로 다 모아서 8비트씩 자르고 -> 10진수 변환후 chr
#06b, 08b
T=int(input())
lst=list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
for i in range(1,T+1):
    ans,check="",""
    q=input()
    for j in q:
        j=format(lst.index(j),'06b')
        check+=j
    for k in range(0,len(check),8):
        ans+=chr(int(check[k:k+8],2))
    print(f"#{i} {ans}")

# lst=list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
# q=input()
# ans,check="",""
# for i in q:
#     i=format(ord(i),'08b')
#     check+=i
# for j in range(0,len(check),6):
#     ans+=lst[int(check[j:j+6],2)]
# print(ans)

            



    
