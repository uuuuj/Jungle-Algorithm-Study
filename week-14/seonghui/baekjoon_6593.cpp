// 공통문제
// https://www.acmicpc.net/problem/6593

#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int L = -1, R = -1, C = -1;

int bfs(tuple<int, int, int> start, vector<vector<vector<char>>>& building) {
	queue<tuple<int, int, int>> q;

	q.push(start);
	
	int minutes = 0;

	// 하, 상, 남, 북, 동, 서
    int dx[6] = {1, -1, 0, 0, 0, 0};
    int dy[6] = {0, 0, 1, -1, 0, 0};
    int dz[6] = {0, 0, 0, 0, 1, -1};
	
	while (!q.empty()) {        
        int qsize = q.size();
        for (int j = 0; j < qsize; ++j) {
            auto [x, y, z] = q.front();
            q.pop();

            for (int i = 0; i < 6; ++i) {
                int new_x = x + dx[i], new_y = y + dy[i], new_z = z + dz[i];
                if (new_x < 0 || new_y < 0 || new_x >= L || new_y >= R || new_z < 0 || new_z >= C) continue;
                
                if (building[new_x][new_y][new_z] == '.') {
                    // 큐에 넣기
                    q.push({new_x, new_y, new_z});
                    building[new_x][new_y][new_z] = 'V';
                }
                // E 만나면 종료
                else if (building[new_x][new_y][new_z] == 'E') {
                    return ++minutes;
                }
            }
        }
        
        ++minutes;
	}

	return -1;
}

int main() {
    while (1) {
        if (!(cin >> L >> R >> C)) break;  
        if (!L && !R && !C) return 0;

        tuple<int, int, int> start = {0, 0, 0};

        vector<vector<vector<char>>> building(L, vector<vector<char>>(R, vector<char>(C)));
        for (int i = 0; i < L; ++i) {
            for (int j = 0; j < R; ++j) {
                string line;
                cin >> line;
    
                for (int k = 0; k < C; ++k) {
                    char temp = line[k];
                    building[i][j][k] = temp;
                    if (temp == 'S') start = {i, j, k};
                }
            }
        }

        // S 찾아서 거기부터 bfs 돌기
        int time = bfs(start, building);
        if (time == -1) cout << "Trapped!"<< endl;
        else cout << "Escaped in " << time << " minute(s)."<< endl;
    }
	
    return 0;
}