def solution(arr):
    n = len(arr)
    answer = [0, 0]  # answer[0] = 압축된 0, answer[1] = 압축된 1

    def compress(x, y, size):
        first = arr[x][y]
        same = True

        # 이 영역이 모두 같은 값인지 확인
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != first:
                    same = False
                    break
            if not same:
                break

        if same:
            answer[first] += 1
            return

        half = size // 2
        compress(x, y, half)                 
        compress(x, y + half, half)          
        compress(x + half, y, half)          
        compress(x + half, y + half, half)   

    compress(0, 0, n)
    return answer
