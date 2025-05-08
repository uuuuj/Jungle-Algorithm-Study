# 프로그래머스: 호텔 대실
# https://school.programmers.co.kr/learn/courses/30/lessons/155651

def solution(book_time):
    room = 0                 # 필요한 최소 객실 수
    cur_room = []            # 현재 사용 중인 객실들의 퇴실 시간 리스트

    # 예약 시작 시간 기준으로 정렬
    book_time = sorted(book_time)

    for check_in, check_out in book_time:
        # 체크인 시간과 체크아웃 시간을 시:분 → 정수형 분 단위로 파싱
        cih, cim = map(int, check_in.split(':'))   # 체크인 시/분
        coh, com = map(int, check_out.split(':'))  # 체크아웃 시/분

        empty_room_idx = 0

        # 현재 예약 시작 전에 퇴실 완료된 객실 수 파악
        for crh, crm in cur_room:
            # 이미 퇴실 완료된 객실 (퇴실 시간 <= 이번 체크인 시간)
            if crh < cih or (crh == cih and crm <= cim):
                empty_room_idx += 1

        # 퇴실 완료된 객실들을 리스트에서 제거 (객실 정리 완료 처리)
        cur_room = cur_room[empty_room_idx:]

        # 퇴실 처리 시간 10분 추가
        if com + 10 >= 60:
            cur_room.append([coh + 1, (com + 10) % 60])
        else:
            cur_room.append([coh, com + 10])

        # 다음 탐색을 위한 정렬 (가장 먼저 퇴실할 객실이 앞에 오도록)
        cur_room = sorted(cur_room)

        # 현재 필요한 최대 객실 수 업데이트
        room = max(len(cur_room), room)

    return room