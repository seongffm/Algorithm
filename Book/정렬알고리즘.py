#합병정렬 [분할 정복 알고리즘,재귀]
def merge_sort(arr):
	if len(arr) <=1:
		return arr
	mid = len(arr)//2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	return merge(left,right)
def merge(left,right):
	sorted_arr =[]
	while left and right:
		if left[0] < right[0]:
			sorted_arr.append(left.pop(0))
		else:
			sorted_arr.append(right.pop(0))
	sorted_arr.extend(left)
	sorted_arr.extend(right)
	return sorted_arr

#퀵정렬 : 피벗을 기준으로 분할, 정렬 재귀적 ,같은 값들의 순서 보장하지 않기 때문에 불안정적인 정렬
def quick_sort(arr):
	if len(arr)<=1:
		return arr
	pivot = arr[len(arr)//2]#중앙값을 피벗으로
	left = [x for x in arr if x<pivot]
	middle = [x for x in arr if x==pivot]
	right = [x for x in arr if x>pivot]
	return quick_sort(left) + middle + quick_sort(right)

#힙 정렬 : 힙 자료구조 이용, 최대 힙 최소 힙
def heapify(arr,n,i):
	largest=i
	left = 2*i+1
	right = 2*i+2
	if left < n and arr[left]>arr[largest]:
		largest=left
	if right<n and arr[right]>arr[largest]:
		largest=right
	if largest!=i:
		arr[i],arr[largest]=arr[largest],arr[i]
		heapify(arr,n,largest)
def heap_sort(arr):
	n=len(arr)
	for i in range(n//2-1,-1,-1):
		heapify(arr,n,i)
	for i in range(n-1,0,-1):
		arr[i],arr[0]=arr[0],arr[i]
		heapify(arr,i,0)
	return arr
##########################
#기수 정렬
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # 출력 배열
    count = [0] * 10  # 0부터 9까지의 카운트 배열
    
    # 각 자릿수에 대한 카운트를 구합니다.
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # 누적 카운트로부터 실제 위치를 찾습니다.
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # 출력 배열을 작성합니다.
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # 출력 배열을 원래 배열에 복사합니다.
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # 배열에서 최대값을 찾아 자릿수 개수를 결정합니다.
    max_val = max(arr)
    
    # 각 자릿수에 대해 카운팅 정렬을 반복합니다.
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# 예시
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("정렬된 배열 (기수정렬):", arr)
################
#계수정렬
def counting_sort(arr):
    if len(arr) == 0:
        return arr
    
    # 배열에서 최소값과 최대값을 찾습니다.
    min_val = min(arr)
    max_val = max(arr)
    
    # 카운트 배열 크기 계산
    count_range = max_val - min_val + 1
    count = [0] * count_range  # 카운트 배열
    
    # 각 원소가 몇 번 나타나는지 셉니다.
    for num in arr:
        count[num - min_val] += 1
    
    # 카운트를 누적합니다.
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # 출력 배열을 작성합니다.
    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    
    return output

# 예시
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("정렬된 배열 (계수정렬):", sorted_arr)
