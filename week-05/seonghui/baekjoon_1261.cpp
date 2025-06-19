// 공통문제
// https://www.acmicpc.net/problem/1261

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int M, N;
    // 입력 받기
    cin >> M >> N;

    int miro[N][M];
    
    for (int i = 0; i < N; i++) {
        string line;
        cin >> line; // 한 줄 입력 받기
        
        int col = 0;
        for (char ch : line) {
            miro[i][col++] = ch-'0';
        }
    }

    vector<vector<int>> wall(N, vector<int>(M, M*N));
    wall[0][0] = 0;
    
    // 좌, 상, 우, 하
    int dx[4] = {0, -1, 0, 1};
    int dy[4] = {-1, 0, 1, 0};

    deque<pair<int, int>> dq;

    dq.push_back({0,0});

    while (!dq.empty()) {
        auto [x, y] = dq.front();
        dq.pop_front();

        for (int j = 0; j < 4; j++) {
            int nx = x + dx[j];
            int ny = y + dy[j];

            // 범위 검사
            if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;

            if (wall[nx][ny] > wall[x][y] + miro[nx][ny]) {
                wall[nx][ny] = wall[x][y] + miro[nx][ny];
                if (miro[nx][ny] == 1) {
                    dq.push_back({nx, ny});
                }
                else {
                    dq.push_front({nx, ny});
                }
            }

        }
    }

    // 최소로 부수는 벽의 개수
    cout << wall[N-1][M-1];

    return 0;
}