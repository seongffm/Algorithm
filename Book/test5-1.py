# 스택 : [],append(),pop() 으로 구현
# 큐 : from collections import deque로 구현
# 재귀 함수 : 반복문 사용하는 것보다 간결하게 구현 가능

# 팩토리얼
# 반복문
res=1
for i in range(1,int(input())+1):
    res*=i
print(res)
# 재귀함수
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)
print(factorial(int(input())))