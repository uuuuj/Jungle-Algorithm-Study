// 공통문제
// https://www.acmicpc.net/problem/9663

#include <iostream>
#include <vector>

using namespace std;

int N, cnt = 0;

void nQueen(int col, vector<pair<int, int>> prev) {
	vector<int> column(N);
	for (auto [x, y] : prev) {
		column[x] = 1;
		int diff = col - y;
		// 범위 체크
		if (x + diff < N) column[x + diff] = 1;
		if (x - diff >= 0) column[x - diff] = 1;
	}
	
	for (int row = 0; row < N; ++row) {
		if (column[row]) continue; // 방문했으면 행 넘어가기
		
		if (col == N - 1) {
			++cnt;
			return;
		}

		auto cur = prev;
		cur.push_back({row, col}); // 1. 배치
		
		nQueen(col + 1, cur); // 2. 다음 열

		// 4. 다음 행
	}

	// 3. 돌아가기
}

int main() {
    cin >> N;

	vector<pair<int, int>> prev;
	nQueen(0, prev);
	
	cout << cnt << endl;

    return 0;
}
