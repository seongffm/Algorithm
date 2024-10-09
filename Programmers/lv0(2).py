# 제곱수 판별하기
# 제출 내역
# 문제 설명
# 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 1,000,000
# 입출력 예
# n	result
# 144	1
# 976	2
# 입출력 예 설명
# 입출력 예 #1

# 144는 12의 제곱이므로 제곱수입니다. 따라서 1을 return합니다.
# 입출력 예 #2

# 976은 제곱수가 아닙니다. 따라서 2를 return합니다.

# 시간복잡도 n으로 풀긴했는데
# def solution(n):
#     answer=0
#     for i in range(2,n//2+1):
#         if i**2==n:
#             answer=1
#             break
#         else:
#             answer=2
#     return answer

# 시간복잡도와, **0.5, 정수 고려하여 푼다면->
def solution(n):
    return 1 if int(n**0.5)**2==n else 2


