// https://www.acmicpc.net/problem/30367

#include <iostream>
#include <queue>
#include <vector>
#include <tuple>
#include <array>

using namespace std;

int n, m;

int bfs(pair<int, int> start, vector<vector<char>>& prison, vector<vector<array<bool,4>>>& visited) {
	int move = 0;
	queue<tuple<int, int, int>> q;
	
	auto [startX, startY] = start;
	q.push({startX, startY, -1});

	while (!q.empty()) {
		int size = q.size();
		for (int i = 0; i < size; ++i) {
			auto [x, y, dir] = q.front();
			q.pop();
	
			// 상하좌우
			int dx[4] = {-1, 1, 0, 0};
			int dy[4] = {0, 0, -1, 1};
			
			for (int k = 0; k < 4; ++k) {
				int newX = x + dx[k], newY = y + dy[k];
				if (newX < 0 || newX >= n || newY < 0 || newY >= m) continue;
				if (prison[newX][newY] == '#' || prison[newX][newY] == 'S') continue;
				if (dir >= 0 && (dx[dir] * dy[k]) - (dy[dir] * dx[k]) == -1) continue;
				
				if (prison[newX][newY] == 'E') return ++move;
				
				if (visited[newX][newY][k]) continue;
	
				q.push({newX, newY, k});
				visited[newX][newY][k] = true;
			}
		}
		++move;
	}

	return -1;
}

int main() {
    cin >> n >> m;
	
	vector<vector<char>> prison(n, vector<char>(m));
	vector<vector<array<bool,4>>> visited(
        n, vector<array<bool,4>>(m, {false,false,false,false})
    );
	pair<int, int> start;
	for (int i = 0; i < n; ++i) {
		string line;
        cin >> line;
        
        for (int k = 0; k < m; ++k) {
			char c = line[k];
			if (c == 'S') start = {i, k};
            prison[i][k] = c;
        }
    }
	
	// bfs
	cout << bfs(start, prison, visited) << endl;
	
    return 0;
}
