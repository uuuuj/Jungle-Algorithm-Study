import sys

noq = int(sys.stdin.readline())

col = [ 0 ] * noq # 퀸이 놓인 행 index
flag = [ False ] * noq # 퀸이 행에 놓였는지
flag_c = [False] * (noq * 2 - 1) # 퀸이 우하향 대각선에 놓여있는지
flag_rc = [False] * (noq * 2 - 1) # 퀸이 우상향 대각선에 놓여있는지

total_count = []

def set_queen(n):
  for i in range(noq):
    if (
          not flag[i] 
      and not flag_c[i + n]
      and not flag_rc[n- i + noq - 1]
    ):
      col[n] = i

      if n == noq - 1:
        total_count.append(col)
      else:
        flag[i] = flag_c[n + i] = flag_rc[n - i + noq - 1] = True
        set_queen(n + 1)
        flag[i] = flag_c[n + i] = flag_rc[n - i + noq - 1] = False  


set_queen(0)
print(len(total_count))