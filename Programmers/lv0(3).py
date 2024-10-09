# 배열 회전시키기
# 제출 내역
# 문제 설명
# 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 3 ≤ numbers의 길이 ≤ 20
# direction은 "left" 와 "right" 둘 중 하나입니다.
# 입출력 예
# numbers	direction	result
# [1, 2, 3]	"right"	[3, 1, 2]
# [4, 455, 6, 4, -1, 45, 6]	"left"	[455, 6, 4, -1, 45, 6, 4]
# 입출력 예 설명
# 입출력 예 #1

# numbers 가 [1, 2, 3]이고 direction이 "right" 이므로 오른쪽으로 한 칸씩 회전시킨 [3, 1, 2]를 return합니다.
# 입출력 예 #2

# numbers 가 [4, 455, 6, 4, -1, 45, 6]이고 direction이 "left" 이므로 왼쪽으로 한 칸씩 회전시킨 [455, 6, 4, -1, 45, 6, 4]를 return합니다.

#스택을 이용해서 pop, append로 풀이했으나
# def solution(numbers, direction):
#     left=0
#     answer=[]
#     if direction == "right":
#         answer.append(numbers.pop())
#     else:
#         left=numbers.pop(0)
#     while numbers:
#         answer.append(numbers.pop(0))
#     if left:
#         answer.append(left)
#     return answer
# 슬라이싱으로 간단하게 구현할 수 있다-> 
def solution(numbers,direction):
    return [numbers[-1]]+numbers[:-1] if direction=="right" else numbers[1:]+[numbers[0]]