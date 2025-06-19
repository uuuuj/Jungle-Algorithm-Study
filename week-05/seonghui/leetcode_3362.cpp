// https://leetcode.com/problems/zero-array-transformation-iii/description/

#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        int q = queries.size();
        int queryIndex = 0;
        int appliedCount = 0;

        // 쿼리 시작 인덱스 기준으로 정렬
        sort(queries.begin(), queries.end());

        // 최대 힙: 사용 가능한 쿼리들의 종료 인덱스 저장
        priority_queue<int> availableQueries;
        // 최소 힙: 현재 활성화된 쿼리들의 종료 인덱스 저장
        priority_queue<int, vector<int>, greater<int>> activeQueries;

        for (int i = 0; i < n; ++i) {
            // 현재 인덱스에서 시작하는 쿼리를 availableQueries에 추가
            while (queryIndex < q && queries[queryIndex][0] == i) {
                availableQueries.push(queries[queryIndex][1]);
                ++queryIndex;
            }

            // 현재 인덱스를 포함하지 않는 활성 쿼리 제거
            while (!activeQueries.empty() && activeQueries.top() < i) {
                activeQueries.pop();
            }

            // nums[i]를 0으로 만들기 위해 필요한 쿼리 적용
            while (nums[i] > static_cast<int>(activeQueries.size())) {
                if (availableQueries.empty() || availableQueries.top() < i) {
                    return -1; // 더 이상 사용할 수 있는 쿼리가 없음
                }
                activeQueries.push(availableQueries.top());
                availableQueries.pop();
                ++appliedCount;
            }
        }

        return q - appliedCount; // 사용되지 않은 쿼리 수 반환
    }
};
