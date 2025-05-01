def search_card(cards, search_list):
    search_dict = {}

    for i in cards:
        if i in search_dict:
            search_dict[i] += 1
        else:
            search_dict[i] = 1
    for j in search_list:
        if j in search_dict:
            print(search_dict[j], end = " ")
        else:
            print(0, end = " ")

    


N = int(input())
Cards = list(map(int, input().split()))
M = int(input())
Search_card = list(map(int, input().split()))

search_card(Cards, Search_card)

# search_card(N, Cards, M, Search_card)