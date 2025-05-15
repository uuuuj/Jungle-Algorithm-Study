// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/description/

#include <vector>
#include <queue>
#include <climits>

using namespace std;

class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size();
        int m = moveTime[0].size();
        vector<vector<vector<int>>> dist(n, vector<vector<int>>(m, vector<int>(2, INT_MAX)));
        dist[0][0][0] = 0;

        using T = tuple<int, int, int, int>; // (시간, x, y, 이동 횟수의 짝수/홀수 상태)
        priority_queue<T, vector<T>, greater<>> pq;
        pq.push({0, 0, 0, 0});

        vector<pair<int, int>> directions = {{0,1}, {1,0}, {0,-1}, {-1,0}};

        while (!pq.empty()) {
            auto [time, x, y, parity] = pq.top(); pq.pop();

            if (x == n - 1 && y == m - 1) return time;
            if (time > dist[x][y][parity]) continue;

            for (auto [dx, dy] : directions) {
                int nx = x + dx, ny = y + dy;
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;

                int moveCost = (parity == 0) ? 1 : 2;
                int waitTime = max(moveTime[nx][ny], time);
                int newTime = waitTime + moveCost;
                int nextParity = 1 - parity;

                if (newTime < dist[nx][ny][nextParity]) {
                    dist[nx][ny][nextParity] = newTime;
                    pq.push({newTime, nx, ny, nextParity});
                }
            }
        }

        return -1; // 도달할 수 없는 경우
    }
};