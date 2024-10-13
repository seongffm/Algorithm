# 안전지대
# 제출 내역
# 문제 설명
# 다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
# image.png
# 지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
# 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# board는 n * n 배열입니다.
# 1 ≤ n ≤ 100
# 지뢰는 1로 표시되어 있습니다.
# board에는 지뢰가 있는 지역 1과 지뢰가 없는 지역 0만 존재합니다.
# 입출력 예
# board	result
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]	16
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]	13
# [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]	0
# 입출력 예 설명
# 입출력 예 #1

# (3, 2)에 지뢰가 있으므로 지뢰가 있는 지역과 지뢰와 인접한 위, 아래, 좌, 우, 대각선 총 8칸은 위험지역입니다. 따라서 16을 return합니다.
# 입출력 예 #2

# (3, 2), (3, 3)에 지뢰가 있으므로 지뢰가 있는 지역과 지뢰와 인접한 위, 아래, 좌, 우, 대각선은 위험지역입니다. 따라서 위험지역을 제외한 칸 수 13을 return합니다.
# 입출력 예 #3

# 모든 지역에 지뢰가 있으므로 안전지역은 없습니다. 따라서 0을 return합니다.

#틀린 나의풀이:
# def solution(board):
#     n=5
#     for row in range(n):
#         for col in range(n):
#             if board[row][col] ==1:
#                 for n_row in range(row-1,row+2):
#                     for n_col in range(col-1,col+2):
#                         if n_row<0:
#                             n_row=0
#                         if n_col<0:
#                             n_col=0
#                         if n_row>n-1:
#                             n_row=n-1
#                         if n_col>n-1:
#                             n_col=n-1

#     cnt=0
#     for i in board:
#         cnt+=i.count(1)
#     return n**2-cnt
#올바르게 카운팅이 안됨
 
# 올바른풀이-->
#8개의 지역을 지정해두고 다 체크(범위 넘어갈 때 빼고)
def solution(board):
    n= len(board)
    dx=[-1,-1,-1,0,0,1,1,1]
    dy=[-1,0,1,-1,1,-1,0,1]
    bomb=[]
    cnt=0
    for row in range(n):
        for col in range(n):
            if board[row][col]==1:
                bomb.append((row,col))
    for x,y in bomb:
        for i in range(8):
            if 0<=x+dx[i]<n and 0<=y+dy[i]<n:
                board[x+dx[i]][y+dy[i]]=1
    for j in board:
        cnt+=j.count(1)
    return n*n-cnt
        
                
                
 
                