# baekjoon 1759 암호 만들기 (통과)
L, C = map(int, input().split())
letters = sorted(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
result = []

def comb(index, cur_list):
    if len(cur_list) == L and any(vowel in cur_list for vowel in vowels):
        vowel_cnt = sum(1 for vowel in cur_list if vowel in vowels)
        if len(cur_list) - vowel_cnt >= 2:
            print(''.join(cur_list))
            return

    for i in range(index, C):
        cur_list.append(letters[i])
        comb(i+1, cur_list)
        cur_list.pop()

comb(0, [])