// https://school.programmers.co.kr/learn/courses/30/lessons/120842

#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<int> num_list, int n) {
    int row = num_list.size() / n;
    
    vector<vector<int>> answer(row, vector<int>(n));
    
    // n 개씩 나누기
    for (int i = 0; i < num_list.size(); ++i) {
        answer[i/n][i%n] = num_list[i];
    }
    
    return answer;
}