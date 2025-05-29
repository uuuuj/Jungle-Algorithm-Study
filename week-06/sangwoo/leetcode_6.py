# LeetCode 6번: Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 예외 처리: 한 줄이거나 문자열 길이보다 줄 수가 많으면 그대로 반환
        if len(s) <= numRows or numRows == 1:
            return s

        board = []                      # 결과적으로 열 단위로 저장되는 문자열 배열
        cur_row = [''] * numRows        # 현재 열을 구성하는 문자열 리스트

        for i in range(len(s)):
            # 그룹 인덱스를 구해 행 방향 또는 대각선 방향 판단
            group_index = i % (2 * numRows - 2)

            if group_index < numRows:
                # 아래로 내려가는 구간
                cur_row[group_index] = s[i]
            else:
                # 대각선 올라가는 구간
                board.append(cur_row)
                cur_row = [''] * numRows
                cur_row[numRows - group_index - 2] = s[i]

            # 한 그룹(세로 아래 + 대각선 위)이 끝나는 시점에 board에 저장
            if group_index == 2 * numRows - 3:
                board.append(cur_row)
                cur_row = [''] * numRows

        # 마지막 cur_row도 누락되지 않도록 추가
        board.append(cur_row)

        # board를 행 중심으로 읽어서 결과 문자열 재구성
        res = ''
        for row in range(numRows):
            for col in range(len(board)):
                if board[col][row] != '':
                    res += board[col][row]

        return res