# https://www.acmicpc.net/problem/1043

# BFS 방식
import sys
from collections import deque

input = sys.stdin.readline

# N: 사람 수, M: 파티 수
N, M = map(int, input().split())

# 진실을 아는 사람 정보
K_info = list(map(int, input().split()))
K = K_info.pop(0)  # 진실을 아는 사람 수
# K_info: 진실을 아는 사람들의 번호 리스트

# 사람별로 참석한 파티 정보 저장
user_party_info = [[] for _ in range(N + 1)]
# 파티별로 참석자 정보 저장
party_user_info = [[] for _ in range(M + 1)]

# 각 파티 정보 입력 받기
for i in range(1, M + 1):
    data = list(map(int, input().split()))
    user = data[1:]  # 참석자 목록
    party_user_info[i] = user

    # 각 참석자가 이 파티에 참석했다고 기록
    for u in user:
        user_party_info[u].append(i)

# 각 파티에 대해 거짓말 가능 여부를 저장
# 인덱스 0은 더미
can_go_party = [False] + [True] * M

# BFS용 방문 배열: 이미 진실이 전파된 사람 체크
visited_user = [False] * (N + 1)

# 진실을 아는 사람들부터 BFS 시작
q = deque(K_info)
for k in K_info:
    visited_user[k] = True

while q:
    cur = q.popleft()

    # 현재 사람이 참석한 모든 파티에 대해
    for p in user_party_info[cur]:
        # 아직 거짓말 가능한 파티라면
        if can_go_party[p]:
            can_go_party[p] = False  # 이제 이 파티에서는 거짓말 불가

            # 이 파티의 모든 사람을 큐에 넣음 (진실이 전파됨)
            for u in party_user_info[p]:
                if not visited_user[u]:
                    visited_user[u] = True
                    q.append(u)

# 거짓말 가능한 파티의 개수 출력
print(sum(can_go_party))

### union-find 방식

# Union-Find에서 루트 노드를 찾는 함수 (경로 압축 포함)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 노드를 같은 집합으로 합치는 함수
def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        parent[b_root] = a_root

# 입력: 사람 수 n, 파티 수 m
n, m = map(int, input().split())
truth_info = list(map(int, input().split()))
truth_people = truth_info[1:]  # 진실을 아는 사람들만 추출

# 각 사람의 부모 초기화 (자기 자신)
parent = [i for i in range(n + 1)]

parties = []  # 각 파티의 참석자 목록 저장

# 파티 정보 입력
for _ in range(m):
    data = list(map(int, input().split()))
    people = data[1:]
    parties.append(people)

    # 같은 파티에 속한 사람들 union (같은 집합으로 묶기)
    for i in range(1, len(people)):
        union(people[0], people[i])

# 진실을 아는 사람들의 루트(대표)만 따로 모음
truth_roots = set(find(p) for p in truth_people)

# 결과 계산: 진실을 아는 집합과 겹치지 않는 파티만 세기
answer = 0
for party in parties:
    # 파티에 있는 사람이 모두 진실 루트와 관련 없을 때만 count
    if all(find(p) not in truth_roots for p in party):
        answer += 1

print(answer)
