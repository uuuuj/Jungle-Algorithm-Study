// 공통문제
// https://www.acmicpc.net/problem/1967

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX = 10001;
vector<pair<int, int>> tree[MAX];
bool visited[MAX];
int maxDist = 0;
int farthestNode = 0;

void dfs(int node, int dist) {
    visited[node] = true;

    if (dist > maxDist) {
        maxDist = dist;
        farthestNode = node;
    }

    for (auto& next : tree[node]) {
        int nextNode = next.first;
        int weight = next.second;

        if (!visited[nextNode]) {
            dfs(nextNode, dist + weight);
        }
    }
}

int main() {
    int n;
    cin >> n;

    for (int i = 1; i < n; i++) {
        int parent, child, weight;
        cin >> parent >> child >> weight;
        tree[parent].push_back({child, weight});
        tree[child].push_back({parent, weight});
    }

    // 1. 아무 노드에서 DFS
    dfs(1, 0);

    // 2. 가장 먼 노드에서 다시 DFS
    fill(visited, visited + MAX, false);
    maxDist = 0;
    dfs(farthestNode, 0);

    cout << maxDist << "\n";

    return 0;
}
