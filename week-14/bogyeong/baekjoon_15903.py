# baekjoon 1759 카드합체놀이
'''
(1)
3 1
3 2 6

(2)
4 2
4 2 3 1
'''
cards = []
N, M = map(int, input().split())
cards = list(map(int, input().split()))

for i in range(M):
    cards.sort()
    a = cards.pop(0)
    b = 0
    for j in range(len(cards)-1):
        if cards[j] != a:
            b = cards.pop(j)
            break
    cards.append(a + b)
    cards.append(a + b)

print(sum(cards))
















