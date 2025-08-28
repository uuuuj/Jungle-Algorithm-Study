# https://www.acmicpc.net/problem/5430

from collections import deque
dec = deque()
is_rev = False

def call_function(s):
    global dec, is_rev

    if s == 'D':
        if len(dec) == 0:
            return "error"
        else:
            if is_rev:
                dec.pop()
            else:
                dec.popleft()
            return
    elif s == 'R':
        is_rev = not is_rev
        return

def deque_frame():
    global dec, is_rev
    is_rev = False

    str_arr =input().strip()

    n =int(input())
    s= input()
    s = s[1:-1]
    arr = []
    if len(s)!=0:
        arr = list(map(int, s.split(",")))

    dec = deque(arr)

    for s in str_arr:
        result = call_function(s)
        if result == "error":
            print("error")
            return
    if is_rev:
        dec.reverse()
    print("[" + ",".join(map(str, (dec))) + "]")

number =int(input())
for i in range(number):
    deque_frame()


