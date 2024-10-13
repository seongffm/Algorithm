# 연속된 수의 합
# 제출 내역
# 문제 설명
# 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 num과 total이 주어집니다. 연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

# 제한사항
# 1 ≤ num ≤ 100
# 0 ≤ total ≤ 1000
# num개의 연속된 수를 더하여 total이 될 수 없는 테스트 케이스는 없습니다.
# 입출력 예
# num	total	result
# 3	12	[3, 4, 5]
# 5	15	[1, 2, 3, 4, 5]
# 4	14	[2, 3, 4, 5]
# 5	5	[-1, 0, 1, 2, 3]
# 입출력 예 설명
# 입출력 예 #1

# num = 3, total = 12인 경우 [3, 4, 5]를 return합니다.
# 입출력 예 #2

# num = 5, total = 15인 경우 [1, 2, 3, 4, 5]를 return합니다.
# 입출력 예 #3

# 4개의 연속된 수를 더해 14가 되는 경우는 2, 3, 4, 5입니다.
# 입출력 예 #4

# 설명 생략

#틀린 나의풀이
dp=[i for i in range(-1000,10001)] 
def solution(num, total):
    for i in range(-1000,10001):
        lst=dp[i:i+num]
        if sum(lst)==total:
            return lst 

#올바른 풀이
def solution(num, total): 
    var=sum(range(num)) #0~num-1까지의 갯수 num인 등차가 1인 수열 var
    diff = total-var  #목표 수열의 합과 위 수열의 합의 차이
    s_num=diff//num #그 차이를 수열의 길이로 나누면 첫번째 수열의 값
    return [s_num+i for i in range(num)]