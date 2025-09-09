// https://school.programmers.co.kr/learn/courses/30/lessons/120847

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> numbers) {
    // 정렬
    sort(numbers.begin(), numbers.end(), greater<int>());
    
    return numbers[0] * numbers[1]; 
}