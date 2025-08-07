def solution(video_len, pos, op_start, op_end, commands):
    video_m, video_s = map(int, video_len.split(':'))
    ops_m, ops_s = map(int, op_start.split(':'))
    ope_m, ope_s = map(int, op_end.split(':'))
    pos_m, pos_s = map(int, pos.split(':'))
    
    def check_is_opening(pos_m, pos_s):
        if (ops_m < pos_m or (ops_m == pos_m and ops_s <= pos_s)) and (pos_m < ope_m or (pos_m == ope_m and pos_s <= ope_s)):
            return [ope_m, ope_s]
        return [pos_m, pos_s]
    
    for c in commands:
        
        pos_m, pos_s = check_is_opening(pos_m, pos_s)
        
        if c == 'next':
            
            pos_s += 10
            
            if pos_s > 60:
                pos_s -= 60
                pos_m += 1
            
            if (pos_m > video_m) or (pos_m == video_m and pos_s > video_s):
                pos_m = video_m
                pos_s = video_s
                
            
            if ops_m <= pos_m and ops_s <= pos_s and pos_m <= ope_m and pos_s <= ope_s:
                pos_m = ope_m
                pos_s = ope_s

        else:
            
            if pos_m == 0 and pos_s < 10:
                pos_m = 0
                pos_s = 0
            
            else:
                if pos_s < 10:
                    pos_s = 60 + pos_s - 10
                    pos_m -= 1
                else:
                    pos_s -= 10
                    
        pos_m, pos_s = check_is_opening(pos_m, pos_s)

        pos = f"{f'0{pos_m}' if pos_m < 10 else pos_m}:{f'0{pos_s}' if pos_s < 10 else pos_s}"

    return pos