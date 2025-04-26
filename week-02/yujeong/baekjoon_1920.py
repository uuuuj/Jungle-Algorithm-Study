def binary_search(array, target):
    # print(f"array : {array}")
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = int((start + end) // 2)
        # print(f"mid : {mid}")
        if array[mid] == target or array[start] == target or array[end] == target or array[mid] == array[start] == array[end] == target:
            return 1
        else:
            if array[mid] > target:
                end = mid - 1
            if array[mid] < target:
                start = mid + 1
        # print(f"start : {start}")
        # print(f"end : {end}")
    return 0


N = int(input())    # A 리스트 원소의 개수
A = list(map(int, input().split()))     # target 을 찾아야 하는 대상 리스트
M = int(input())    # target의 개수
M_list = list(map(int, input().split()))   # target의 개수
# print(f"target_list : {M_list}")

A.sort()
for m in M_list:
    print(binary_search(A, m))