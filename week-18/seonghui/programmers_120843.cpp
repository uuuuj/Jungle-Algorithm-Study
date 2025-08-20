// https://school.programmers.co.kr/learn/courses/30/lessons/120843

#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers, int k) {
    int answer = (1 + 2 * (k-1)) % numbers.size();
    if (!answer) return numbers.size();
    return answer;
}