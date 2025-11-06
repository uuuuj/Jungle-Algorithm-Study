# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    lux = 51
    luy = 51
    rdx = -1
    rdy = -1
    for i, line in enumerate(wallpaper): 
        for j, ele in enumerate(line):    
            if ele == "#":
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i)
                rdy = max(rdy, j)
                     
    return [lux, luy, rdx + 1, rdy + 1]
