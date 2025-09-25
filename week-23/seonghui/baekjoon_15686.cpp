// 공통문제
// https://www.acmicpc.net/problem/15686

#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

vector<pair<int, int>> chicken;
vector<pair<int, int>> houses;
int N, M, minVal;

void calChickenDist(vector<pair<int, int>>& selected) {
	int sum = 0;
	for (auto [i, j] : houses) {
		int val = 2 * N + 1;
		for (auto [x, y] : selected) {
			int dist = abs(i-x) + abs(j-y);
			if (val > dist) val = dist;
		}
		sum += val;
	}
	if (minVal > sum) minVal = sum;
}

void combination(vector<pair<int, int>> selected, int idx) {
	selected.push_back(chicken[idx]);
	if (selected.size() >= M) {
		// 최솟값 연산
		calChickenDist(selected);
		return;
	}
	for (int i = idx+1; i < chicken.size(); ++i) {
		combination(selected, i);
	}
}

int main() {
    cin >> N >> M;
	minVal = 4 * pow(N, 2) + 1;
	
	vector<vector<int>> city(N, vector<int>(N));
	
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; j++) {
			int val;
			cin >> val;
			arr[i][j] = val;
			if (val == 1) {
				houses.push_back({i, j});
			}
			else if (val == 2) {
				chicken.push_back({i, j});
			}
        }
	}

	vector<pair<int, int>> selected;
	// combination
	for (int i = 0; i < chicken.size(); ++i) {
		combination(selected, i);
	}
	
	// 0 빈 1 집 2 치킨
	
	cout << answer + 1 << " " << max + 1 << endl;

    return 0;
}
