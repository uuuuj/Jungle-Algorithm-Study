# https://www.acmicpc.net/problem/1863
'''
도시에서 태양이 질 때에 보이는 건물들의 윤곽을 스카이라인이라고 한다.

스카이라인만을 보고서 도시에 세워진 건물이 몇 채인지 알아 낼 수 있을까?

..........................
.....XX.........XXX.......
.XXX.XX.......XXXXXXX.....
XXXXXXXXXX....XXXXXXXXXXXX
'''

n = int(input()) #  (1 ≤ n ≤ 50,000)

skyline = []

tower = 0
for i in range(n):
    x, h = map(int, input().split())
    if h == 0:
        skyline = []
        continue
    if len(skyline) == 0:
        skyline.append([x, h])
        tower += 1
    elif len(skyline) > 0 and h > skyline[-1][1]:
        skyline.append([x, h])
        tower += 1
    elif skyline:
        while skyline:
            tx, th = skyline.pop()
            if skyline:
                if h == skyline[-1][1]:
                    skyline.append([x, h])
                    break
                elif h > skyline[-1][1]:
                    skyline.append([x, h])
                    tower += 1
                    break
                elif h < skyline[-1][1]:
                    continue
        if not skyline:
            skyline.append([x, h])
            tower += 1

print(tower)
# 스택에 건물이 없을 때 타워 +1
'''
10
1 1
2 5
5 1
6 3
8 1
11 0
15 2
17 3
20 2
22 1

01🟨
02🟨🟨
03🟨🟨
04🟨🟨
05🟨
06🟨🟨🟨
07🟨🟨🟨
08🟨
09🟨
10🟨
11
12
13
14
15🟨🟨
16🟨🟨
17🟨🟨🟨
18🟨🟨🟨
19🟨🟨🟨
20🟨🟨
21🟨🟨
22🟨
23🟨
'''
