import sys                    
from itertools import combinations  # 조합을 쉽게 만들어 주는 함수

input = sys.stdin.readline    

# 무한 루프 → 0이 나올 때까지 계속 테스트 케이스를 처리
while True:
    data = list(map(int, input().split()))   
    k = data[0]                              # 맨 앞 숫자가 k (후보 개수)
    if k == 0:                               # k가 0이면 입력 종료
        break

    nums = data[1:]                          # 실제 로또 후보 번호들
    # itertools.combinations로 6개씩 뽑은 모든 조합을 돌면서 출력
    for comb in combinations(nums, 6):
        print(*comb)                         # 공백 구분 출력

    print()                                  # 케이스 구분을 위한 빈 줄
