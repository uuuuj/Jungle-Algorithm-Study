import sys

input = sys.stdin.readline

# p: 플레이어 수, m: 방의 정원(최대 인원)
p, m = map(int, input().split())

# 생성된 방들을 저장하는 리스트
# 각 방은 [[이름, 레벨], [이름, 레벨], ...] 형태로 저장됨
rooms = []

# 각 플레이어를 순서대로 처리
for _ in range(p):
  no_room = True  # 적합한 방을 찾지 못했는지 체크하는 플래그
  level, name = input().split()
  level = int(level)

  # 첫 번째 플레이어인 경우 새 방 생성
  if len(rooms) == 0:
    rooms.append([[name, level]])
    continue

  # 기존 방들을 순회하며 입장 가능한 방 찾기
  for r in rooms:
    standard_lv = r[0][1]  # 방의 기준 레벨 (첫 번째 입장자의 레벨)
    
    # 디버깅용 주석 처리된 print문
    # print(f'name: {name}, is10: {standard_lv - 10 <= level <= standard_lv + 10}, len5: {len(r)< m}')
    
    # 이미 해당 방에 입장한 경우 (중복 체크)
    if name in [i[0] for i in r]:
      no_room = False 
      break
    
    # 입장 조건:
    # 1. 레벨이 기준 레벨의 ±10 범위 내
    # 2. 방의 현재 인원이 정원 미만
    if standard_lv - 10 <= level <= standard_lv + 10 and len(r) < m:
      r.append([name, level])  # 방에 플레이어 추가
      no_room = False 
      break

  # 입장 가능한 방이 없으면 새 방 생성
  if no_room:
    rooms.append([[name, level]])

# 각 방의 상태 출력
for r in rooms:
  # 방이 정원에 도달하면 게임 시작, 아니면 대기 중
  if len(r) == m:
    print('Started!')
  else:
    print('Waiting!')

  # 방의 멤버들을 닉네임 기준 사전순 정렬 후 출력
  # 형식: "레벨 닉네임"
  joined_mem = [str(mem[1]) + " " + mem[0] for mem in sorted(r, key=lambda x : x[0])]
  
  # 한 줄에 한 명씩 출력
  print(*joined_mem, sep='\n')